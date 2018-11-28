#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define M 1100

int n,m,C;
int data[M][M];
void read_data()
{
	cin >> n >> m >> C;
	int i,j;
	char ch;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
		{
			cin >> ch;
			data[i][j] = ch - '0';
		}
}

void update(int a,int &s)
{
	if (s < a) s = a;
}
int work_ans()
{
	int i,j,k,l,p;
	int temp1,temp2;
	int ans = -1;
	for (i=2;i<n;i++)
		for (j=2;j<m;j++)
		{
			for (p=1;;p++)
			{
				if (i - p < 1 || i + p > n || j - p < 1 || j + p > m) break;
				temp1 = temp2 = 0;
				for (k=i-p;k<=i+p;k++)
					for (l=j-p;l<=j+p;l++)
					{
						if ((k == i - p || k == i + p) && (l == j - p || l == j + p)) continue;
						temp1 += (k - i) * data[k][l];
						temp2 += (l - j) * data[k][l];
					}
				if (temp1 == 0 && temp2 == 0) update(p * 2 + 1,ans);
			}
		}

	for (i=3;i<n;i++)
		for (j=3;j<m;j++)
		{
			for (p=2;;p++)
			{
				if (i-p < 1 || i + p - 1 > n || j - p < 1 || j + p - 1 > m) break;
				temp1 = temp2 = 0;
				for (k=i-p;k<=i+p-1;k++)
					for (l=j-p;l<=j+p-1;l++)
					{
						if ((k == i - p || k == i + p-1) && (l == j - p || l == j + p-1)) continue;
						temp1 += ((k - i)*2 + 1) * data[k][l];
						temp2 += ((l - j)*2 + 1) * data[k][l];
					}
				if (temp1 == 0 && temp2 == 0) update(p * 2,ans);
			}
		}
	return ans;
}
int main()
{
	int ans,t,i;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small.out","w",stdout);
	cin >> t;
	for (i=1;i<=t;i++)
	{
	read_data();
	ans = work_ans();
	printf("Case #%d: ",i);
	if (ans > 0) printf("%d\n",ans); else printf("IMPOSSIBLE\n");
	}
	return 0;
}