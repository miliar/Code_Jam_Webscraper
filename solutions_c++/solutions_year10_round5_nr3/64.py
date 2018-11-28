#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

map <int,int> a;

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		a.clear();
		int n;
		cin >> n;
		for (int i=0;i<n;i++){
			int v,x;
			cin >> x >> v;
			a[x]=v;
		}
		int ans=0;
		while (1){
			bool kpyto=true;
			for (map <int,int>:: iterator i=a.begin();i!=a.end();i++){
				if (i->second>1){
					kpyto=false;
					i->second-=2;
					a[i->first-1]+=1;
					a[i->first+1]+=1;
					ans++;
					break;
				}
			}
			if (kpyto)break;
		}
		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}
