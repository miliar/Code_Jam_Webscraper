//Google Code Jam - Problem B
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
int com[30][30];
int opp[30][30];
char v[105];
int main(){
	int t,c,d,n,k;
	string s;
	int cs,i,j,tmp;
	bool fnd = false;
	GET(t);
	FOR(cs,1,t+1){
		SET(com); SET(opp);
		GET(c);
		FOR(i,0,c){
			cin>>s;
			com[s[0]-'A'][s[1]-'A'] = com[s[1]-'A'][s[0]-'A'] = s[2]-'A'+1;
		}
		GET(d);
		FOR(i,0,d){
			cin>>s;
			opp[s[0]-'A'][s[1]-'A'] = opp[s[1]-'A'][s[0]-'A'] = 1;
		}
		GET(n);
		cin>>s;
		k = 0;
		FOR(i,0,n){
			tmp = com[s[i]-'A'][v[k-1]-'A'];
			fnd = false;
			if(k){
				if(tmp){ 
					v[k-1] = 'A' + tmp-1;
					fnd = true;
				}
				else{
					FOR(j,0,k){
						if(opp[v[j]-'A'][s[i]-'A']){
							k = 0;
							fnd = true;
						}
					}
				}
				if(!fnd) v[k++] = s[i];
			}
			else v[k++] = s[i];
		}
	printf("Case #%d: [",cs);
	FOR(i,0,k-1) printf("%c, ",v[i]);
	if(k) printf("%c",v[i]);
	printf("]\n");
	}
	return 0;
}
