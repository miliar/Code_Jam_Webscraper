#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

struct Point{
	double X, Y;
};

struct Pair{
	int R, K;
};

double dist (Point A, Point B)
{
	return sqrt( (A.X - B.X)*(A.X-B.X) + (A.Y-B.Y)*(A.Y-B.Y) );
}

bool cmp(Pair A, Pair B)
{
	return A.R > B.R;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T, N, W, L;
    fin >> T;
    int R[1001];
    Pair RK[1001];
    Point ans[1001];
    Point trueans[1001];
    bool assign[1001];
    
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N >> W >> L;

		for (int j = 0 ; j < N ; j++)
		{fin >> R[j]; RK[j].R = R[j]; RK[j].K = j;};
		sort(RK, RK+N,cmp);
            
        fout.unsetf(ios::floatfield);
		fout.precision(10);

		ans[0].X = 0; ans[0].Y = 0; int prev = 0;
		for (int j = 1 ; j < N ; j++)
		{
			if (ans[j-1].X + (RK[j].R+RK[j-1].R) <= W)
			{
				ans[j].X = ans[j-1].X + (RK[j].R+RK[j-1].R);
				ans[j].Y = ans[j-1].Y;
			}
			else
			{
				while (true)
				{
					if (ans[prev].Y + (RK[j].R+RK[prev].R) <= L)
					{
	                    ans[j].X = ans[prev].X;
						ans[j].Y = ans[prev].Y + (RK[j].R+RK[prev].R);
						prev = j;
						break;
						
					}
					prev++;
				}
			}
		}
		

		fout << "Case #" << i << ":";
		for (int j = 0 ; j < N ; j++)
		    for (int k = 0 ; k < N ; k++)
		        if (RK[k].K == j)
		    		{
						fout << " " << ans[k].X << " " << ans[k].Y;
						trueans[j].X = ans[k].X;
						trueans[j].Y = ans[k].Y;
		    			break;
		    		}
		    		
		fout << endl;
		
    }
}
