#include <cstdio>
#include <ctime>
#include <cstring>
#include <assert.h>
#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct rabit{
	int x,v;
	bool operator <(const rabit&b)const{
		return x>b.x;
	}
};

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int C,n,k,b,t;
	rabit r[50];
	bool able[50];
	cin>>C;
	for(int c=1;c<=C;++c){
		cin>>n>>k>>b>>t;
		for(int i=0;i<n;++i)
			cin>>r[i].x;
		for(int i=0;i<n;++i)
			cin>>r[i].v;
		sort(r,r+n);
		memset(able,0,sizeof able);
		int count=0;
		int num=0;
		for(int i=0;i<n&&num<k;++i){
			if(r[i].x + r[i].v*t >= b){
				able[i] = true;
				++num;
				for(int j=0;j<i;++j){
					if(!able[j]) ++count;
				}
			}
		}
		if(num <k)printf("Case #%d: IMPOSSIBLE\n",c);
		else
			printf("Case #%d: %d\n",c,count);
	}
	return 0;
}