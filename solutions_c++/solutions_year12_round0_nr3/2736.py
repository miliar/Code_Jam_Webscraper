#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	ifstream in("recycle.in");
	ofstream out("recycle.out");
	int t;
	in >> t;
	for (int test = 1; test <= t; test++)
	{
		int a, b, ans = 0;
		in >> a >> b;
		//check no of digits
		int digits;
		{
			stringstream ss;
			ss << a;
			string s;
			ss >> s;
			digits = s.size();
		}
		for (int i = a; i <= b; i++)
		{
			//convert i to string
			string s;
			{
				stringstream ss;
				ss << i;
				ss >> s;
			}
			int good = true;
			//check some digits are different
			for (int j = 1; j < digits; j++)
				if (s[0] != s[j])
					good = false;
			if (good)
				continue;
			
			int found = 1;
			int going = 0;
			//try moving
			for (int j = 0; j < digits - 1; j++)
			{
				string str = s;
				string sub = str.substr(0, j + 1);
				str.erase(0, j + 1);
				str.append(sub);
				//check valid
				if (str[0] == '0')
					continue;
				stringstream ss;
				ss << str;
				int q;
				ss >> q;
				if (q > b || q < a)
					continue;
				if (q < i)
				{
					going = 0;
					break;
				}
				if (q == i)
				{
					break;
				}
					
				going += found;
				found++;
			}
			ans += going;
		}
		out << "Case #" << test << ": " << ans << "\n";
	}
}