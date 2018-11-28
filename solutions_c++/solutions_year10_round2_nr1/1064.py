#include <fstream>
#include <boost\algorithm\string.hpp>
#include <vector>
#include <cmath>
#include <map>
#include <mpir.h>

using namespace std;
using namespace boost;

int main (int argc, char *argv[])
{
	//argc = 3;
	//argv[1] = "E:/raj/dev/Projects/IN_OUT/input.txt";
	if (argc < 1)
	{
		exit(1);
	}
	else
	{
		string line;
		ifstream i_fh(argv[1]);
		ofstream o_fh("E:/raj/dev/Projects/IN_OUT/output.txt");
		if(i_fh.is_open())
		{
			while(!i_fh.eof())
			{
				getline(i_fh, line);
				trim(line);
				int T, N, M;
				T = atoi(line.c_str());
				vector<string> tmp;
				map<string, int> hsh;
				int n_mkdir;
				for(int T_index = 0; T_index < T; T_index++)
				{
					n_mkdir = 0;
					tmp.clear();
					hsh.clear();
					getline(i_fh, line);
					trim(line);
					split(tmp, line, is_any_of(" "));
					N = atoi(tmp[0].c_str());
					M = atoi(tmp[1].c_str());
					
					for(int N_index = 0; N_index < N; N_index++)
					{
						getline(i_fh, line);
						trim(line); 
						hsh[line] = 1;
					}
					tmp.clear();
					for(int M_index = 0; M_index < M; M_index++)
					{
						string joined;
						getline(i_fh, line);
						trim(line); 
						if(hsh.count(line) == 1)
							continue;
						else
						{
							n_mkdir++;
							hsh[line] = 1;
							split(tmp, line, is_any_of("/"));
							tmp.pop_back();
							joined = join(tmp, "/");
							//joined = "/" + joined;
							while(joined != "" && hsh.count(joined) == 0)
							{
								n_mkdir++;
								hsh[joined] = 1;
								tmp.clear();
								split(tmp, joined, is_any_of("/"));
								tmp.pop_back();
								joined = join(tmp, "/");
								//joined = "/" + joined;
							}
						}
						
					}
					//write to 0_fh in the end
					o_fh <<"Case #"<<T_index+1<<": "<<n_mkdir<<endl;
				}
			}
			o_fh.close();
		}
		i_fh.close();
	}
}