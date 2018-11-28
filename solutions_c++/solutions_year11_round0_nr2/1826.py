#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <climits>
#define REP(i,n) for(int (i)=0, _n=(n); (i) < (_n); i++)
#define REPD(i,n) for(int (i)=(n-1); i >= 0; i--)
#define FOR(i,a,n) for(int (i)=(a),_n=(n); (i) <= (_n); (i)++)
#define FORD(i,a,n) for(int (i)=(a),_n=(n); (i) >= (_n); (i)--)
#define MAXN 120
using namespace std;

int main(int argc, char **argv)
{

		freopen("B.in","r",stdin);
		freopen("B.txt","w",stdout);	
	
	
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		int c,d,n;
		int com[30][30]={};
		bool des[30][30]={};
		char str[MAXN],ans[MAXN]={};
		
		memset(com,-1,sizeof com);
		scanf("%d",&c);
		REP(i,c){
			char t[10];
			scanf("%s",t);
			t[0]-='A';t[1]-='A';t[2]-='A';
			com[t[0]][t[1]]=com[t[1]][t[0]]=t[2];	
		}
		
		scanf("%d",&d);
		REP(i,d){
			char t[10];
			scanf("%s",t);
			t[0]-='A';t[1]-='A';
			des[t[0]][t[1]]=des[t[1]][t[0]]=1;	
		}
		
		int idx=0;
		scanf("%d",&n);
		scanf("%s",str);
		REP(i,n){
			str[i]-='A';
			if(idx && com[str[i]][ans[idx-1]]!=-1){
				ans[idx-1]=com[str[i]][ans[idx-1]];
				continue;
			}
			bool b= 0;
			REP(j,idx)
				if(des[str[i]][ans[j]]){
					idx=0;
					b=1;
					break;	
				}
				
			if(!b)ans[idx++]=str[i];
		}
		
		printf("Case #%d: [",cs);
		REP(i,idx){
			if(i)printf(", ");
			printf("%c",ans[i]+'A');	
		}
		puts("]");
	}
    return 0;
}
