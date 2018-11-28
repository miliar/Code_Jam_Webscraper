#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>

#define MAXN 1005
using namespace std;

string N[MAXN];

string gen(int a){
	string A;
	while(a!=0){
		int q = a%10;
		A+=(char)(q+'0');
		a/=10;
	}
	reverse(A.begin(),A.end());
	return A;
}

bool isRec(int a,int b){
	string A = N[a];
	string B = N[b];

	int l = A.length();
	for(int j=0;j<l;j++){
		if(B[j] == A[0]){
			int p = j;
			bool f = true;
			for(int i=0;i<l;i++){
				if(A[i] != B[p]){
					f = false;
					break;
				}
				p = ((p+1)%l);
			}
			if(f) return true;
		}
	}
	return false;
}

int main()
{
	freopen("tc.in","r",stdin);
	freopen("tc.out","w",stdout);
	
	for(int q=0;q<MAXN;q++){
		N[q] = gen(q);
	}

	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		int A,B,i,j;
		scanf("%d %d",&A,&B);

		int cnt = 0;
		for(i=A;i<B;i++){
			for(j=i+1;j<=B;j++){
				if(isRec(i,j) ) cnt++;
			}
		}
		
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}