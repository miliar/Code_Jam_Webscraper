#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A-large.in");
	int T = 0;
	fin>>T;
	int N = 0;
	int Bprev = 1, Oprev = 1;
	char cha;
	int Onow, Bnow, Otime, Btime, contBtime = 0, contOtime = 0;
	char pre = ' ';
	int sum = 0;
	ofstream fout("res.txt");
	for(int t = 1; t<=T; t++)
	{
		fin >> N;
		sum = 0;
		contBtime = 0;
		contOtime = 0;
		pre = ' ';
		Bprev = 1; Oprev = 1;
		for(int n = 1; n <= N; n++)
		{
			fin >> cha;
			if(cha == 'O')
			{
				fin >> Onow; 
				Otime = abs(Onow - Oprev) + 1;
				if(pre == ' '|| pre == 'O')
				{
					sum += Otime;
					contOtime += Otime;
				}
				else
				{
					if(Otime <= contBtime)
					{
						sum += 1;
						contOtime = 1;
					}
					else
					{
						sum += (Otime - contBtime);
						contOtime = Otime - contBtime;
					}
				}
				pre = 'O';
				Oprev = Onow;
			}
			else
			{
				fin >> Bnow; 
				Btime = abs(Bnow - Bprev) + 1;
				if(pre == ' '|| pre == 'B')
				{
					sum += Btime;
					contBtime += Btime;
				}
				else
				{
					if(Btime <= contOtime)
					{
						sum += 1;
						contBtime = 1;
					}
					else
					{
						sum += (Btime - contOtime);
						contBtime = Btime - contOtime;
					}
				}
				pre = 'B';
				Bprev = Bnow;
			}	
		}
		fout << "Case #" << t << ": " << sum <<endl;
	}
}