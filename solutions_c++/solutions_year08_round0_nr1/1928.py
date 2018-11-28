
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<string>
#include<stack>
#include<sstream>
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FOREACH(it,(x)) cerr << *it << ","; cerr << "\n"; 
#define fup(i,a,b) for(int i=a;i<=b;i++)
#define fdo(i,a,b) for(int i=a;i>=b;i--)
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) (int)a.size()
#define inf 1000000000
#define SQR(a) ((a)*(a))
using namespace std;
#define maxn 1005
typedef long long int64;

string name[maxn];
string query[maxn];
int best[maxn];
int nbest[maxn];
int main(){
	int cas;
	scanf("%d",&cas);
	fup(ca,1,cas){	
		int s,q;
		scanf("%d",&s);
		char c;scanf("%c",&c);
		fup(i,1,s)getline(cin,name[i]);
		scanf("%d",&q);
		scanf("%c",&c);

		fup(i,1,q)getline(cin,query[i]);
		fup(i,1,s)best[i]=0;
		fup(i,1,q){
			int mi=inf;
			fup(j,1,s)mi=mini(mi,best[j]);			
			fup(j,1,s){
				nbest[j]=inf;
				if(query[i]!=name[j]){
					nbest[j]=best[j];
					nbest[j]=mini(nbest[j],mi+1);
				}else nbest[j]=inf;
			
			}
			fup(j,1,s)best[j]=nbest[j];
		}
		int mini=inf;fup(j,1,s)mini=mini(mini,best[j]);
		printf("Case #%d: %d\n",ca,mini);
	}

	return 0;	
}
