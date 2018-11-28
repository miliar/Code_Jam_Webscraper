#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

const int mod = 1000003;

int T,n,m,cnt;
string s[5];
int id[5][5],rec[5][5];

int contain(int opt, int i)
{
	if ( (opt | (1<<i)) == opt ) return 1;
	else return 0;
}

void work(int &x, int &y)
{
	if (x==-1) x = n-1;
	if (x==n) x = 0;
	if (y==-1) y = m-1;
	if (y==m) y = 0;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> n >> m;
		for (int i=0;i<n;i++) cin >> s[i];
		cnt = 0;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) id[i][j] = cnt++;
		int ans = 0;
		for (int opt=0;opt<(1<<cnt);opt++)
		{
			//debug(opt);
			memset(rec,0,sizeof rec);
			for (int i=0;i<n;i++) for (int j=0;j<m;j++)
				if (contain(opt,id[i][j]))
				{
					//printf("i=%d j%d case1\n",i,j);
					if (s[i][j]=='-')
						if (j==0) rec[i][m-1]++;
						else rec[i][j-1]++;
					if (s[i][j]=='|')
						if (i==0) rec[n-1][j]++;
						else rec[i-1][j]++;
					int ii,jj;
					if (s[i][j]=='/')
					{
						ii=i+1;
						jj=j-1;
						work(ii,jj);
						rec[ii][jj]++;
					}
					if (s[i][j]=='\\')
					{
						ii=i-1;
						jj=j-1;
						work(ii,jj);
						rec[ii][jj]++;
					}
				}
				else
				{
					//printf("i=%d j%d case2\n",i,j);
					if (s[i][j]=='-')
						if (j==m-1) rec[i][0]++;
						else rec[i][j+1]++;
					if (s[i][j]=='|')
						if (i==n-1) rec[0][j]++;
						else rec[i+1][j]++;
					int ii,jj;
					if (s[i][j]=='/')
					{
						ii=i-1;
						jj=j+1;
						work(ii,jj);
						rec[ii][jj]++;
					}
					if (s[i][j]=='\\')
					{
						ii=i+1;
						jj=j+1;
						work(ii,jj);
						rec[ii][jj]++;
					}
				}
			int ok = 1;
			//debug(ok);
			for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (rec[i][j]>1) ok = 0;
			if (ok) ans++;
		}
		printf("Case #%d: %d\n",test,ans%mod);
	}
	
	return 0;
}
