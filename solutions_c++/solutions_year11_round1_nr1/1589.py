#include <iostream>
#include <fstream>

using namespace std;

int T, N, PD, PG;
int D;

int main()
{
	ifstream ifs("input.txt", ios::in);
	ofstream ofs("output.txt", ios::out);

	ifs >> T;
	for(int t=0; t<T; t++)
	{
		ifs >> N >> PD >> PG;

		bool is_ok = false;
		ofs << "Case #" << t+1 << ": ";

		if(PD==100 && PG!=0)
		{
			is_ok = true;
		}
		else if(PD==0 && PG!=100)
		{
			is_ok = true;
		}
		else if(PD!=100 && PG==100)
		{
			is_ok = false;
		}
		else if(PD!=0 && PG==0)
		{
			is_ok = false;
		}
		else
		{
			for(int n=1; n<=N; n++)
			{
				if((n * PD) % 100 == 0)
				{
					is_ok = true;
					break;
				}
			}
		}

		if(!is_ok)
		{
			ofs << "Broken" << endl;
		}
		else
		{
			ofs << "Possible" << endl;
		}
	}

	ofs.close();
}