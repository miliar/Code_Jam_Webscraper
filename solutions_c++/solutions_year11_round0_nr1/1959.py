//Google Code Jam - Problem A
//Author: Sushant Bhatia
#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<cstring>
#define FOR(i,j,k) for(i = j;i < k;i++)
#define RFOR(i,j,k) for(i = k-1;i >= j;i--)
#define LL long long
#define GET(x) scanf("%d",&x)
#define OUT(x) printf("%d\n",x)
#define SET(x) memset(x,0,sizeof(x))
#define S(x) x.size()
bool comp(int i,int j){ return i > j; }
using namespace std;
int main(){
	int t;
	int lpo,lpb,tmvo,tmvb,crps;
	char crmv;
	GET(t);
	int c,i,sz,n;
	FOR(c,1,t+1){
		GET(n);
		lpo = lpb = 1;
		tmvo = tmvb = 0;
		FOR(i,0,n){
			cin>>crmv>>crps;
			if(crmv == 'O'){
				tmvo += abs(crps-lpo)+1;
				tmvo = max(tmvo,tmvb+1);
				lpo = crps;
			}
			else{
				tmvb += abs(crps-lpb) + 1;
				tmvb = max(tmvb,tmvo+1);				
				lpb = crps;
				//tmv += mvb-mvo;
				//mvo = 0;
			}
		//cout<<tmvo<<"  "<<tmvb<<"\n";
		}
	printf("Case #%d: %d\n",c,max(tmvo,tmvb));
	}
	return 0;
}
