#include<fstream.h>
#include<conio.h>
void main()
{
	clrscr();
	int N=0,K=0,T=0,state[10] = {0},power[10] = {0};
	power[0] = 1;
	char ch;
	ofstream fout;
	fout.open("output.txt");
	fout.seekp(0);
	ifstream fin;
	fin.open("A-small-attempt1.in");
	fin.seekg(0);
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		fin.get(ch);
		fin>>N;
		fin.get(ch);
		fin>>K;
		for(int m=0;m<10;m++)
		{
			state[m] = 0;
			power[m] = 0;
		}
		power[0] = 1;
		for(int j=1;j<=K;j++)
		{
			for(int k=0;k<N;k++)
			{
				if(power[k] == 1)
				{
					if(state[k] == 0)
						state[k] = 1;
					else
						state[k] = 0;
				}
			}
			for(k=1;k<N;k++)
			      power[k] = state[k-1]*power[k-1];
		}
		if(state[N-1] == 1 && power[N-1] == 1)
			fout<<"Case #"<<i<<": ON\n";
		else
			fout<<"Case #"<<i<<": OFF\n";
	}
	fin.close();
	fout.close();
	getch();


}