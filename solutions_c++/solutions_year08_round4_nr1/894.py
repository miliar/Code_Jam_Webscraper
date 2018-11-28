#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int N;
	fin  >> N;
	int rec[10000];
	bool flag[10000];
	int dp1[10000];
	int dp0[10000];
	for(int ii = 0; ii < N; ii++)
	{
		fout << "Case #" << ii+1 << ": ";
		int M,V;
		fin >> M >> V;
		memset(rec,0, 10000*sizeof(int));
		memset(flag,0, 10000*sizeof(bool));
		memset(dp1,0, 10000*sizeof(int));
		memset(dp0,0, 10000*sizeof(int));
		for(int i = 0; i < (M-1)/2 ; i++)
			fin >> rec[i] >> flag[i];
		for(int i = (M-1)/2 ; i < M; i++)
			fin >> rec[i];
		for(int i = M-1; i >= 0; i--)
		{
			if(i >= (M-1)/2)
			{
				if(rec[i] == 1)
				{
					dp1[i] = 0;
					dp0[i] = -1;
				}
				else
				{
					dp1[i] = -1;
					dp0[i] = 0;
				}
			}
			else
			{
				int dpand0,dpand1,dpor0,dpor1;
				if(dp1[2*i+1] != -1 && dp1[2*i+2] != -1)
				{
					dpand1 = dp1[2*i+1] + dp1[2*i+2];
				}
				else
				{
					dpand1 = -1;
				}
				if(dp0[2*i+1] != -1 && dp0[2*i+2] != -1)
					dpand0 = dp0[2*i+1]<dp0[2*i+2]?dp0[2*i+1]:dp0[2*i+2];
				else
				{
					if(dp0[2*i+1] == -1)
						dpand0 = dp0[2*i+2];
					else
						dpand0 = dp0[2*i+1];
				}

				if(dp0[2*i+1] != -1 && dp0[2*i+2] != -1)
				{
					dpor0 = dp0[2*i+1] + dp0[2*i+2];
				}
				else
				{
					dpor0 = -1;
				}
				if(dp1[2*i+1] != -1 && dp1[2*i+2] != -1)
					dpor1 = dp1[2*i+1]<dp1[2*i+2]?dp1[2*i+1]:dp1[2*i+2];
				else
				{
					if(dp1[2*i+1] == -1)
						dpor1 = dp1[2*i+2];
					else
						dpor1 = dp1[2*i+1];
				}
		
				if(rec[i] == 1)
				{
					dp1[i] = dpand1;
					dp0[i] = dpand0;
				}
				else
				{
					dp1[i] = dpor1;
					dp0[i] = dpor0;
				}
				
				if(flag[i] == 1)
				{
					if(rec[i] == 1)
					{
						if(dpor1 != -1)
						{
							if(dp1[i] == -1)
								dp1[i] = dpor1 + 1;
							else
								dp1[i] = (dpor1+1)<dp1[i]?(dpor1+1):dp1[i];
						}
						if(dpor0 != -1)
						{
							if(dp0[i] == -1)
								dp0[i] = dpor0 + 1;
							else
								dp0[i] = (dpor0+1)<dp0[i]?(dpor0+1):dp0[i];
						}
						
					}
					else
					{
						if(dpand1 != -1)
						{
							if(dp1[i] == -1)
								dp1[i] = dpand1 + 1;
							else
								dp1[i] = (dpand1+1)<dp1[i]?(dpand1+1):dp1[i];
						}
						if(dpand0 != -1)
						{
							if(dp0[i] == -1)
								dp0[i] = dpand0 + 1;
							else
								dp0[i] = (dpand0+1)<dp0[i]?(dpand0+1):dp0[i];
						}
					}
				}
			}
		}
		if(V == 0 && dp0[0] != -1)
			fout << dp0[0] <<endl;
		else if(V == 1 && dp1[0] != -1)
			fout << dp1[0] << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
	return 0;
}