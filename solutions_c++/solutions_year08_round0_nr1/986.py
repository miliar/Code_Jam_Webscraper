#include<fstream>
#include<vector>
#include<map>
#include<string>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 2)return 0;
	ifstream is(argv[1]);
	ofstream os("A.out");
	int n;
	is>>n;
	for(int casenum = 0; casenum < n; ++casenum)
	{
		int s;
		map<string , int> servers;
		vector<string> querys;
		is>>s;
		char temp[100];
		is.getline(temp,100);//clear the line
		while(s)
		{			
			is.getline(temp,100);
			servers[temp] = 0;
			s--;
		}
		s = (int)servers.size();

		int q;
		is>>q;
		is.getline(temp,100);//clear the line
		while(q)
		{
			is.getline(temp,100);
			querys.push_back(temp);
			q--;
		}
		q = (int)querys.size();

		int nameSum = 0;
		int switchSum = 0;
		for(int i = 0; i < q; ++i)
		{
			if(servers[querys[i]] == 0)
			{
				servers[querys[i]] = 1;
				nameSum += 1;
				if(nameSum == s)
				{
					++switchSum;
					nameSum =0;
					for(map<string,int>::iterator it = servers.begin(); it != servers.end(); ++it)
					{
						it->second = 0;
					}
					--i;//this query still need to be checked
				}
			}
		}
		os<<"Case #"<<casenum+1<<": "<<switchSum<<endl;
	}
	return 0;
}