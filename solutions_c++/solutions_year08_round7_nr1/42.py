#include<iostream>
#include <cmath>
#include <cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include <functional>
#include<utility>
using namespace std;

#define _abs(x)		(((x)>0)?(x):-(x))
#define _max(x,y)	(((x)>(y))?(x):(y))
#define _min(x,y)	(((x)<(y))?(x):(y))

#define EPS 1e-10
#define INF 1000000000

#define S(x)	((x)*(x))
#define Z(x)	(_abs(x) < EPS)
#define N(x)	(x < 0 && !Z(x))
#define P(x)	(x > 0 && !Z(x))
#define ZN(x)	(x < 0 || Z(x))
#define ZP(x)	(x > 0 || Z(x))

#define E(x,y)	(Z((x)-(y)))

#define D2(a,b)	(S(a.x-b.x) + S(a.y-b.y))
#define D1(a,b)	(sqrt(D2(a,b)))

#define T2(a,b,c)	((a.x*b.y+b.x*c.y+c.x*a.y) - (a.y*b.x+b.y*c.x+c.y*a.x))

typedef pair<int,int> PII;

#define ALL(x)  x.begin(),x.end()
#define PB push_back
#define FT first
#define SD second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
#define MP make_pair
typedef vector<int> VI;

//PII operator+(PII a, PII b){ return MP(a.FT+b.FT,a.SD+b.SD); }
//PDD operator+(PDD a, PDD b){ return MP(a.FT+b.FT,a.SD+b.SD); }

//typedef __int64 LL;

/*struct Point{
	int x,y;
	void scan(){
		scanf("%d%d",&x,&y);
	}
	Point(int _x=0,int _y=0){
		x=_x;
		y=_y;
	}
};*/


map<string,int> m;

#define MAX 1002

struct Item{
	string name;
	vector<int> ch;
} items[MAX];
int nc=0;
string names[MAX],name;
vector<string> ch[MAX];

int recur(int id){
	if (ch[id].size()==0) return 1;
	int i,j,k,mx=0;
	vector<int> v;
	for (i=0; i<ch[id].size(); i++){
		v.push_back(recur(m[ch[id][i]]));
	}
	sort(v.begin(),v.end(),greater<int>());
	for (i=0; i<ch[id].size(); i++){
		if (i+v[i]>mx) mx=i+v[i];
	}
	if (mx>ch[id].size()) return mx;
	return mx+1;
}
		

int main(){
	int t,n,mi,i,j,k;	
	cin>>t;
	for (int u=1; u<=t; u++){
		cin>>n;
		m.clear();
		for (i=1; i<=n; i++){
			cin>>names[i];
			//int id=
			m[names[i]]=i;
			cin>>mi;
			ch[i].clear();
			for (j=0; j<mi; j++){
				cin>>name;
				if (name[0]<'a') ch[i].push_back(name);
			}
		}
		cout<<"Case #"<<u<<": "<<recur(1)<<endl;
	}
	return 0;
}



