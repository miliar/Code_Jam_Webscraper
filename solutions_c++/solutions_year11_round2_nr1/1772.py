#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define LEN 50000
#define INPUT "C:\\temp\\A-small.in"


static void print(string i)
{
	cout<<i<<endl;
}

static string readline(ifstream& ifs)
{
	char line[LEN];
	ifs.getline(line, LEN);
	string s = line;
	return s;
}

static string int_to_string(long i)
{
	ostringstream oss;
	oss<<i;
	return oss.str();
}

static long string_to_int(string s)
{
	istringstream iss(s);
	int i;
	iss>>i;
	return i;
}


int main()
{
	ifstream ifs;
	ifs.open(INPUT);

	int ncases = string_to_int(readline(ifs));

	for(int nc=0; nc<ncases; nc++)
	{
		int N = string_to_int(readline(ifs));

		string buf(N, ' ');
		vector<string> scores(N, buf);

		for(int i=0; i<N; i++)
			scores[i] = readline(ifs);

		cout<<"Case #"<<nc+1<<":"<<endl;

		vector<double> wpall(N, 0);
		for(int team=0; team < N; team++)
		{
			double wp = 0;
			int sz = scores.size();

			double ngames = 0, won = 0;
			for(int i=0; i<sz; i++)
			{
				if(scores[team][i] != '.') 
					ngames++;

				if(scores[team][i] == '1')
					won++;
			}
			wp = won/ngames;
			wpall[team] = wp;
		}

		vector<double> owpall(N, 0);
		for(int team=0; team < N; team++)
		{
			double owp = 0;
			int x = 0;

			for(int j = 0; j<N; j++)
			{
				if(j==team)
					continue;

				if(scores[team][j] == '.')
					continue;
				else
					x++;

				double ngames = 0, won = 0;
				for(int k=0; k<N; k++)
				{
					if(k!=team)
					{
						if(scores[j][k] != '.')
							ngames++;

						if(scores[j][k] == '1')
							won++;
					}
				}

				owp += (won/ngames);
			}
			
			owpall[team] = owp/x;
		}


		vector<double> oowpall(N, 0);
		for(int i=0; i<N; i++)
		{
			double oowp = 0;
			int x = 0;
			for(int j=0; j<N; j++)
			{
				if(j!=i && scores[j][i] != '.')
				{
					oowp += owpall[j];
					x++;
				}
			}

			oowpall[i] = oowp/x;
		}


		for(int i=0; i<N; i++)
		{
			double res = 0.25*wpall[i] + 0.5*owpall[i] + 0.25*oowpall[i];
			cout<<res<<endl;
		}

	}

	return 0;
}