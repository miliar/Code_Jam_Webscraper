#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <set>
#include <map>

using namespace std;

void swap(string &tmp)
{
	char c = tmp[0];
	tmp[0] = tmp[1];
	tmp[1] = c;
}

int main(int argc, char argv[])
{
	ifstream ifile("B-large.in");
	ofstream ofile("B-large.out");

	//set<string> combine, opposed;

	int case_num, combine_num, opposed_num;
	string tmp;
	ifile >> case_num;

	for(int i=0;i<case_num;++i)
	{
		map<string, char> combine;
		set<string> opposed;
		set<char> opposed_char;

		ifile >> combine_num;
		for(int j=0;j<combine_num;++j)
		{
			ifile >> tmp;
			combine[tmp.substr(0,2)] = tmp[tmp.size()-1];
			swap(tmp);
			combine[tmp.substr(0,2)] = tmp[tmp.size()-1];
		}
		ifile >> opposed_num;
		for(int j=0;j<opposed_num;++j)
		{
			ifile >> tmp;
			opposed_char.insert(tmp[0]);
			opposed_char.insert(tmp[1]);
			opposed.insert(tmp);
			swap(tmp);
			opposed.insert(tmp);
		}
		string invoke;
		ifile >> invoke >> invoke;

		string res = "";
		res += invoke[0];
		for(int j=1;j<invoke.size();++j)
		{
			if(res.size() > 0 && combine_num > 0)
			{
				string in_pair = invoke.substr(j,1) + res[res.size()-1];
				//if((invoke[j] == combine[0] && res[res.size()-1] == combine[1]) || (invoke[j] == combine[1] && res[res.size()-1] == combine[0]))
				if(combine.find(in_pair) != combine.end())
				{
					res.pop_back();
					res += combine[in_pair];
					continue;
				}
			}
			if(opposed_num > 0)
			{
				bool app = true;

				if(opposed_char.find(invoke[j]) != opposed_char.end())
				//if(invoke[j] == opposed[0])
				{
					for(int k=res.size()-1;k>=0;--k)
					{
						string in_pair = invoke.substr(j,1) + res[k];
						//if(res[k] == opposed[1])
						if(opposed.find(in_pair) != opposed.end())
						{
							res.clear();
							app = false;
							break;
						}
					}
				}
				/*
				else if(invoke[j] == opposed[1])
				{
					for(int k=res.size()-1;k>=0;--k)
					{
						if(res[k] == opposed[0])
						{
							res.clear();
							app = false;
							break;
						}
					}
				}
				*/
				if(!app)
					continue;
			}
			res += invoke[j];
		}

		
		ofile << "Case #" << i+1 << ": [";
		if(res.size() > 0)
			ofile << res[0];
		for(int j=1;j<res.size();++j)
			ofile << ", " << res[j];
		ofile << "]\n";
		
	}

	ifile.close();
	ofile.close();

	//system("pause");
	
	return 0;
}

