#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	//ifstream fin("A-small-attempt2.in");
	//ofstream fout("A-small-attempt2.out");
	ifstream fin("A-large.in");
    ofstream fout("A-large.out");
	
    int T, X, S, R, N, time;
	int B[1010], E[1010], w[1010];
	double length[101];
    fin >> T;
	
    for (int i = 1 ; i <= T ; i++)
    {
		double ans = 0;
        fin>> X >> S >> R >> time >> N;
		for (int j = 1 ; j <= N ; j++)
			fin >> B[j] >> E[j] >> w[j];
		E[0] = 0; B[N+1] = X;
		
		for (int j = 0 ; j <= 100 ; j++) length[j] = 0;
		
		for (int j = 1 ; j <= N+1 ; j++)
		{
			length[0] += B[j]-E[j-1];
			if (j == N+1) continue;
			length[w[j]] += E[j]-B[j];
		}
		
		double run_left = (double)time;
		for (int j = 0 ; j <= 100 ; j++)
		{
			if (length[j] == 0) continue;          
			if (run_left == 0) ans += (double)length[j]/(double)(j+S);
			else 
			{
				double temp = (double)length[j]/(double)(j+R);
				if (temp <= run_left) 
				{
					run_left -= temp;
					ans += temp;
				}
				else 
				{
					ans += run_left;
					length[j] -= run_left*(j+R);
					ans += (double)length[j]/(double)(j+S);
					run_left = 0;
				}
			}
		}
		fout.precision(6);
  	    fout.setf(ios::fixed);
		fout << "Case #" << i << ": " << ans << endl;
    }
       
}
