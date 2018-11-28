#include <iostream>
#include <cstdio>

using namespace std;
const int MXN = 510;
//int x[MXN][MXN][MXN];
//int y[MXN][MXN][MXN];
int s[MXN][MXN];
int a[MXN][MXN];
int sl[MXN][MXN];
int sr[MXN][MXN];
int su[MXN][MXN];
int sd[MXN][MXN];
int sum[MXN][MXN];
int n, m;
char buf[1010];
int Sum(int s2[MXN][MXN], int x1, int y1, int x2, int y2, int d)
{
	//cout<<"sum "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<' '<<d<<endl;
	int ret = s2[x2][y2] - s2[x1 - 1][y2] - s2[x2][y1 - 1] + s2[x1 - 1][y1 - 1];
	int sum = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1];
	//cout<<"ret= "<<ret<<" "<< "sum= "<<sum<<" "<<s2[x2][y2]<<endl;
	return ret - sum * d;
	
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int _t = 1; _t <= T; ++_t) {
		//memset(x,0,sizeof(x));
		//memset(y,0,sizeof(y));
		memset(s, 0, sizeof(s));
		memset(sl, 0, sizeof(sl));
		memset(sr, 0, sizeof(sr));
		memset(sd, 0, sizeof(su));
		memset(su, 0, sizeof(sd));
		memset(sum, 0, sizeof(sum));
		
		int d;
		int i, j;
		scanf("%d%d%d\n",&n,&m,&d);
		for (int i = 0; i < n; ++i) {
			gets(buf);
			for (int j = 0; j < m; ++j) s[i+1][j+1] = buf[j] - '0';
		}
		for (i = 1; i <= n; ++i)
			for (j = 1; j <= m; ++j) {
				a[i][j] = s[i][j];
				sl[i][j] = s[i][j] * (m-j+1);
				sr[i][j] = s[i][j] * j;
				su[i][j] = s[i][j] * (n-i+1);
				sd[i][j] = s[i][j] * i;
			}
		for (int i = 1; i <= n; ++i) {
			for (j = 1; j <= m; ++j) {
				//sum[i][j] = sum[i][j - 1] + s[i][j];
				s[i][j] += s[i][j-1];
				sl[i][j] += sl[i][j-1];
				sr[i][j] += sr[i][j-1];
				su[i][j] += su[i][j-1];
				sd[i][j] += sd[i][j-1];
			}
			for (j = 1; j <= m; ++j) {
				s[i][j] += s[i-1][j];
				sl[i][j] += sl[i-1][j];
				sr[i][j] += sr[i-1][j];
				su[i][j] += su[i-1][j];
				sd[i][j] += sd[i-1][j];
			}
			//for (j = 1; j <= m; ++j) sum[i][j] += sum[i-1][j];
		}

		//cout<<"query"<<Sum(sr,3,5,5,6,5)<<endl;
		int ans = 2;
		for (i = 1; i <= n; ++i)
			for (j = 1; j <= m; ++j) {
				for (int k = ans + 1;; k += 1) {
					if (k % 2 == 1) {//奇数，中心在格子上 
						int d = k / 2;
						//continue;
						if (j - d  < 1 || j + d > m || i - d < 1 || i + d > n) break;
						//左
						//Sum(sl,i-d,j-d,i+d,j-1,m-j+1);
						//(a[i-d][j-d]+a[i+d][j-d])*d
						//右
						//Sum(sr,i-d,j+1,i+d,j+d,j);
						//(a[i-d][j+d]+a[i+d][j+d])*d
						int tmp = Sum(sl,i-d,j-d,i+d,j-1,m-j+1);
						//cout<<i<<' '<<j<<' '<<k<<' '<<tmp<<endl;
						tmp  -= Sum(sr,i-d,j+1,i+d,j+d,j);
						tmp -= (a[i-d][j-d]+a[i+d][j-d])*d - (a[i-d][j+d]+a[i+d][j+d])*d;
						//if (tmp == 0) cout << i << " " << j << " " << k << std::endl;
						if (tmp != 0) continue;
						
						tmp = Sum(su, i-d,j-d,i-1,j+d,n-i+1);
						tmp-=Sum(sd,i+1,j-d,i+d,j+d,i);
						tmp-=(a[i-d][j-d]+a[i-d][j+d])*d-(a[i+d][j-d]+a[i+d][j+d])*d;
						if (tmp!=0) continue;
						//cout<<i<<' '<<j<<' '<<k<<' '<<tmp<<endl;
						ans=k;
					} else {//偶数，中心在中间 
						int d = k / 2;
						if (i-d<1 || i+d-1>n || j-d<1 || j+d-1>m) break;
						int tmp = Sum(sl, i-d,j-d,i+d-1,j-1,m-j+1);
						int t1 = tmp;
						tmp-=Sum(sr,i-d,j,i+d-1,j+d-1,j-1);
						//cout<<"after "<<tmp<<endl;
						tmp-=(a[i-d][j-d]+a[i+d-1][j-d])*d-(a[i-d][j+d-1]+a[i+d-1][j+d-1])*d;
						if (tmp!=0) continue;
						//cout<<"oh"<<i<<" "<<j<<' '<<k<<' '<<tmp<<' ' <<t1<<endl;
						tmp=Sum(su,i-d,j-d,i-1,j+d-1,n-i+1);
						tmp-=Sum(sd,i,j-d,i+d-1,j+d-1,i-1);
						tmp-=(a[i-d][j-d]+a[i-d][j+d-1])*d-(a[i+d-1][j-d]+a[i+d-1][j+d-1])*d;
						if (tmp!=0) continue;
						ans=k;
					}
					
				}
			}
		if (ans<3)
			printf("Case #%d: IMPOSSIBLE\n", _t);
		else printf("Case #%d: %d\n", _t, ans);
	}
}
