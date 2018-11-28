#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define N 1000009
#define M 120
#define ll long long
#define inf 1<<30
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-8
#define pii pair<int,int>
#define pdd pair<double,double>
#define It map<unsigned,string>::iterator
#define MP(i,j) make_pair(i,j)
#define PB push_back
#define VI vector<int>
#define lchild(id) (id<<1)
#define rchild(id) ((id<<1)|1)
#define base 2048

int n;
pii p[N];

string gao(int i){
	string res;
	while(i){
		res.insert(res.begin(),i%10+'0');
		i/=10;
	}
	return res;
}
void init(){
	n=0;
	for(int i=1;i<=1000;i++){
		string a=gao(i);
		int len=a.length();
		for(int j=1;j<len;j++){
			string b=a.substr(0,j);
			string c=a.substr(j);
			c+=b;
			if(c[0]=='0')
				continue;
			int t=atoi(c.c_str());
			if(i<t)
				p[n++]=MP(i,t);
			else if(t<i)
				p[n++]=MP(t,i);
		}
	}
	sort(p,p+n);
	n=unique(p,p+n)-p;
	//cout<<n<<endl;
}

bool check(int a,int b,int c){
	return a>=b && a<=c;
}
int main() {
#ifndef	ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	init();
	int cas,pcas=1;
	int A,B;
	scanf("%d\n",&cas);
	while(cas--){
		printf("Case #%d: ",pcas++);
		scanf("%d%d",&A,&B);
		
		int ans=0;
		for(int i=0;i<n;i++)
			if(check(p[i].first,A,B) && check(p[i].second,A,B)){
				//cout<<p[i].first<<" "<<p[i].second<<endl;
				ans++;
			}
		printf("%d\n",ans);
	}
	return 0;
}