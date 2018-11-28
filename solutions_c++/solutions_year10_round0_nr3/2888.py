#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

#define LL long long 
LL n,k,r;
LL a[1111];
LL len[1111],val[1111];

void work(){
	cin >> r >> k >> n;
	for (int i=0;i<n;i++) cin >> a[i];
	LL rt=0,pos=0;
	memset(len,0,sizeof(len));
	memset(val,0,sizeof(val));
	
	LL cir=0,ans=0,f=0;
	while (rt<r){
		//cout << rt <<"__"<< ans <<endl;
		LL cur=0,prev_pos=pos;
		while (cur+a[pos]<=k) {
			cur+=a[pos];ans+=a[pos];
			if ((pos+1)%n==prev_pos) break;
			pos=(pos+1)%n; 
		}
		//cout << ans <<" " << cur <<endl;
		rt++;
		/*if (len[pos]>0&&!f){
			LL cir=rt-len[pos],cval=ans-val[pos];
			k-=rt;
			ans=ans+(k/cir)*cval;
			k%=cir;
			f=1;
		}
		val[pos]=ans;
		len[pos]=rt;*/
	}
	cout << ans <<endl;
}

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;cin >>t;
	int num=0;
	while (t--) {
		cout <<"Case #" << ++num<<": ";
		work();
	}
	return 0;
}
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
