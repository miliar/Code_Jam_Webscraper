#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
	int i;
	ifstream in("D:\\B-small-attempt2.in");
	ofstream out("D:\\B-small_result.txt");

	int T, caseN = 1;
	int S, N;
	int p;
	int t[105]={0};

	in >> T;
	while (T--)
	{
		int cnt;
		int rem, aver;

		in >> N >> S >> p;
		for (i=0; i<N; i++)
			in >> t[i];

		cnt = 0;
		for (i=0; i<N; i++)
		{
			aver = t[i] / 3;
			rem  = t[i] % 3;

			if (aver >= p) 
			{
				cnt++;
				continue;
			}
			if (aver+2 < p)
			{
				continue;
			}

			//aver+1, aver+2  == ? p
			if (rem == 0)
			{
				if ( (aver>0) && (aver+1==p) && (S>0) )
				{
					S--;
					cnt++;
				}
			}
			else if (rem == 1)
			{
				if (aver+1 == p)
				{
					cnt++;
				}
			}
			else //rem==2
			{
				if (aver+1 == p)
				{
					cnt++;
					continue;

				}
				if ( (aver+2>=p) && (S>0) )
				{
					cnt++;
					S--;
				}
			}
		}

		out << "Case #" << caseN++ << ": " << cnt << endl;
	}
	
	return 0;
}