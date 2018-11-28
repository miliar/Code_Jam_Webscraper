#define MD(x) if (0) {x;}
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
void MyAssert(int p){ while (!p) printf("error\n"); };
#define O1(S,A,n) MD(cout<<S<<":";for (int i=0; i<n; i++)cout<<A[i]<<" ";cout<<endl;)
#define O2(S,A,n) MD(cout<<S<<"\n";for (int i=0; i<n; i++){for (int j=0; j<n; j++)cout<<A[i][j]<<" ";cout<<endl;})
using namespace std;


const int maxN = 100;
int A[maxN][maxN];
int N;

bool ok(int i, int row){ // put A[i] on row?
	for (int j=row+1; j<N; j++)
		if (A[i][j]) return false;
	return true;
}

void swapRow(int i, int j){
	for (int k=0; k<N; k++)
		swap(A[i][k],A[j][k]);
}


int main(){
	int tc;
	scanf("%d",&tc);
	for (int ti=1; ti<=tc; ti++){
		printf("Case #%d: ",ti);
		// TODO
		scanf("%d",&N);
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				scanf("%1d",&A[i][j]);
		int ans = 0;
		for (int i=0; i<N; i++){
			int j = i;
			for (; j<N; j++)
				if ( ok(j,i) ) break;
			MD(cout<<"swap "<<i<<" "<<j<<endl;)
			for (int k=j; k>i; k--){
				swapRow(k,k-1);
				ans ++;
			}
		}
		printf("%d\n",ans);
	}
	
	return 0;
}
