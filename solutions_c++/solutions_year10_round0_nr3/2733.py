#include <fstream>
#include <iostream>
#include <boost/algorithm/string.hpp>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;
using namespace boost;

int main(int argc, char* argv[])
{
	if (argc < 1)
	{
		cerr <<"Not enough arguments";
		exit(1);
	}
	else
	{
		string line;
		ifstream i_fh(argv[1]);
		ofstream o_fh("E:/files/output.txt");
		if(i_fh.is_open())
		{
			while(!i_fh.eof())
			{
				getline(i_fh, line);
				trim(line);
				int T;
				T = atoi(line.c_str());
				vector<string> rkn;
				vector<string> tmp;
				list<int> helper;
				list<int> Q;
				
				for(int t_index=0; t_index<T ; t_index++)
				{
					int R,K,N;
					int running_count, euros;
					getline(i_fh, line);
					trim(line);
					split(rkn, line, is_any_of(" "));
					R = atoi(rkn[0].c_str());
					K = atoi(rkn[1].c_str());
					N = atoi(rkn[2].c_str());
					getline(i_fh, line);
					trim(line);
					split(tmp, line, is_any_of(" "));
					Q.clear();
					//cout <<"Case "<<t_index<<endl<<"R K N"<<R<<" "<<K<<" "<<N<<endl;
					int tmp_size = tmp.size();
					for(int i = 0; i < N; i++)
						Q.push_back(atoi(tmp[i].c_str()));
					euros = 0;
					for(int r_index = 0; r_index != R; r_index++)
					{
						running_count = 0;
						while(Q.size() !=0 && Q.front()+running_count <= K)
						{
							running_count += Q.front();
							helper.push_back(Q.front());
							Q.pop_front();
						}
						int helper_size = helper.size();
						for(int i = 0; i < helper_size; i++)
						{
							Q.push_back(helper.front());
							helper.pop_front();
						}
						euros += running_count;
					}
					o_fh <<"Case #"<<t_index+1<<": "<<euros<<endl;
				}
				o_fh.close();
			}
		}
		i_fh.close();
	}
	
	return 0;
}