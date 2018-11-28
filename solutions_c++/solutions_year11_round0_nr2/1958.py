#include <iostream> 
#include <cmath> 
#include <string> 
#include <cstring> 
#include <set> 
#include <map> 
#include <vector> 
#include <cstdio> 
using namespace std; 

int main(int argc, char *argv[]) 
{ 
 freopen("A.txt","r",stdin);
freopen("AOUT.txt","w",stdout);
	int tstCs = 1;
	int T = 0;
	cin >> T;
	while (T--)
	{
		int C;
		int cnct[192][192];
		memset(cnct, 0, sizeof cnct);
		cin >> C;
		string cmb; 
		for (int i = 0; i < C; i++)
		{
			cin >> cmb;
			cnct[cmb[0]][cmb[1]] = cnct[cmb[1]][cmb[0]] = (int)cmb[2];
		}
		int D;
		cin >> D;
		bool opst[192][192];
		memset(opst, false, sizeof opst);
		string so;
		for (int i = 0; i < D; i++)
		{
			cin >> so;
			opst[so[0]][so[1]] = opst[so[1]][so[0]] = true;		
		}
		int N;
		cin >> N;
		string list;
		cin >> list;
		string ret = "";
		for (int i = 0; i < N; i++)
		{
			char c = list[i];
			ret += c;
			int sz = ret.size();
			if (sz < 2) continue;
			char c1 = ret[sz-1], c2 = ret[sz-2];
			if (cnct[c1][c2] != 0)
			{
				ret = ret.substr(0, sz-2)+(char)cnct[c1][c2];
				for (int j = 0; j < ret.size(); j++)
				{
					if (opst[ret[j]][cnct[c1][c2]])
					{
						ret = "";
						break;
					}
				}
				continue;
			}
			else
			{
				for (int j = 0; j < sz; j++)
				{
					if (opst[ret[j]][c])
					{
						ret = "";
						break;
					}
				}
			}
		}
		cout << "Case #" << tstCs++ << ": [";
		for (int i = 0; i < ret.size(); i++)
		{
			if (i == ret.size()-1)
			{
				cout << ret[i];
			}
			else
				cout << ret[i] << ", ";
		}
		cout << "]" << endl;
	}
    return 0; 
}

