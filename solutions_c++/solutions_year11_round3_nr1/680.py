#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int R;
	int C;
	bool symbol;
	char* square=0;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("Alarge-answer.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>R;
		fin>>C;
		symbol=true;
		square=new char[R*C];
		for (int j=0;j<=R-1;j++)
		{
			for (int k=0;k<=C-1;k++)
			{
				fin>>square[j*C+k];
			}
		}

		int j=0;
		int k=0;
		while(j<=R-1)
		{
			int s;
			for (s=k;s<=C-1;s++)
			{
				if (square[j*C+s]=='#')
				{
					k=s;
					break;
				}
			}

			if (s==C)
			{
				j++;
				k=0;
			}
			else
			{
				if ((j==R-1) || (k==C-1))
				{
					fout<<"Case #"<<i<<":"<<endl;
					fout<<"Impossible"<<endl;
					symbol=false;
					break;
				}
				else
				{
					if ((square[j*C+k+1]!='#') || (square[(j+1)*C+k]!='#') || (square[(j+1)*C+k+1]!='#'))
					{
						fout<<"Case #"<<i<<":"<<endl;
						fout<<"Impossible"<<endl;
						symbol=false;
						break;
					}
					else
					{
						square[j*C+k]=47;
						square[j*C+k+1]=92;
					    square[(j+1)*C+k]=92;
						square[(j+1)*C+k+1]=47;
					}
				}
			}
		}

		if (symbol==true)
		{
			fout<<"Case #"<<i<<":"<<endl;
			for (j=0;j<=R-1;j++)
			{
				for (k=0;k<=C-1;k++)
				{
					fout<<square[j*C+k];
				}
				fout<<endl;
			}
		}
	}
	return 0;
}