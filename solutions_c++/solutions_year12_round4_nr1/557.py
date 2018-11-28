#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstring>

#include <queue>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T, N;
    fin >> T;
    int D[10001], L[10001], max_next[10001], max_prev[10001];;
    int DIST;
    
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N;
		bool done = false;

		for (int j = 0 ; j < N ; j++)
            fin >> D[j] >> L[j];
		fin >> DIST;
		
		memset(max_next, 0, sizeof(max_next));
		memset(max_prev, 0, sizeof(max_prev));
		max_next[0] = D[0]*2; max_prev[0] = 0;
		for (int j = 0 ; j < N ; j++)
		{
			int k = j+1;
			if (max_next[j] >= DIST) {done = true; break;}

 //fout << k << " : " << max_next[k] << "  " << endl;
			while (k < N)
			{
                //fout << k << " : " << max_next[k] << " - " << D[k] + min(L[k],D[k]-D[max_prev[j]]) << " -- " << D[k] << endl;
				if (max_next[j] < D[k])
				    break;
				if (max_next[k] < D[k] + min(L[k],D[k]-D[max_prev[j]]))
				{
				    max_next[k] = D[k] + min(L[k],D[k]-D[max_prev[j]]);
				    max_prev[k] = k;
					//fout << k << " : " << max_next[k] << " -- " << endl;
				}
				k++;
			}
		}
		fout << "Case #" << i << ": ";
		if (done)
			fout << "YES";
  		else
  			fout << "NO";
		fout << endl;
    }
}
