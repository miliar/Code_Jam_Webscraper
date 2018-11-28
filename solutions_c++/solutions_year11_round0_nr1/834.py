#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

char C[100]; // color sequence
int P[100]; // position sequence

int main()
{
	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	//freopen("A-small.in","r",stdin);freopen("A-small.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N;
    cin >> N;
		for(int i=0; i<N; i++)
			cin >> C[i] >> P[i];
   
    long long t=0;
    int a=1, b=1; //loop invarience: a=current pos of 'O', b=current pos of 'B'
    long long t0=0;
    int nO=0; // next occurence of 'O'
    int nB=0; // next occurence of 'B'
    int j=0;
    for(int i=0; i<N; i++) {
      // update next occurrence of 'B' in C[]
      if (nB<=i) {
        for(j=i+1; j<N; j++) {
          if(C[j]=='B') {
            nB = j;
            break;
          }
        }
      }
      // update next occurrence of 'O' in C[]
      if (nO<=i) {
        for(j=i+1; j<N; j++) {
          if(C[j]=='O') {
            nO = j;
            break;
          }
        }
      }
      if(C[i]=='O') {
        t0 = abs(P[i]-a)+1; // time required to move O from a to P[i], and push button
        // move O to position P[i]
        t = t+t0;
        a = P[i];
        // if next B exits, move B to a point closest to P[nB] in time t0
        if (nB>i) {
          if(abs(P[nB]-b) <= t0) 
            b = P[nB];
          else {
            if(P[nB] > b)
              b += t0;
            else
              b -= t0;
          }
        }
      }
      else  { // (C[i]=='B')
        t0 = abs(P[i]-b)+1; // time required to move B from b to P[i], and push button
        // move B to position P[i] and push button
        t = t+t0;
        b = P[i];
        // if next O exits, move O to a point closest to P[nO] in time t0
        if(nO>i) {
            if(abs(P[nO]-a) <= t0) 
              a = P[nO];
            else {
              if(P[nO] > a)
                a += t0;
              else
                a -= t0;
            }
        }
      }
      //printf("after i=%d, a=%d, b=%d, t=%d, nO=%d, nB=%d, \n", i+1, a, b, t, nO, nB);
    }

		printf("Case #%d: ",caseId);
		printf("%lld", t);
		printf("\n");
	}

	return 0;
}
