
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

int cas;
int eval(string x){
//	debug(x);
	int val=60*10*(x[0]-'0')+60*(x[1]-'0')+(x[3]-'0')*10+(x[4]-'0');
//	cout<<val<<endl;
	return val;
}
vector<pair<int,int> > t[2];
int T;
void go(int s,int czas){
	if(siz(t[s])==0)return ;
	fup(i,0,siz(t[s])-1){
			if(t[s][i].first>=czas){
				int x=t[s][i].second+T;
				t[s].erase(t[s].begin()+i);
				go(!s,x);
				break;
			}
	}
}
int main(){
	scanf("%d",&cas);
	fup(ca,1,cas){
		t[0].clear();
		t[1].clear();
		int ab,ba;
		scanf("%d",&T);
		scanf("%d%d",&ab,&ba);
		fup(i,1,ab){
			string s,e;
			cin>>s>>e;
			int ss,ee;
			ss=eval(s);ee=eval(e);
		//	debug(ss);debug(ee);
			t[0].push_back(MP(ss,ee));
		}
		fup(i,1,ba){
			string s,e;
			cin>>s>>e;
			int ss,ee;
			ss=eval(s);ee=eval(e);
			t[1].push_back(MP(ss,ee));
		}
		sort(t[0].begin(),t[0].end());
		sort(t[1].begin(),t[1].end());		
		int suma=0,sumb=0;
		while(siz(t[0])>0||siz(t[1])>0){
			if(siz(t[0])==0){sumb++;go(1,-1);continue;}
			if(siz(t[1])==0){suma++;go(0,-1);continue;}
			if(t[0][0].first<t[1][0].first){suma++;go(0,-1);continue;}
			else{sumb++;go(1,-1);continue;}

		}
		//debug(suma);debug(sumb);
		//cout<<suma<<" "<<sumb<<endl;
		printf("Case #%d: %d %d\n",ca,suma,sumb);


	}
	return 0;	
}
