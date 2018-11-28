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
char lets[20]="welcome to code jam";
char inp[510];
int len;
int memo[510][20];
int howMany(int i,int j)
{
	if(memo[i][j]!=-1) return memo[i][j];
	if(j>=19) return memo[i][j]=1;
	if(i>=len) return memo[i][j]=0;
	int calc=0;
	for(int t=i;t<len;t++){
		if(inp[t]==lets[j]) {
			int tak=howMany(t+1,j+1);
			//if(tak==-2)continue;
			calc=(calc+tak); 
			if(calc>=10000) calc%=10000;
		}
	}
	return memo[i][j]=calc;
}
main()
{
	int N;
	scanf("%d\n",&N);
	for(int i=0;i<N;i++){
		memset(memo,-1,sizeof(memo));
		gets(inp);
		len=strlen(inp);
		printf("Case #%d: %04d\n",(i+1),howMany(0,0));
	}
}