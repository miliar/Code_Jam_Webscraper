#include <fstream>
#include <bitset>
#include <map>
#include <string>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int num;
	fin >> num;
	for(int cas = 1; cas <= num; cas++)
	{
		int res(0);
		map<string,int> mp;
		int seaNameNum;
		int indNum;
		fin >> seaNameNum;
		bitset<101> flag(0);
		string strtmp;
		getline(fin, strtmp);
		for(int i = 1 ; i <= seaNameNum; i++)
		{
			getline(fin,strtmp);
			mp[strtmp] = i;
		}
		fin >> indNum;
		getline(fin,strtmp);
		for(int i = 0; i < indNum; i++)
		{
			getline(fin,strtmp);
			if(mp[strtmp])
			{
				flag[mp[strtmp]] = 1;
				if(flag.count() == seaNameNum)
				{
					res++;
					flag = 0;
				}
				flag[mp[strtmp]] = 1;
			}
		}

		fout << "Case #" << cas <<": " << res << endl;
	}
	
	
}