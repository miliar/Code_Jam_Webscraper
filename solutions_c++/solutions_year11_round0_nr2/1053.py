#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

bool op[100][100];
char co[100][100];
string ans;

int main()
{
	char ch1, ch2, ch3, ch;
	int t, caseN, i, j, n;
	fin>>t;
	for(caseN = 1; caseN <=t; ++ caseN)
	{
		for(ch1 = 'A'; ch1 <='Z'; ++ch1)
			for(ch2 = 'A'; ch2 <='Z'; ++ch2)
			{
				op[ch1 - 'A'][ch2 - 'A'] = false;
				co[ch1 - 'A'][ch2 - 'A'] = '*';
			}
		ans = "";
		fin>>n;
		for(i=0; i<n; ++i)
		{
			fin>>ch1>>ch2>>ch3;
			co[ch1 - 'A'][ch2 - 'A'] = ch3;
			co[ch2 - 'A'][ch1 - 'A'] = ch3;
		}
		fin>>n;
		for(i=0; i<n; ++i)
		{
			fin>>ch1>>ch2;
			op[ch1 - 'A'][ch2 - 'A'] = true;
			op[ch2 - 'A'][ch1 - 'A'] = true;
		}
		fin>>n;
		for(i=0; i<n; ++i)
		{
			fin>>ch;
			
			bool addCh = true;
			if(!ans.empty())
			{
				if(co[ans[ans.length() - 1] - 'A'][ch - 'A'] != '*')
				{
					ans[ans.length()-1] = co[ans[ans.length() - 1] - 'A'][ch - 'A'];
					addCh = false;
				}
			}
			if(addCh)
			for(j=0; j<ans.length(); ++j)
				if(op[ans[j] - 'A'][ch - 'A'])
				{
					ans.clear();
					addCh = false;
					break;
				}

			if(addCh)
				ans+=ch;
		}
		fout<<"Case #"<<caseN<<": ";
		fout<<"[";
		if(!ans.empty())
			fout<<ans[0];
		for(i=1; i<ans.length(); ++i)
			fout<<", "<<ans[i];
		fout<<"]"<<endl;
	}
	return 0;
}