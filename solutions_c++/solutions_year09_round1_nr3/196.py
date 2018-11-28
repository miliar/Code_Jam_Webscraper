#include<iostream>
#include<string>
#include<cstring>
#include<map>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<sstream>
#include<set>
#include<stack>
#define vi vector<int>
#define vvi vector<vector<int> > 
#define vpi vector<pair<int,int> >
#define vvpi vector<vector<pair<int,int> > > 
#define pi pair<int,int> 
#define ll long long
#define boolean bool
using namespace std;
ll C[41][41];
int n,c;
double memo[10001][42];
boolean fmemo[10001][42];
double val(int i,int sel)
{
	//change please
	if(i>10000) return 0;
	if(sel==c)return i;
	if(fmemo[i][sel])return memo[i][sel];
	fmemo[i][sel]=1;
	double ret=0;
	for(int s=0;s<=n;s++){
		if(s<=sel&&(n-s)<=(c-sel)){
			ret+=((double)C[sel][s]/C[c][n])*C[c-sel][n-s]*val(i+1,sel+n-s);
		}
	}
	return memo[i][sel]=ret;
}
main()
{
	C[0][0]=1;
	for(int i=1;i<41;i++){
		C[i][0]=1;
		for(int j=1;j<=i;j++){
			C[i][j]=C[i-1][j]+C[i-1][j-1];
		}
	}
	int t;
	scanf("%d",&t);
	int tc=1;
	while(t--!=0){
		scanf("%d%d",&c,&n);
		memset(fmemo,0,sizeof(fmemo));
		printf("Case #%d: %llf\n",tc++,val(0,0));
		
	}
}