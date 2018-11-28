#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
template <class T> void checkmin(T &t,T x){if (x < t) t = x;}
template <class T> void checkmax(T &t,T x){if (x > t) t = x;}
const int N = 105;
int Tc;
int n,s,p;
int a[N];
bool not_sur[31];
bool can_cha[31];

int main(){
	memset(not_sur,0,sizeof(not_sur));
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&Tc);
	for (int r=1;r<=Tc;r++){
		memset(not_sur,0,sizeof(not_sur));
		memset(can_cha,0,sizeof(can_cha));
		printf("Case #%d: ",r);
		scanf("%d%d%d",&n,&s,&p);
		for (int i=0;i<n;i++) scanf("%d",&a[i]);

		for (int i=0;i<=10;i++)
			for (int j=0;j<=10;j++)
				for (int k=0;k<=10;k++) {
					if ( (i >= p || j >= p || k >= p ) && abs(i-j)<=1 && abs(i-k)<=1 && abs(j-k)<=1 ){
						not_sur[i+j+k] = 1;
					}
					if ( (i >= p || j >= p || k >= p ) && abs(i-j)<=2 && abs(i-k)<=2 && abs(j-k)<=2 ){
						can_cha[i+j+k] = 1;
					}
				}
		int cnt = 0;
		int cnt2 = 0;
		for (int i=0;i<n;i++)
			if (not_sur[a[i]]) {
				cnt++;
			} else if (can_cha[a[i]]) {
				cnt2++;
			}
		int ans = cnt + min( cnt2 , s );
		printf("%d\n",ans);
	}
}

