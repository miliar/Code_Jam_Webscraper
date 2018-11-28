#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace  std;

string tmp;

int main() 
{
	ifstream fin("A-small-attempt0.in");
    int ans=0;
	int N;
	fin>>N;
	getline(fin,tmp);
	int n=1;
	int used=0;
	while (n<=N)
	{
		ans=0;

		int NumEngines;
		fin>>NumEngines;
		getline(fin,tmp);
		map<string,int> engines;
		string tmp;
	

		for (int i=0;i<NumEngines;++i)
		{
			getline(fin,tmp);
			engines[tmp]=i;
		}
		int Numwords;
		fin>>Numwords;
		getline(fin,tmp);
		vector<char> flag;
		flag.assign(NumEngines,0);
		used=0;
		bool down=true;
		for (int i=0;i<Numwords;++i)
		{
			if (down)
			{
				getline(fin,tmp);
			}
			down=true;

			if (engines.count(tmp)>0)
			{
				if (flag[engines[tmp]]==0)
				{
					flag[engines[tmp]]=1;
					++used;
					if (used==NumEngines)
					{
						used=0;
						++ans;
						memset(&flag[0],0,NumEngines);
						--i;
						down=false;
					}
				}
			}
			
		}
		cout<<"Case #"<<n<<": "<<ans<<endl;
		++n;
	}
	return 0;
}