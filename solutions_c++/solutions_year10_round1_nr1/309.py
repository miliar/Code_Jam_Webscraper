#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

inline long Min(long a,long b) {return (a>=b) ? b : a;}

char D[55][55]={0};

bool horLine(char a,int n,int m,int K)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m-K+1;j++)
		{
			bool now=true;
			for(int t=0;t<K;t++)
			{
				if (D[i][j+t]!=a)
				{
					now=false;
					break;
				}
			}
			if (now) return true;
		}
	}
	return false;
}

bool verLine(char a,int n,int m,int K)
{
	for(int j=0;j<m;j++)
	{
		for(int i=0;i<n-K+1;i++)
		{
			bool now=true;
			for(int t=0;t<K;t++)
			{
				if (D[i+t][j]!=a)
				{
					now=false;
					break;
				}
			}
			if (now) return true;
		}
	}
	return false;
}

bool diagLine(char a,int n,int m,int K)
{
	for(int i=0;i<n-K+1;i++)
	{
		for(int j=0;j<m-K+1;j++)
		{
			if (D[i][j]!=a) continue;
			int k=K-1,curx=i,cury=j;
			bool now=true;
			while(k>0)
			{
				curx++; cury++;
				if (curx>=0&&curx<n&&cury>=0&&cury<m) k--;
				else break;
				if (D[curx][cury]!=a)
				{
					now=false;
					break;
				}
			}
			if (k==0&&now) return true;
		}
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if (D[i][j]!=a) continue;
			int k=K-1,curx=i,cury=j;
			bool now=true;
			while(k>0)
			{
				curx++; cury--;
				if (curx>=0&&curx<n&&cury>=0&&cury<m) k--;
				else break;
				if (D[curx][cury]!=a)
				{
					now=false;
					break;
				}
			}
			if (k==0&&now) return true;
		}
	}
	return false;
}

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int T=0;
	dat >> T;
	for(int t=0;t<T;t++)
	{
		if (t==74)
		{
			int r=45;
		}
		int n,k,m;
		dat >> n >> k;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<55;j++)
				D[i][j]='\0';
			//memset(D[i],0,sizeof(D[i]));
			dat >> D[i];
		}
		m=strlen(D[0]);
		for(int i=0;i<n;i++)
		{
			int curp=m-1;
			for(int j=m-1;j>=0;j--)
				if (D[i][j]!='.')
				{
					if (j==curp)
					{
						curp--;
						continue;
					}
					D[i][curp]=D[i][j];
					D[i][j]='.';
					curp--;
				}
//			sol << D[i] << endl;
		}
		bool v1=horLine('B',n,m,k)||verLine('B',n,m,k)||diagLine('B',n,m,k),
			v2=horLine('R',n,m,k)||verLine('R',n,m,k)||diagLine('R',n,m,k);
		//sol << horLine('B',n,m,k) << endl << verLine('B',n,m,k) << endl << diagLine('B',n,m,k) << endl;
		//sol << horLine('R',n,m,k) << endl << verLine('R',n,m,k) << endl << diagLine('R',n,m,k) << endl << endl;
		sol << "Case #" << t+1 << ": ";
		if (v1&&v2)
		{
			sol << "Both\n";
			continue;
		}
		if (v1)
		{
			sol << "Blue\n";
			continue;
		}
		if (v2)
		{
			sol << "Red\n";
			continue;
		}
		sol << "Neither\n";
	}
	return 0;
}

/*#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

inline long Min(long a,long b) {return (a>=b) ? b : a;}

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int T=0;
	dat >> T;
	for(int t=0;t<T;t++)
	{
		long D,I,M,N;
		dat >> D >> I >> M >> N;
		vector <int> nums(N,0);
		for(int i=0;i<N;i++)
			dat >> nums[i];
		long F[102][258]={0},ans=1000000000;
		for(int i=1;i<=N;i++)
		{
			for(int j=0;j<=255;j++)
			{
				int v1=1000000000,v2=1000000000,v3=1000000000;
				v1=D+F[i-1][j];
				for(int r=0;r<=255;r++)
				{
					if (abs(j-r)<=M) v2=Min(v2,(F[i-1][r]+abs(nums[i-1]-j)));
					if (M!=0)
					{
						long f=abs(nums[i-1]-r)/M;
						if (abs(nums[i-1]-r)%M==0) f--;
						if (f>0) v3=Min(v3,(I*f+F[i-1][r]));
					}
				}
				F[i][j]=Min(v1,v2);
				if (j==nums[i-1]) F[i][j]=Min(F[i][j],v3);
				if (i==N) ans=Min(ans,F[i][j]);
				//sol << F[i][j] << "	";
			}
			//sol << endl;
		}
		sol << "Case #" << t+1 << ": " << ans << endl;
		//sol << endl;
	}
	return 0;
}*/
