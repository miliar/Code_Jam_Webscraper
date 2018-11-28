
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

typedef long long int64;
#define maxn 304
int color[maxn];
pair<int,int> t[maxn];
int cas;
map<string,int> mapa;
int kol=0;
vector<int> kto[maxn];
int n;	
int ile(int a,int b,int c){
	vector<pair<int,int> > tab;
	fup(i,1,n)if(color[i]==a||color[i]==b||color[i]==c){
		tab.PB(MP(t[i].FI,t[i].SE));	
	}
	sort(tab.begin(),tab.end());
	int last=0;
	priority_queue<int> Q;
	int act=0;
	int sum=0;
	while(1){
		if(last>=10000)break;
		while(act<siz(tab)){
			if(tab[act].FI<=last+1){
				Q.push(tab[act].SE);
				act++;
			}else break;
		}
		if(siz(Q)==0)return inf;	
		int z=Q.top();
		Q.pop();	
		last=z;
		sum++;
	}
	return sum;
}
int main(){
	cin>>cas;
	fup(c,1,cas){
		int mini=inf;
		mapa.clear();
		kol=0;
		cin>>n;
		fup(i,1,n){
			string x;cin>>x>>t[i].FI>>t[i].SE;
			int colo=-1;
			if(mapa.find(x)!=mapa.end())colo=mapa[x];
			else {
				mapa[x]=++kol;
				colo=mapa[x];
			}
			color[i]=colo;
		}
		fup(i,0,n)kto[i].clear();
		fup(i,1,n)kto[color[i]].PB(i);

		fup(i,1,kol)fup(j,i,kol)fup(z,j,kol){
			int q=ile(i,j,z);
			if(q<mini)mini=q;
		}
		printf("Case #%d: ",c);
		if(mini==inf)cout<<"IMPOSSIBLE"<<endl;
		else cout<<mini<<endl;
	}	

	return 0;	
}
