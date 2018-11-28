
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

typedef enum {Q = 0, W, E, R, A, S, D, F, UNINIT} Base_elements;

class Magicka {
  private:
    char combine[8][8];
    Base_elements opposed[8];
    char *stimulus;
    char *result;

  public:
    Magicka() {
      int i = 0, j = 0;

      stimulus = NULL;
      result = NULL;

      for (i = 0; i < 8; i++) {
	for (j = 0; j < 8; j++) {
	  combine[i][j] = '\0';
	}
	opposed[i] = UNINIT;
      }
    }

    ~Magicka() {
      if (stimulus) free(stimulus);
      if (result) free(result);
    }

    Base_elements mapBase(char c) {
      Base_elements e = UNINIT;
      switch (c) {
	case 'Q':
	  e = Q;
	  break;
	case 'W':
	  e = W;
	  break;
	case 'E':
	  e = E;
	  break;
	case 'R':
	  e = R;
	  break;
	case 'A':
	  e = A;
	  break;
	case 'S':
	  e = S;
	  break;
	case 'D':
	  e = D;
	  break;
	case 'F':
	  e = F;
	  break;
	default:
	  break;
      }
      return e;
    }

    char rMapBase(Base_elements r) {
      char e = 'x';
      switch (r) {
	case Q:
	  e = 'Q';
	  break;
	case W:
	  e = 'W';
	  break;
	case E:
	  e = 'E';
	  break;
	case R:
	  e = 'R';
	  break;
	case A:
	  e = 'A';
	  break;
	case S:
	  e = 'S';
	  break;
	case D:
	  e = 'D';
	  break;
	case F:
	  e = 'F';
	  break;
	default:
	  break;
      }
      return e;
    }

    void addCombine(char *s) {
      combine[mapBase(s[0])][mapBase(s[1])] = s[2];
    }

    void addOpposed(char key, char data) {
      if (opposed[mapBase(key)] == UNINIT)
	opposed[mapBase(key)] = mapBase(data);
    }

    void addStimulus(char *s) {
      stimulus = s;
    }

    void execute() {
      int start = 0, end = 0;
      int alpha[8];
      char *ptr = stimulus;

      if (!ptr) return;
      result = strdup(ptr);

      for (int i = 0; i < 8; i++) {
	alpha[i] = 0;
      }

      while (*ptr != '\0') {
	if (mapBase(*ptr) == UNINIT) {
	  printf("Bad input\n");
	  return;
	}

	alpha[mapBase(*ptr)] += 1;
	result[end] = *ptr;
	if (start != end) {
	  // Handle combine
	  char r = '\0';
	  if ((mapBase(result[end]) != UNINIT) && (mapBase(result[end-1]) != UNINIT)) {
	    r = combine[mapBase(result[end-1])][mapBase(result[end])];
	    if (r == '\0') {
	      r = combine[mapBase(result[end])][mapBase(result[end-1])];
	    }
	  }
	  if (r != '\0') {
	    alpha[mapBase(result[end - 1])] -= 1;
	    alpha[mapBase(result[end])] -= 1;
	    --end;
	    result[end] = r;
	  }
	  else {
	    // Handle opposed
	    Base_elements opp = UNINIT;
	    
	    if (mapBase(result[end]) != UNINIT)
	      opp = opposed[mapBase(result[end])];

	    if (opp != UNINIT) {
	      if (alpha[opp] > 0) {
		end = start - 1;
		for (int k = 0; k < 8; k++) {
		  alpha[k] = 0;
		}
	      }
	    }
	  }
	}
	++end;
	++ptr;
      }
      result[end] = '\0';
    }

    void print(FILE *fp) {
      fprintf(fp, "Combine Hash:\n");
      for (int i = 0; i < 8; i++) {
	for (int j = 0; j < 8; j++) {
	  if (combine[i][j] != '\0')
	    fprintf(fp, "[%c%c, %c]", rMapBase((Base_elements)i), rMapBase((Base_elements)j), combine[i][j]);
	}
      }
      fprintf(fp, "\n");
      fprintf(fp, "Opposed Hash:\n");
      for (int i = 0; i < 8; i++) {
	if (opposed[i] != UNINIT)
	  fprintf(fp, "[%c, %c]", rMapBase((Base_elements)i), rMapBase(opposed[i]));
      }
      fprintf(fp, "\n");

      fprintf(fp, "Stimulus: %s\n", stimulus);
    }

    void printResult(FILE *fp) {
      char *r = result;
      fprintf(fp, "[");
      while (r && (*r != '\0')) {
	fprintf(fp, "%c", *r);
	++r;
	if (*r != '\0')
	  fprintf(fp, ", ");
      }
      fprintf(fp, "]");
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
  int numtests = 0, i = 0, j = 0;
  Magicka *magics = NULL;

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

  magics = new Magicka[numtests];
  for (i = 0; i < numtests; i++) {
    int num_combine, num_opposed, num_stimulus;
    char combine[4];
    char opposed[3];
    char *stimulus = NULL;

    skipWS(infile);
    fscanf(infile, "%d", &num_combine);
    for (j = 0; j < num_combine; j++) {
      skipWS(infile);
      fscanf(infile, "%s", combine);
      magics[i].addCombine(combine);
    }
    skipWS(infile);
    fscanf(infile, "%d", &num_opposed);
    for (j = 0; j < num_opposed; j++) {
      skipWS(infile);
      fscanf(infile, "%s", opposed);
      magics[i].addOpposed(opposed[0], opposed[1]);
      if (opposed[0] != opposed[1])
	magics[i].addOpposed(opposed[1], opposed[0]);
    }
    skipWS(infile);
    fscanf(infile, "%d", &num_stimulus);
    if (num_stimulus > 0) {
      skipWS(infile);
      stimulus = (char *)calloc(num_stimulus+1, sizeof(char));
      fscanf(infile, "%s", stimulus);
      magics[i].addStimulus(stimulus);
    }
  }
  fclose(infile); infile = NULL;

  for (i = 0; i < numtests; i++) {
#if 1
    magics[i].execute();

    fprintf(outfile, "Case #%d: ", i + 1);
    magics[i].printResult(outfile);
    fprintf(outfile, "\n");
#endif
#if 0
    /* Test */
    magics[i].print(stdout);
#endif
  }

  delete [] magics;

  fclose(outfile);
  return 0;
}

