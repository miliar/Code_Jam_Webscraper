#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int N=0;
int S=0;
int Q=0;
string se[105];
string in[1005];
bool seb[105];
int t=0;

int main ()
{
 	int count;
 	scanf ("%d",&N);
 	getchar ();
 	int i,j,k,ii;
 	for (i=1; i<=N; i++) {
		scanf ("%d",&S);
		getchar ();
		for (k=1; k<=S; k++) {
			seb[k]=0;
		}
		t=0;
		count=0;
		for (j=1; j<=S; j++) getline(cin, se[j]);
		scanf ("%d",&Q);
		getchar ();
		for (j=1; j<=Q; j++) {
			getline(cin, in[j]);
			for (k=1; k<=S; k++) {
				if (se[k]==in[j] && seb[k]==0) {
				   				  seb[k]=1;
				   				  t++;
				   				  break;
				   				  }
			}
			if (t==S) {
			   		  count++;
			   		  t=1;
			   		  for (ii=1; ii<=S; ii++) {
					  	  if (ii==k) continue;
					  	  seb[ii]=0;
					  }
					  }		  
		}
		printf ("Case #%d: %d\n",i,count);
	}
	return 1;
}
