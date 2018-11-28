#include <iostream>
#include <string>
using namespace std;

int main()
{
	int test;
	
	char ss[105] ;
	string input;
	freopen("d:\\A-small-attempt0.in", "r", stdin);
	freopen("d:\\out.txt", "w", stdout);
	cin >> test;
		gets(ss);

	char cc, tt;
	for(int t = 1; t<=test;t++)
	{
		cout << "Case #" << t <<": " ;
		gets(ss);
		input = ss;
		for(int i=0;i<input.length();i++)
		{
			cc = input[i];
			if(cc == 'a')   tt = 'y';
			else if(cc == 'b')   tt = 'h';
			else if(cc == 'c')   tt = 'e';
			else if(cc == 'd')   tt = 's';
			else if(cc == 'e')   tt = 'o';
			else if(cc == 'f')   tt = 'c';
			else if(cc == 'g')   tt = 'v';
			else if(cc == 'h')   tt = 'x';
			else if(cc == 'i')   tt = 'd';
			else if(cc == 'j')   tt = 'u';
			else if(cc == 'k')   tt = 'i';
			else if(cc == 'l')   tt = 'g';
			else if(cc == 'm')   tt = 'l';
			else if(cc == 'n')   tt = 'b';
			else if(cc == 'o')   tt = 'k';
			else if(cc == 'p')   tt = 'r';
			else if(cc == 'q')   tt = 'z';
			else if(cc == 'r')   tt = 't';
			else if(cc == 's')   tt = 'n';
			else if(cc == 't')   tt = 'w';
			else if(cc == 'u')   tt = 'j';
			else if(cc == 'v')   tt = 'p';
			else if(cc == 'w')   tt = 'f';
			else if(cc == 'x')   tt = 'm';
			else if(cc == 'y')   tt = 'a';
			else if(cc == 'z')   tt = 'q';
			else
				tt = cc;

			cout << tt;
		}
		cout << endl;
	}
	return 0;
}