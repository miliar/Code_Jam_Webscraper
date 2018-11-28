#include <iostream.h>
#include <string.h>

int NumberOfTests;
int S,Q;
char SearchEngines[100][101];
char Input[101];
int Answer[2][100];

void main() {
  int I,J,K,M;

  cin>>NumberOfTests;M=0;
  while (M++<NumberOfTests) {
    cin>>S;
    I=0;
    while (I<S) {Answer[0][I]=0;Answer[1][I]=0;++I;}

    cin.getline(SearchEngines[0],101);
    I=0;
    while (I<S) {
      cin.getline(SearchEngines[I],101);
      ++I;
    }

    cin>>Q;
    cin.getline(Input,101);
    I=0;
    while (I<Q) {
      cin.getline(Input,101);
      J=0;
      K=0;
      while (K<S) {
	Answer[1-(I&1)][K]=Answer[I&1][K];
	++K;
      }
      while (J<S) {
	if (strcmp(Input,SearchEngines[J])==0) {
	  Answer[1-(I&1)][J]=32000;

	  K=0;
	  while (K<S) {
	    if (K!=J) {
	      if (Answer[I&1][J]+1<Answer[1-(I&1)][K]) Answer[1-(I&1)][K]=Answer[I&1][J]+1;
	    }
	    ++K;
	  }
	}
	++J;
      }
      ++I;
    }

    for (J=0;J<S;++J)
      if (Answer[I&1][J]<Answer[I&1][0]) Answer[I&1][0]=Answer[I&1][J];

    cout<<"Case #"<<M<<": "<<Answer[I&1][0]<<endl;
  }
}