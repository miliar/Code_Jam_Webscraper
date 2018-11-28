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

	int ncases = 0;
	string ncases_str = readline(ifs);
	istringstream iss(ncases_str);
	iss>>ncases;

	for(int nc=0; nc<ncases; nc++)
	{
		unsigned long long N, Pd, Pg;
		istringstream c(readline(ifs));
		c>>N>>Pd>>Pg;

		bool possible = false;
		for(unsigned long long n=1; n<=N; n++)
		{
			if((Pd*n)%100 == 0)
			{
				//cout<<"possible N = "<<n<<endl;
				unsigned long long wins = n*Pd/100;
				unsigned long long losses = n-wins;

				unsigned long long G = n;
				int x = 0;
				while(1)
				{
					if(x > 10000) break;
					x++;

					
					if((Pg*G)%100 == 0)
					{
						unsigned long long gwins = G*Pg/100;
						unsigned long long glosses = G-gwins;
						if(gwins >= wins && glosses >= losses)
						{
							//cout<<"G="<<G;
							possible = true;
							break;
						}
					}
					G++;
				}
			}

			if(possible)
				break;
		}
		
		string res = ( possible == true ) ? "Possible" : "Broken";
		cout<<"Case #"<<nc+1<<": "<<res<<endl;
	}

	return 0;
}