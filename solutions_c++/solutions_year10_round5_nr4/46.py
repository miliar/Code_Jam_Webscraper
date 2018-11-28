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

int n,b;

bool f[10][10];
int ans;

void erebor(int l,int s)
{
	if (s==n){
		ans++;
		return;
	}
	for (int i=l+1;i<=n-s;i++){
		int q=i,j=0;
		bool kpyto=true;
		while (q){
			kpyto&=f[j][q%b];
			j++;q/=b;
		}
		if (kpyto){
			q=i;j=0;
			while (q){
				f[j++][q%b]=false;
				q/=b;
			}
			erebor(i,i+s);
			q=i;j=0;
			while (q){
				f[j++][q%b]=true;
				q/=b;
			}
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		cin >> n >> b;
		ans=0;
		memset(f,true,sizeof(f));
		erebor(0,0);
		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}
