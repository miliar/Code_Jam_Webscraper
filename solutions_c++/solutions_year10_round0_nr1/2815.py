#include <fstream>
#include <cmath>
#include <vector>
#include <iostream>
#include <boost/algorithm/string.hpp>

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
		ofstream o_fh("E:/files/snapper_out.txt");
		if(i_fh.is_open())
		{
			while(!i_fh.eof())
			{
				getline(i_fh, line);
				trim(line);
				int T;
				T = atoi(line.c_str());
				vector<string> vec;
				for(int t_index=0; t_index<T ; t_index++)
				{
					getline(i_fh, line);
					trim(line);
					split(vec, line, is_any_of(" "));
					long int N = atoi(vec[0].c_str());
					long long int K = atoi(vec[1].c_str());

					long long power = pow(2.0, N);
					long double div = double(K) / double(power);
					long long int Num1 = floor(div);
					long long int Num2 = ceil(div);

					if ((power*Num1)-1 == K || (power*Num2)-1 == K)
						o_fh <<"Case #"<<t_index+1<<": "<<"ON"<<endl;
					else
						o_fh <<"Case #"<<t_index+1<<": "<<"OFF"<<endl;
				}
				o_fh.close();
			}
			i_fh.close();
		}
	}
	return 0;
}