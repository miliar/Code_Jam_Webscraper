#include <fstream>
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
//		for(int i=0;i<=255;i++)
//			sol << i << "	";
//		sol << endl;
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
						long f=abs(j-r)/M;
						if (abs(j-r)%M==0) f--;
						if (f>=0) v3=Min(v3,(I*f+F[i-1][r]+abs(nums[i-1]-j)));
					}
				}
				F[i][j]=Min(v1,v2);
				F[i][j]=Min(F[i][j],v3);
				if (i==N) ans=Min(ans,F[i][j]);
//				sol << F[i][j] << "	";
			}
//			sol << endl;
		}
		ans=min(ans,D*N);
		sol << "Case #" << t+1 << ": " << ans << endl;
		//sol << endl;
	}
	return 0;
}
