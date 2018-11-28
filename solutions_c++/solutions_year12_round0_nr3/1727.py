#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <sstream>
using namespace std;
template <class T> void checkmin(T &t,T x){if (x < t) t = x;}
template <class T> void checkmax(T &t,T x){if (x > t) t = x;}
const int N = 2000005;
int n,m;
int A,B;
long long ans;
bool app[N];

void gao(int x){
	char buf[15];
	sprintf(buf,"%d",x);
	int sz = strlen(buf);
	int cnt = 0;
	for (int i=0;i<sz;i++){
		sscanf(buf,"%d",&x);
		if (x >= A && x <= B && !app[x]) {
			cnt++;
			app[x] = 1;
		}
		char c = buf[0];
		for (int j=0;j+1<sz;j++)
			buf[j] = buf[j+1];
		buf[sz-1] = c;
	}
	ans += 1LL * cnt * (cnt-1) / 2;
}

int main(){
	int Tc;
	cin >> Tc;
	for (int r=1;r<=Tc;r++){
		printf("Case #%d: ",r);
		memset(app,0,sizeof(app));
		cin >> A >> B;
		ans = 0;
		for (int i=A;i<=B;i++)
			if (!app[i]){
				gao(i);
			}
		cout << ans << endl;
	}
}

