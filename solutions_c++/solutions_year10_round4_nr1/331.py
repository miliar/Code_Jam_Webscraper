#include<iostream>
#include<cstdio>

using namespace std;
int v[400][100];
int d[400][100],k;

const int FS = 0x12345678;

inline int linelen(int l,int k)
{
	if (l<k) return l+1;
	l=2*k-l-1;
	return l; 
}

bool test(int n)
{
	for(int i=0;i<2*n-1;i++)
	{
		for(int j=0;j<linelen(i,n);j++)
		{
			int a = 0;
			for(int x=0;x<2*n-1;x++)
				for(int y=0;y<linelen(x,n);y++)
					d[x][y] = FS;

			bool possibleplace = true;
			for(int x=0;x<2*k-1;x++)
			{
				for(int y=0;y<linelen(x,k);y++)
				{
					int nx = i+x;
					if(nx>=2*n-1) { possibleplace = false; break; }
					int ny = j;
					for(int t=i;t<=nx;t++)
						if (t<n)
							if (t-i<k) ;
							else ++ny;
						else
							if (t-i<k) --ny;
							else ;
					ny+=y;

					if (ny<0||ny>=linelen(nx,n)) { possibleplace = false; break; }

					d[nx][ny] = v[x][y];

				}
				if (!possibleplace) break;
			}
			if (!possibleplace) continue;

			bool possible = true;
			for(int x=0;x<2*n-1;x++)
			{
				for(int y=0;y<linelen(x,n);y++)
				{
					if (d[x][y]==FS) continue;
					int o1 = d[x][linelen(x,n)-y-1], o2 = d[2*n-2-x][y];
					if ((o1!=FS&&d[x][y]!=o1)||(o2!=FS&&d[x][y]!=o2))
					{
						possible = false;
						break;
					}
				}
				if (!possible) break;
			}
			if (possible) return true;
		}
	}
	return false;
}

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);

	int t;
	cin>>t;

	for(int tt=1;tt<=t;tt++)
	{
		cin>>k;

		for(int i=0;i<k;i++)
			for(int j=0;j<=i;j++)
				cin>>v[i][j];
		for(int i=0;i<k-1;i++)
			for(int j=0;j<=k-i-2;j++)
				cin>>v[i+k][j];

		int ans = k;
		while(!test(ans)) ++ans;

		printf("Case #%d: %d\n",tt,ans*ans-k*k);
	}

	return 0;
}
