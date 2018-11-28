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
int nums[40];
char inp[100];
int memo[100000][40];
int chk(int val,int dig)
{
	//cout<<val<<endl;
	if(memo[val][dig]==-2)return memo[val][dig]=0;
	if(memo[val][dig]!=-1)return memo[val][dig]; 
	memo[val][dig]=-2;
	int gsum=0,gval=val;
	while(gval!=0){
		int ggsum=gval/dig;
		int mgsum=gval-ggsum*dig;
		gsum+=mgsum*mgsum;
		gval=ggsum;
	}
	//evaluate the corresponding number
	if(chk(gsum,dig))return memo[val][dig]=1;
	return memo[val][dig]=0;
}
main()
{
	int t;
	scanf("%d\n",&t);
	memset(memo,-1,sizeof(memo));
	for(int i=2;i<40;i++)
	memo[1][i]=1;
	int tc=1;
	while(t--!=0){
		int a,b;
		gets(inp);
		int len=strlen(inp);
		string st=string(inp);
		int finp;
		stringstream ss(st);
		int l=0;
		while(ss>>finp){
			nums[l++]=finp;	
		}
		int ans=2;
		while(true){
			//cout<<ans<<endl;
			int j=0;
			for(j=0;j<l;j++){
				int num=0,gn=ans;
				/*
				while(gn!=0){
					int ggn=gn/nums[j];
					int mn=gn-ggn*nums[j];
					num+=mn*mn;
					gn=ggn;
				}
				//cout<<j<<endl;
				*/
				//if(ans==3) cout<<num<<endl;
				if(chk(ans,nums[j])==0)break;
			}
			if(j==l)break;
			ans++;
		}
		printf("Case #%d: %d\n",tc++,ans);
	}
}