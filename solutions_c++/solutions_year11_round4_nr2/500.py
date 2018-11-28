#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 505;

string a[nmax];

int n,m,d;

double FI[nmax][nmax],FJ[nmax][nmax],FA[nmax][nmax];

double sumI[nmax][nmax],sumJ[nmax][nmax],sumA[nmax][nmax];

void preCalc(double f[nmax][nmax],double sum[nmax][nmax])
{
	for (int i = 0;i < n; ++i)
		for (int j = 0;j < m; ++j) 
		{			
			double s1 = 0;
			double s2 = 0;
			double s3 = 0;
			if (i > 0) s1 = sum[i-1][j];
			if (j > 0) s2 = sum[i][j-1];
			if (i > 0 && j > 0) s3 = sum[i-1][j-1];

			sum[i][j] = s1 + s2 - s3 + f[i][j];
		}
}

double getSum(double f[nmax][nmax],double sum[nmax][nmax],int imin,int jmin,int imax,int jmax)
{
	double ans = 0;

	ans += sum[imax][jmax];
	if (jmin > 0) ans -= sum[imax][jmin-1];
	if (imin > 0) ans -= sum[imin-1][jmax];
	if (imin > 0 && jmin > 0) ans += sum[imin-1][jmin-1];

	return ans - f[imin][jmin] - f[imax][jmax] - f[imin][jmax] - f[imax][jmin];
}


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		
		cin >> n >> m >> d;
		for (int i = 0;i < n; ++i)
			 cin >> a[i];

		int ans = -1;

		for (int i = 0;i < n; ++i)
			for (int j = 0;j < m; ++j)
			{
				FI[i][j] = ((double)(a[i][j]-'0'+d)) * ((double) i + 0.5);
				FJ[i][j] = ((double)(a[i][j]-'0'+d)) * ((double) j + 0.5);
				FA[i][j] = ((double)(a[i][j]-'0'+d));
			}
		preCalc(FI,sumI);
		preCalc(FJ,sumJ);
		preCalc(FA,sumA);


		for (int i = 0;i < n; ++i)
			for (int j = 0;j < m; ++j)
			{
				for (int k = 3;; k++)
				{
					if (i + k - 1 >= n || j + k - 1  >= m) break;

					if (k > ans)
					{
						
						

						double cI = (double)i + (double) k / 2;
						double cJ = (double)j + (double) k / 2;

						double I = getSum(FI,sumI,i,j,i+k-1,j+k-1) - getSum(FA,sumA,i,j,i+k-1,j+k-1) * cI;
						double J = getSum(FJ,sumJ,i,j,i+k-1,j+k-1) - getSum(FA,sumA,i,j,i+k-1,j+k-1) * cJ;

						/*for (int ii = i;ii < i + k; ++ii)
							for (int jj = j; jj < j + k; ++jj)
							{
								if (ii == i && jj == j) continue;
								if (ii == i+k-1 && jj == j) continue;
								if (ii == i && jj == j+k-1) continue;
								if (ii == i+k-1 && jj == j+k-1) continue;

								I += ((double) ii + 0.5 - cI) *  ((double)(a[ii][jj]-'0'+d));
								J += ((double) jj + 0.5 - cJ) *  ((double)(a[ii][jj]-'0'+d));
							}*/
						if (I == 0 && J == 0) ans = k;
					}
				}
			}
		
		if ( ans > -1) printf("Case #%i: %i\n",test,ans);		
		else printf("Case #%i: IMPOSSIBLE\n",test);		
	}
	
	return 0;
}