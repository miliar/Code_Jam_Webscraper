
#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <complex>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define f first
#define s second

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int n;scanf("%d",&n);
		map<int,int> mp;
		for(int i=0;i<n;i++){
			int a,b;scanf("%d%d",&a,&b);
			mp[a]=b;
			//if(npr==11)cout<<a<<"-"<<b<<endl;
		}

		int ans=0;
		while(1){
			map<int,int> mpn;

#if 0
			for(__typeof(mp.begin()) it=mp.begin();it!=mp.end();it++){
				cout<<it->f<<"("<<it->s<<") ";
			}
			cout<<endl;
#endif

			int hit=0;
			for(__typeof(mp.begin()) it=mp.begin();it!=mp.end();it++){
				if(it->s==1)mpn[it->f]+=1;
				if(2<=it->s){
					int cnt=it->s/2;
					ans+=cnt;
					hit=1;
					mpn[it->f-1]+=cnt;
					mpn[it->f+1]+=cnt;
					if(it->s%2)mpn[it->f]+=1;
				}
			}
			if(hit==0)break;
			swap(mpn,mp);
		}

		printf("Case #%d: ",npr);
		printf("%d\n",ans);
	}
	return 0;
}
