#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<numeric>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;
#define pb push_back

int n;
int main(){
	int runs;
	scanf("%d",&runs);
	for(int r = 1; r <= runs; r++){
		scanf("%d",&n);	
		vector <int> A;vector <char> B;
		for(int i=0;i<n;i++){
			char c; int val;cin>>c>>val;
			A.pb(val); B.pb(c);
		}
		int res = 0, endO = 1,endB = 1, bef = 0;
		char who = 'X';
		for(int i = 0;i < A.size(); i++){
			if(B[i] == 'O'){
				if(B[i] == who){
					res += abs(A[i]-endO)+1;
					bef += abs(A[i]-endO)+1;
					who = B[i];
					endO = A[i];
					continue;
				}
				int D = abs(A[i]-endO);
				if(D-bef <= 0) D = 0;
				else D -= bef;
				res += D + 1;
				bef = D + 1;
				endO = A[i];
				who = B[i];
			}else{
				if(B[i] == who){
					res += fabs(A[i] - endB) + 1;
					bef += fabs(A[i] - endB) + 1;
					who = B[i]; endB = A[i];
					continue;
				}
				int D = fabs(A[i]-endB);
				if(D - bef <= 0) D = 0;
				else D -= bef;
				res += D+1; bef = D+1;endB = A[i];who = B[i];
			}
		}
		printf("Case #%d: %d\n",r,res);
	}
	return 0;
}
