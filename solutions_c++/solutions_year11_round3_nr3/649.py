#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int N;
	int L;
	int H;
	int* sound=0;
	ifstream fin;
	ofstream fout;
	fin.open("C-small.in");
	fout.open("Csmall-answer.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;
		fin>>L;
		fin>>H;
		sound=new int[N];
		for (int j=0;j<=N-1;j++)
		{
			fin>>sound[j];			

		}

		bool alls=false;
		for (int s=L;s<=H;s++)
		{
			bool symbol=true;
			for (int j=0;j<=N-1;j++)
			{
				if ((sound[j]%s!=0) && (s%sound[j]!=0))
				{
					symbol=false;
					break;
				}
			}
			if (symbol==true)
			{
				fout<<"Case #"<<i<<": "<<s<<endl;
				alls=true;
				break;
			}
		}
		if (alls==false)
		{
			fout<<"Case #"<<i<<": NO"<<endl;
		}
	}
	return 0;
}