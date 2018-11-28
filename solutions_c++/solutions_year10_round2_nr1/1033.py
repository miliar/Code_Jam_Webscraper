#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<algorithm>
#include<list>
#include<math.h>
#include<vector>
#include <stdint.h>
#define STR "std::string"
using namespace std;

int main()
{
//	ifstream infile("A-small.txt");
//	ofstream outfile("A-small.out");
//	ifstream infile("A-small-attempt0.in");
//	ofstream outfile("A-small-attempt0.out");
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	
	if(!infile)
	{
		cout<<"Error opening inout file";
		return 1;
	}
	if(!outfile)
	{
		cout<<"Error opening output file";
		return 1;
	}
	int numTestCases;
	infile >> numTestCases;
	for(int i = 1; i<= numTestCases; i++)
	{
		int n, m;
		//Input testcase
		
		std::map<std::string, char> old_dirs[100];
		infile >> n;
		infile >> m;
		//cout << "num is "<<n<<endl;
		//cout << "k is "<<m<<endl;

		/*for(int j=0;j<n;j++)
		{
			std::map<std::string,char> tempmap;
		}*/
		std::map<string,char> dirs;
		for(int j=0;j<n;j++)
		{
			std::string str;
			infile >> str;
			std::string tempstr = str+"/";
			unsigned int start_index=1, index;
			int dir_no=0;
			dirs[str]='0';
			/*
			while((index = tempstr.find_first_of("/",1)) != tempstr.npos)
			{
				cout<<tempstr<<endl;
				std::string dirname = tempstr.substr(1,index-1);
				tempstr = tempstr.substr(index);
				start_index = index;
				cout<< dirname<< " : "<<tempstr<<endl;
				old_dirs[dir_no][dirname] = '1';
				dir_no++;
			}
			cout<<tempstr<<" " <<index<<" " <<start_index;
			*/
		}
			int sum = 0;
		//Process 
		for(int j=0;j<m;j++)
		{
			std::string str;
			infile >> str;
			std::string tempstr = str+"/";
			unsigned int start_index=1, index;
			int dir_no=0;
			
			while((index = str.find_first_of("/",start_index)) != str.npos)
			{
				std::string dirname = str.substr(0,index);
				//cout<<dirname<<endl;
				if(dirs.find(dirname) == dirs.end())
				{
					sum++;
					dirs[dirname]='0';
				}
				start_index = index + 1;
			}
			if(dirs.find(str) == dirs.end())
			{
				sum++;
				dirs[str]='0';
			}
/*
			while((index = tempstr.find_first_of("/",1)) != tempstr.npos)
			{
				cout<<tempstr<<endl;
				std::string dirname = tempstr.substr(1,index-1);
				tempstr = tempstr.substr(index);
				start_index = index;
				cout<< dirname<< " : "<<tempstr<<endl;
				if(old_dirs[dir_no].find(dirname) == old_dirs[dir_no].end())
					sum++;
				dir_no++;
			}
			*/
		}


		//Output result
		outfile << "Case #"<< i <<": " << sum<<"\n";
	}

}
