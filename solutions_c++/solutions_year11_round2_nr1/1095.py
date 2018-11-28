#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <math.h>
#include <ctype.h>

#define rep(i,n) for(int i=0;i<n;i++)
#define fori(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define ma(a,b) (a>b?a:b)
#define mi(a,b) (a<b?a:b)
#define foreach(it,arr) for(__typeof((arr).begin())it=(arr).begin();it!=(arr).end();it++)
#define foreachd(it,arr) for(__typeof((arr).begin())it=(arr).rbegin();it!=(arr).rend();it++)

typedef long long LL;

using namespace std;

int tc,n;
int ar[200][200];
float owp[1000];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tc);
	fori(t,1,tc){
		scanf("%d", &n);
		rep(i,n){
			char c;
			scanf("%c", &c);
			rep(j,n){
				char ch;
				scanf("%c",&ch);
				ar[i][j] = (ch == '1' ? 1 : (ch == '.' ? -1 : 0));
			}
		}
		
		rep(i,n){
			float sum = 0;
			int jum = 0;
			rep(j,n){
				int cnt = 0;
				int tot = 0;
				if(ar[i][j] > -1) jum++;
				else continue;
				rep(k,n){
					if(k==i) continue;
					if(ar[j][k] == 1) cnt++;
					if(ar[j][k] > -1) tot++;
				}
				sum += cnt*1.0/tot;
			}
			owp[i] = sum / jum;

		}
		printf("Case #%d:\n",t);
		rep(i,n){
			float ans = 0;
			int jum = 0;
			float wp = 0;
			rep(j,n){
				if(ar[i][j]>-1){
					jum++;
					ans+=owp[j];
					wp+=ar[i][j];
				}
			}
			ans=ans/jum;
			wp = wp*1.0 / jum;
			float ret = 0.25 * wp + 0.5 * owp[i] + 0.25 * ans;
			printf("%f\n", ret);
		}
	}
    return 0;
}
