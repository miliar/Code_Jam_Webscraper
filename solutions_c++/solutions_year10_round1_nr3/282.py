#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define SZ(x) ((int)(x).size())
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define MS(a,b) memset((a),b,sizeof(a))
#define EC(tp,it,a) for(tp::iterator it=(a).begin();it!=(a).end();++it)
#define SE(x) cout<<#x<<" = "<<x<<endl
#define PB push_back

template<class T> void inc(T& a, const T& b) {
	if (a < b) a = b;
}
template<class T> void dec(T& a, const T& b) {
	if (a > b) a = b;
}

int a1,a2,b1,b2;
map<pair<int,int>,int> table;

int find(int x,int y){
//	printf("%d %d\n",x,y);
//	system("pause");

	if(x==y)return 0;
	

	if(x>y)swap(x,y);
	if(y%x==0)return 1;

	if(table.find(make_pair(x,y))!=table.end()){
		return table[make_pair(x,y)];
	}
	
	for(int i=y-x; i>0; i-=x){
		//printf("go %d %d\n",i,y);
		if(find(x,i)==0){
			table[make_pair(x,y)]=1;
			return 1;
		}
	}
	table[make_pair(x,y)]=0;
	return 0;
}

int run(){
	int rez=0;
	for(int i=a1;i<=a2;++i){
		for(int j=b1;j<=b2;++j){
			if(find(i,j)==1)++rez;
		}
	}
	return rez;
}

int main() {
	freopen("c1.in","r",stdin);
	freopen("c1.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	FR(cas,0,ts){
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		printf("Case #%d: %d\n",cas+1,run());
	}
	return 0;
}
