#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int dp[11][1<<11];

#define M 10007

int has2ones(int x){
	while(x){
		if (x%4==3) return 1;
		x/=2;
	}
	return 0;
}

int collider(int c, int x){
	int ret=0,i;
	for (i=1; i<c; i++){
		if ((x>>i)&1) ret|=(1<<(i-1));
	}
	for (i=0; i<c-1; i++){
		if ((x>>i)&1) ret|=(1<<(i+1));
	}
	return ret;
}

int bcount(int x){
	int c=0;
	while(x){
		if (x&1) c++;
		x/=2;
	}
	return c;
}

#define max(a,b) (((a)>(b))?(a):(b))

string b[100];
int pat[100],bitcount[1<<11];
int ok[1<<11],colliders[1<<11];

int main(){
	int i,j,k,u,t,r,c;
	cin>>t;
	for (i=0; i<(1<<10); i++){
		ok[i]=1-has2ones(i);
		bitcount[i]=bcount(i);
	}

	for (u=0; u<t; u++){
		cin>>r>>c;
		for (i=0; i<(1<<c); i++)
			colliders[i]=collider(c,i);

		for (i=0; i<r; i++){
			cin>>b[i];
			pat[i]=0;
			for (j=0; j<c; j++){
				if (b[i][j]=='x')
					pat[i]|=(1<<j);
			}
		}
		
		for (i=0; i<(1<<c); i++){
			if (ok[i] && (pat[0]&i)==0)
				dp[0][i]=bitcount[i];
			else 
				dp[0][i]=0;
		}
		for (i=1; i<r; i++){
			for (j=0; j<(1<<c); j++)
				dp[i][j]=0;
			for (j=0; j<(1<<c); j++){
				if (!ok[j]) continue;
				if ((pat[i]&j)!=0) continue;
				for (k=0; k<(1<<c); k++){
					if (!ok[k]) continue;
					if (colliders[j]&k) continue;
					dp[i][j]=max(dp[i][j],dp[i-1][k]+bitcount[j]);
				}
			}
		}

		int res=0;
		for (j=0; j<(1<<c); j++){
			if (dp[r-1][j]>res)
				res=dp[r-1][j];
		}
		cout<<"Case #"<<(u+1)<<": "<<res<<endl;

	}
	return 0;
}
