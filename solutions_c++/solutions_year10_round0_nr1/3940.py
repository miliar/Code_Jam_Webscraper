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

int n,k;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ts;
	scanf("%d",&ts);
	FR(i,0,ts){
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i+1);
		if(k%(1<<n) == (1<<n)-1)puts("ON");
		else puts("OFF");
	}
	return 0;
}
