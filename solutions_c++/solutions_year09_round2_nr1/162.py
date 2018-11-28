#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <set>

#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

char buf[100], _buf[10000];
char inp[50000];

set<string> F;

int main()
{
	int N,te=1;
	cin.getline(buf,100);
	istringstream in(buf);
	in >> N;
	while(N--)
	{
		int L;
		cin.getline(buf,100);
		istringstream _in1(buf);
		_in1 >> L;
		int len=0;
		int sp=1;
		FOR(i,0,L)
		{
			cin.getline(buf,100);
			int _len=strlen(buf);
			FOR(j,0,_len)
				if(buf[j] == ' ' && !sp) { inp[len++] = ' '; sp = 1;}
				else if(buf[j] == '(')
				{
					if(!sp) inp[len++] = ' ';
					inp[len++] = '(';
					inp[len++] = ' ';
					sp = 1;
				}
				else if(buf[j] == ')')
				{
					if(!sp) inp[len++] = ' ';
					inp[len++] = ')';
					inp[len++] = ' ';
					sp = 1;
				}
				else { inp[len++] = buf[j]; sp = 0;}
		}
		inp[len++] = '\0';
		
		int A;
		cin.getline(buf,100);
		istringstream _in2(buf);
		_in2 >> A;
		cout << "Case #" << te << ":" << endl;
		//cout << inp << endl;
		FOR(i,0,A)
		{
			cin.getline(_buf,10000);
			istringstream _in3(_buf);
			F.clear();
			string str;
			_in3 >> str;
			int n;
			_in3 >> n;
			while(n--) { _in3 >> str; F.insert(str);}
			istringstream _in(inp);
			double prob = 1.0;
			int done = 0;
			while(!done)
			{
				string str;
				_in >> str;
				assert(str == "(");
				double wt;
				_in >> wt;
				prob *= wt;
				_in >> str;
				if(str != ")")
				{
					if(F.find(str) == F.end())
					{
						_in >> str;
						int lev = 1;
						while(lev)
						{
							_in >> str;
							if(str == "(") lev++;
							if(str == ")") lev--;
						}
					}
				}
				else done = 1;
			}
			printf("%.8lf\n",prob);
		}
		te++;
	}
	return 0;
}
