#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main()
{
	int L,D,N;
	cin >> L >> D >> N;
	vector <string> dic (D);
	for (int i=0;i<D;i++)
	{
		cin >> dic[i];
	}
	for (int caso=1;caso<=N;caso++)
	{
		string s;
		cin >> s;
		int ct=0;
		vector <bool> pos (D,true);
		int res=D;
		for (int i=0;i<L;i++)
		{
			set<char> lc;
			if (s[ct]=='(')
			{
				while(s[ct]!=')')
					lc.insert(s[ct++]);
			}
			else
				lc.insert(s[ct]);
			ct++;
			for (int j=0;j<D;j++)
			{
				if (pos[j])
				{
					if (lc.find(dic[j][i])==lc.end())
					{
						pos[j]=false;
						res--;
					}
				}
			}
		}
		cout << "Case #" << caso << ": " << res << endl;
	}
}
