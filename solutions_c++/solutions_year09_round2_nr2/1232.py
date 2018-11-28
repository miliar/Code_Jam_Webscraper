
#include <conio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;


string calc(string s)
{
	string res;
	for (int i = s.length() - 1; i >= 0; i--)
	{
		if (i == 0)
		{
			sort(s.begin(), s.end());
			if (s[0] == '0')
			{
				for (int j = 1; j < s.size(); j++)
				{
					if (s[j] != '0')
					{
						char a = s[j];
						s[j] = '0';
						s[0] = a;
						break;
					}
				}	
			}
			string s1 = "0";
			res = s[0] + s1 + s.substr(1, s.size() - 1);
			return res;
		}
		if (s[i] <= s[i-1]) continue;
		if (s[i] > s[i-1])
		{
			string ss = s.substr(0, i - 1);
			string sss = s.substr(i, s.size() - i);
			sort(sss.begin(), sss.end());
			for (int j = 0; j < sss.size(); j++)
			{
				if (sss[j] > s[i - 1])
				{
					string si;
					si = sss[j];
					sss.erase(j, 1);
					sss += s[i - 1];
					sort(sss.begin(), sss.end());
					res = ss + si + sss;
					return res;
				}
			}
		}
	}
	return res;
}
int main(int argc, _TCHAR* argv[])
{
	string file_name_input = "f:\\code_jam_files\\1.in",
		   file_name_output = "f:\\code_jam_files\\2.out",
		   s;

	ifstream is;
	ofstream os;
	
	is.open(file_name_input.c_str(), ios_base::in);
	os.open(file_name_output.c_str(), ios_base::out);

	if (!is || !os)
	{
		cout<<"error";
		getch();
		return 0;
	}

	int n;
	long long N;
	is>>n;
	is.ignore();
	for (int cases = 1; cases <= n; cases++)
	{
		is>>s;
		is.ignore();
		string res;
		res = calc(s);

		cout<<res<<"\n";

		os<<"Case #"<<cases<<": "<<res<<endl;
	}
	is.close();
	os.close();
	cout<<"done!";

	getch();
	return 0;
}

