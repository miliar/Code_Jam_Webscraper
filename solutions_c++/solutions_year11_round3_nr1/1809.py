
#include <stdio.h>
using namespace std;

class A {
  private:
    char mat[100][100];
    int row;
    int col;
    int possible;
    char result[100][100];
  public:
    A() {
      row = 0;
      col = 0;
      possible = 1;
    }

    ~A() {
    }

    void setRowCol(int r, int c){
      row = r;
      col = c;
    }
    void setMatrix(char c, int i, int j) {
      mat[i][j] = c;
    }
    void computeResult() {
      char next;
      for (int i = 0; i < row; i++) {
	for (int j = 0; j < col; j++) {
	  if (mat[i][j] == '#') {
	    if (j+1 < col) {
	      if (mat[i][j+1] != '#') {
		possible = 0;
		return;
	      }
	      else {
		++j;
	      }
	    }
	    else {
	      possible = 0;
	      return;
	    }
	  }
	}
      }

      for (int i = 0; i < col; i++) {
	for (int j = 0; j < row; j++) {
	  if (mat[j][i] == '#') {
	    if (j+1 < row) {
	      if (mat[j+1][i] != '#') {
		possible = 0;
		return;
	      }
	      else {
		++j;
	      }
	    }
	    else {
	      possible = 0;
	      return;
	    }
	  }
	}
      }

      // set red
      for (int i = 0; i < row; i++) {
	for (int j = 0; j < col; j++) {
	  if (mat[i][j] == '#') {
	    mat[i][j] = '/';
	    mat[i][j+1] = '\\';
	    mat[i+1][j] = '\\';
	    mat[i+1][j+1] = '/';
	  }
	}
      }
    }
    void printResult(FILE *fp) {
      if (possible == 0) {
	fprintf(fp, "\nImpossible");
      }
      else {
	for (int i = 0; i < row; i++) {
	  fprintf(fp, "\n");
	  for (int j = 0; j < col; j++) {
	    fprintf(fp, "%c", mat[i][j]);
	  }
	}
      }
    }
    void print() {
      for (int i = 0; i < row; i++) {
	for (int j = 0; j < col; j++) {
	  printf("%c ", mat[i][j]);
	}
	printf("\n");
      }
      printf("================\n");
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
    int row, col;
    char r;

    skipWS(infile);
    fscanf(infile, "%d", &row);
    skipWS(infile);
    fscanf(infile, "%d", &col);
    alist[k].setRowCol(row, col);

    for (i = 0; i < row; i++) {
      for (j = 0; j < col; j++) {
	skipWS(infile);
	fscanf(infile, "%c", &r);
	alist[k].setMatrix(r, i, j);
      }
    }
  }
  fclose(infile); infile = NULL;

  for (i = 0; i < numtests; i++) {
    // alist[i].print();
    alist[i].computeResult();

    fprintf(outfile, "Case #%d: ", i + 1);
    alist[i].printResult(outfile);
    fprintf(outfile, "\n");
  }

  delete [] alist;

  fclose(outfile);
  return 0;
}

