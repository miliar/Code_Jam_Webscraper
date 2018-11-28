#include<iostream>
#include<set>
#include<queue>
#include<string>
#include<fstream>
using std::ofstream;
using std::ifstream;
using std::string;
using std::set;
using std::cout;
using std::cin;
using std::queue;
using std::endl;
using std::getline;
int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int test_cases;
	in>>test_cases;
	for(int i=1;i<=test_cases;i++)
	{
		int no_of_search_engines;
		in>>no_of_search_engines;
		in.ignore();
		set<string> search_engines1,search_engines2;
		for(int j=1;j<=no_of_search_engines;j++)
		{
			string str;
			getline(in,str);
			search_engines1.insert(str);
		}

		int size=search_engines1.size();
		int no_of_queries;
		in>>no_of_queries;
		int count=0;
		in.ignore();
		for(int k=1;k<=no_of_queries;k++)
		{
			string str;
			getline(in,str);
			set<string>::iterator iter=search_engines1.find(str);
			if(iter!=search_engines1.end())
			{
				search_engines2.insert(str);
				if(search_engines2.size()==size)
				{
					count++;
					search_engines2.clear();
					search_engines2.insert(str);
				}
			}
		}
		out<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
