// Author : Muhammad Rifayat Samee
// Problem : B
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif




using namespace std;
struct tri{
	int sum;
	int f;
	int a;
	int b;
	int c;
	int max;
}T[35][180];
int in,n,s,p;
int how[35];
int score[105];
int memo[105][105][105];
int done[105][105][105],cc=1;
void precal(){
	int s,i,j,k;
	int a[5];
	in = 0;
	for(s=0;s<=30;s++){
		in = 0;
		for(i=0;i<=s;i++){
			
			for(j=0;j<=s-i;j++){
				a[0] = i;
				a[1] = j;
				k = s - i - j;
				a[2] = k;
				sort(a,a+3);
				if(a[1]-a[0]>2 || a[2]-a[0]>2 || a[2]-a[1]>2 || a[0]>10 || a[1]>10 || a[2]>10 ){
					continue;
				}
				if(a[1]-a[0]==2 || a[2]-a[0]==2 || a[2]-a[1]==2){
					T[s][in].sum = s;
					T[s][in].a = a[0];
					T[s][in].b = a[1];
					T[s][in].c = a[2];
					T[s][in].f= 1;
					T[s][in].max = a[2];
					in++;
				}
				else{
					T[s][in].sum = s;
					T[s][in].a = a[0];
					T[s][in].b = a[1];
					T[s][in].c = a[2];
					T[s][in].f= 0;
					T[s][in].max = a[2];
					in++;
				}
			}
		}
		how[s] = in;
	}
}

int dp(int i,int f,int tot){
	if(i==n){
		if(f==s){
			return tot;
		}
		else return 0;
	}
	if(done[i][f][tot]==cc)
		return memo[i][f][tot];
	int res = 0,r,s,j;
	s = score[i];
	r = 0;
	for(j=0;j<how[s];j++){
		if(T[s][j].f==1){
			if(T[s][j].max>=p)
				r = dp(i+1,f+1,tot+1);
			else
				r = dp(i+1,f+1,tot);
		}
		else{
			if(T[s][j].max>=p)
				r = dp(i+1,f,tot+1);
			else
				r = dp(i+1,f,tot);
		}
		if(res<r)
			res = r;
	}
	done[i][f][tot] = cc;
	memo[i][f][tot] = res;
	return res;
}
int main(){

	//freopen("Bl.in","r",stdin);
	//freopen("out.txt","w",stdout);
	precal();
	//printf("%d\n",in);
	int cases,a,b,c,i,j,f,r,k,res,ct=1;
	/*for(j=0;j<=30;j++){
		printf("%d\n",j);
		for(i=0;i<how[j];i++){
			printf("%d %d %d %d\n",T[j][i].a,T[j][i].b,T[j][i].c,T[j][i].f);
		}
		printf("\n");
	}*/

	scanf("%d",&cases);
	while(cases--){
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++){
			scanf("%d",&score[i]);
		}
		printf("Case #%d: %d\n",ct++,dp(0,0,0));
		cc++;
	}
	return 0;
}