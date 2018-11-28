#include <iostream>
using namespace std;
#include <fstream>
#include <string>
#include <sstream>
#include <hash_map>


void rcnum(string fpath)
{
	ifstream fin(fpath);
	ofstream fout("out.txt");
	

	if(!fin)
	{
		cout<<"Fail to read file"<<endl;
		system("PAUSE");
		exit(1);
	}
	
	int temp;
	int num;
	fin>>num;

	
	for(int i=0; i<num;i++)
	{
		hash_map<string,bool> hmap;
		int A,B;
		int sum=0;
		fin>>A>>B;	
		for(int j=A; j<=B; j++)
		{
			ostringstream ss;
			ss<<j;
			string sa = ss.str();
			string so = sa;
			if(j>9)
			{
				for(int k=0; k<sa.size()-1; k++)
				{
					sa = sa[sa.size()-1]+sa.substr(0,sa.size()-1);
					
					if( sa[0] != '0' && sa!=so && atoi(sa.c_str()) <= B && hmap[so+sa] != true && atoi(sa.c_str()) > atoi(so.c_str()))
					{
						sum++;
						hmap[so+sa] = true;
					}
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<sum;
		fout<<endl;
	}

	fin.close();
	fout.close();
}

void main()
{
	string fpath = "C-small-attempt0.in";
	rcnum(fpath);
	system("PAUSE");
}