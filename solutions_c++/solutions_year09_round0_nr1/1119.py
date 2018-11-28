// GCJ.cpp : Defines the entry point for the console application.

#include <stdio.h>
#include <iostream>
using namespace std;

void Alien(){
  int L, D, N;

  scanf("%d", &L);
  scanf("%d", &D);
  scanf("%d", &N);

  int i, k;
  char ** pWords = new char*[D];
  for(i = 0; i < D; i++){
    pWords[i] = new char[L+1];
  }

  char ch;
  scanf("%c", &ch);
  for(i = 0; i < D; i++){
    for(k = 0; k < L; k++){
      scanf("%c", &ch);
      pWords[i][k] = ch;
    }
    scanf("%c", &ch); // \n
    pWords[i][L] = 0;
  }

  bool ** pHash = new bool*[L];
  for(i = 0; i < L; i++){
    pHash[i] = new bool[26];
  }

  for(i = 0; i < N; i++){
    for(k = 0; k < L; k++)
      memset(pHash[k], 0, 26);

    for(k = 0; k < L; k++){
      scanf("%c", &ch);
      if(ch!='(')
        pHash[k][ch-'a'] = 1;
      else{
        scanf("%c", &ch);
        while(ch != ')'){
          pHash[k][ch - 'a'] = 1;
          scanf("%c", &ch);
        }
      }
    }
    scanf("%c", &ch); // \n

    // match
    int cnt = 0;
    int d = 0;
    for(d = 0; d < D; d++){
      for(k = 0; k < L; k++){
        if( ! pHash[k][ pWords[d][k]-'a' ])
          break;
      }
      if(k == L)
        cnt++;
    }

    printf("Case #%d: ", i+1);
    printf("%d\n", cnt);
  }

  for(i = 0; i < L; i++){
    delete [] pHash[i];
  }
  delete [] pHash;

  for(i = 0; i < D; i++){
    delete [] pWords[i];
  }
  delete [] pWords;
}

int main()
{
  Alien();
  //Welcome();
	return 0;
}

