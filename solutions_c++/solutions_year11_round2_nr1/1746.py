
#include <stdio.h>
using namespace std;

class A {
  private:
    char mat[100][100];
    int max_team;
    double rpi[100];
    double wp[100];
    double owp[100];
    double oowp[100];
    double result;
  public:
    A() {
      result = 0.0;
    }

    ~A() {
    }

    void setMax(int i){
      max_team = i;
    }
    void setMatrix(char c, int i, int j) {
      mat[i][j] = c;
    }
    double computeWP(int team) {
      int numwin = 0, numlose = 0;
      for (int j = 0; j < max_team; j++) {
	if (mat[team][j] == '1') {
	  ++numwin;
	}
	else if (mat[team][j] == '0') {
	  ++numlose;
	}
	else {
	}
      }
      return (((double)numwin) / ((double)numwin+numlose));
    }
    void computeResult() {
      int i,j;
      char backup[100];
      // Compute WP
      for (i = 0; i < max_team; i++) {
	wp[i] = computeWP(i);
      }
      // Compute OWP
      for (i = 0; i < max_team; i++) {
	int numteam = 0;
	double lowp = 0.0;
	// save
	for (j = 0; j < max_team; j++) {
	  backup[j] = mat[j][i];
	  mat[j][i] = '.';
	}

	for (j = 0; j < max_team; j++) {
	  if (backup[j] != '.') {
	    ++numteam;
	    lowp += computeWP(j);
	  }
	}
	owp[i] = lowp / numteam;

	// restore
	for (j = 0; j < max_team; j++) {
	  mat[j][i] = backup[j];
	}
      }

      // Compute OOWP
      for (i = 0; i < max_team; i++) {
	int numteam = 0;
	double lowp = 0.0;
	for (j = 0; j < max_team; j++) {
	  if (mat[i][j] != '.') {
	    ++numteam;
	    lowp += owp[j];
	  }
	}
	oowp[i] = lowp / numteam;
      }

      // Compute RPI
      for (i = 0; i < max_team; i++) {
	rpi[i] = (0.25 * wp[i]) + (0.5 * owp[i]) + (0.25 * oowp[i]);
      }
    }
    void print() {
      int i,j;
      for (i = 0; i < max_team; i++) {
	for (j = 0; j < max_team; j++) {
	  printf(" %c", mat[i][j]);
	}
	printf("\n");
      }
      printf("---------\n");
    }
    void printResult(FILE *fp) {
      for (int i = 0; i < max_team; i++) {
	fprintf(fp, "\n%lf", rpi[i]);
	//printf("%f, %f, %f, %f\n", wp[i], owp[i], oowp[i], rpi[i]);
      }
    }
};

void skipWS(FILE *fp)
{
  char s[1024];
  fscanf(fp, "%[ \t\n]", s);
}

int main(int argc, char **argv)
{
  FILE *infile = NULL, *outfile = NULL;
  int numtests = 0, i = 0, j = 0, k = 0;
  A *alist = NULL;

  if (argc != 2) {
    printf("Usage %s <input_file>\n", argv[0]);
    return -1;
  }

  infile = fopen(argv[1], "r");
  if (!infile) {
    printf("Cannot find file %s\n", argv[1]);
    return -1;
  }

  outfile = fopen("result.out", "w");
  if (!outfile) {
    printf("Cannot open output file result.out for writing.\n");
    fclose(infile);
    return -1;
  }

  fscanf(infile, "%d", &numtests);
  if (numtests <= 0) {
    fclose(infile);
    fclose(outfile);
    return 0;
  }

  alist = new A[numtests];
  for (k = 0; k < numtests; k++) {
    int numpos, b;
    char r;

    skipWS(infile);
    fscanf(infile, "%d", &numpos);
    alist[k].setMax(numpos);

    for (i = 0; i < numpos; i++) {
      for (j = 0; j < numpos; j++) {
	skipWS(infile);
	fscanf(infile, "%c", &r);
	alist[k].setMatrix(r, i, j);
      }
    }
  }
  fclose(infile); infile = NULL;

  for (i = 0; i < numtests; i++) {
    alist[i].computeResult();

    fprintf(outfile, "Case #%d: ", i + 1);
    alist[i].printResult(outfile);
    fprintf(outfile, "\n");
  }

  delete [] alist;

  fclose(outfile);
  return 0;
}

