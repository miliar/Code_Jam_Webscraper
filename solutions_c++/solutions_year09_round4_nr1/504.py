#include <cstdio>
#include <cmath>
#include <cassert>
#include <iostream>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define inf 0x3f3f3f3f
#define Eo(x) { cerr << #x << " = " << x << endl;}
string a[300];
int n,ferlon;
int was[300],num[300];
inline  bool zero(string &w, int b){
	for ( int i = b; i < w.length(); i++)
		if (w[i] == '1') return false;
	return true;
}
int main(){
//	assert(freopen("input.txt","r",stdin));
	scanf("%d",&ferlon);
	for (int _ = 0; _ < ferlon; _++){
		int ans = 0;
		scanf("%d\n",&n);
		memset(was,0,sizeof(was));
		char buff[256];
		for ( int i = 0; i < n; i++){
			scanf("%s",buff);
			a[i] = buff;
		}
		for ( int i = 0; i < n; i++){
			int j = 0;
			for (; j < n; j++)
				if (!was[j] && zero(a[j],i + 1)){
					was[j] = 1;
					num[i] = j;
					break;
				}
				assert( j != n);
		}
		for ( int i = 0; i < n; i++)
			for ( int j = i + 1 ; j < n; j++)
				if ( num[j] < num[i]) ans ++;
		cout << "Case #"<<(_+1) << ": " << ans << endl;
	}
	return 0;
}

