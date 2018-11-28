#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


void main()
{
	ifstream ifs("B-small-attempt1.in");
	ofstream ofs("B-small-attempt1.out");

	int T,l,n,c;
	__int64 t;
	int i,j,k;
	ifs>>T;
	for(i=0; i<T; i++)
	{
		ifs>>l>>t>>n>>c;

		vector<__int64> len;

		vector<__int64> tmp(n+1,0);
		vector<vector<__int64> > tm(l+1,tmp);

		for(j=0; j<c; j++)
		{
			int a;
			ifs>>a;
			len.push_back(a);
		}

		for(j=1; j<=n; j++)
			tm[0][j]=tm[0][j-1]+len[(j-1)%c]*2;

		for(k=1; k<=l; k++)
			for(j=1; j<=n; j++)
			{
				__int64 pp;
				if(tm[k-1][j-1]>=t)
					pp=tm[k-1][j-1]+len[(j-1)%c];
				else if(tm[k-1][j-1]+len[(j-1)%c]*2<=t)
					pp=tm[k-1][j-1]+len[(j-1)%c]*2;
				else
				{
					__int64 tt=t-tm[k-1][j-1];
					pp=tm[k-1][j-1]+tt+(len[(j-1)%c]-tt/2);
				}
				tm[k][j]=min(tm[k][j-1]+len[(j-1)%c]*2, pp);
			}

		__int64 sol=tm[0][n];
		for(j=1; j<=l; j++)
			sol=min(sol,tm[j][n]);

		ofs<<"Case #"<<i+1<<": "<<sol<<endl;
	}
} 