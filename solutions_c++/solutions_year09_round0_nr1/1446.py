#include<fstream>
#include<string>
#include<iostream>
#include<cstring>
using namespace std;

const int Max = 5000;
const int Len = 15;

string dict[Max];
bool mark[Len][26];

ifstream fin("qualround1.in");
ofstream fout("qualround1.out");
int L, D, N;

int main()
{
	fin>>L>>D>>N;
	for (int i=0;i<D ;i++ )
	{
		fin>>dict[i];
	}

	for (int i=1;i<=N ;i++ )
	{
		string str;
		int ans = 0;

		fin>>str;
		
		memset(mark, 0, sizeof(mark));
		
		for (int j=0, k=0 ;j<str.size();j++, k++ )
		{
			if (str[j] == '(')
			{
				j++;
				while (str[j] != ')')
				{
					mark[k][int(str[j]-'a')]=1;
					j++;
				}
			}
			else mark[k][int(str[j]-'a')] = 1;
		}

		for (int j=0;j<D ;j++ )
		{
			bool flag = 1;
			for (int k=0;k<L ;k++ )
			{
				if (!mark[k][dict[j][k]-'a'])
				{
					flag = 0;
					break;
				}
			}
			ans += flag;
		}

		fout<<"Case #"<<i<<": "<<ans<<endl;
	}

	return 0;
}
