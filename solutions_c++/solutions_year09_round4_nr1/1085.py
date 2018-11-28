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
ll vals[70];
char inp[100];
int swp=100000;
int n;
main()
{
	int t;
	scanf("%d",&t);
	int tc=1;
	while(t--!=0){
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",inp);
			int len=strlen(inp);
			vals[i]=0;
			for(int j=0;j<len;j++){
				if(inp[j]=='1')vals[i]|=(1LL<<j);
			}
		}
		swp=0;
		for(int i=0;i<n;i++){
			ll req=(1LL<<(i+1))-1;
			if(vals[i]<=req)continue;
			for(int j=i+1;j<n;j++){
				if(vals[j]<=req){
					swp+=(j-i);
					ll t=vals[j];
					for(int k=j;k>i;k--) vals[k]=vals[k-1];
					vals[i]=t;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",tc++,swp);
	}
}