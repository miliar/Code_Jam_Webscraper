#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<bitset>
#include<list>
using namespace std;

char mapp[26] =
{ 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k',
		'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

int main()
{
	int T;
	cin>>T;
	getchar();
	for (int i = 1; i <= T; ++i)
	{
		string inStr;
		getline(cin, inStr);
		for (unsigned int j = 0; j < inStr.size(); ++j)
		{
			inStr[j] = ((inStr[j] == ' ' )? ' ':mapp[int(inStr[j] - 'a')] );
		}
		cout << "Case #" << i << ": " << inStr.c_str() << endl;
	}
	return 0;
}
