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
char words[5000][20];
bool memo[5000][20];
char inp[600];
int calc[20];
main()
{
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;i++) scanf("%s",words[i]);
	for(int i=0;i<N;i++){
		int howmany=0;
		scanf("%s",inp);
		int pos=0,num=0,glen=strlen(inp);
		for(int j=0;j<glen;j++){
			if(inp[j]=='('){
				int t=j+1;
				while(inp[t]!=')'){
					num=num|(1<<(inp[t]-'a'));
					t++;
				}
				calc[pos]=num;
				j=t;
			}
			else{
				calc[pos]=1<<(inp[j]-'a');
			}
			num=0;
			pos++;
		}
		memset(memo,0,sizeof(memo));
		for(int j=0;j<D;j++){
			for(int k=0;k<L;k++){
				if((calc[k]&(1<<(words[j][k]-'a')))!=0)  {memo[j][k]=true;}
			}
		}
		int count=0;
		for(int j=0;j<D;j++){
			bool fnd=false;
			for(int k=0;k<L;k++){
				if(!memo[j][k]) {fnd=true;break;}
			}
			if(!fnd) count++;
		}
		printf("Case #%d: %d\n",(i+1),count);
	}
}