#include <iostream>
using namespace std;
#include <fstream>
#include <string>


void googledance(string fpath)
{
	ifstream fin(fpath);
	ofstream fout("out.txt");


	if(!fin)
	{
		cout<<"Fail to read file"<<endl;
		system("PAUSE");
		exit(1);
	}
	
	int score;
	int sur;
	int p;
	int num;
	int g_num;
	
	fin>>num;

	
	for(int i=0; i<num;i++)
	{
		int sum=0;

		fin>>g_num;
		fin>>sur;
		fin>>p;
		fout<<"Case #"<<i+1<<": ";

		for(int j=0; j<g_num; j++)
		{
			fin>>score;
			int base = score/3;
			int left = score%3;

			switch(left)
			{
				case 0:
					if(base >= p)
						sum++;
					else if(sur>0 && base> 0 && base+1 >= p)
					{
						sum++;
						sur--;
					}
					break;
				case 1:
					if(base >= p || base+1 >= p)
						sum++;
					else if(sur>0 && base+1 >= p)
					{
						sum++;
						sur--;
					}
					break;				
				case 2:
					if(base >= p || base+1 >= p)
						sum++;
					else if(sur>0 && base+2 >= p)
					{
						sum++;
						sur--;
					}
					break;		
			}

		}

		fout<<sum;
		fout<<endl;
	}

	fin.close();
	fout.close();
}

void main()
{
	string fpath = "B-large.in";
	googledance(fpath);
	system("PAUSE");
}