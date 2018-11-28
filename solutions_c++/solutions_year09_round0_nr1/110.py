#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int ww[22];

int main(void)
{
	int L,D;
	cin >> L >> D;
	int CC;
	cin >> CC;
	vector<string> vs;
	string s;
	for(int i=0;i<D;++i)
	{cin >> s;vs.push_back(s);}
	for(int cn=1;cn <= CC;++cn)
	{
		int out = 0;
		cin >> s;
		for(int i=0,at=0;at<L;++at)
		{
			if(s[i] == '(')
			{
				++i;
				ww[at] = 0;
				while(s[i] != ')')
				{
					ww[at] |= (1<<(s[i]-'a'));
					++i;
				}
				++i;
			}
			else
			{
				ww[at] = (1<<(s[i]-'a'));
				++i;
			}
		}
		for(int i=0;i<D;++i)
		{
			for(int j=0;j<L;++j)
			{
				if((ww[j]&(1<<(vs[i][j]-'a')))==0)
				{goto el;}
			}
			++out;el:;
		}
		cout << "Case #" << cn << ": " << out << endl;
	}
	return 0;
}
