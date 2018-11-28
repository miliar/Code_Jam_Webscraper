#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <cstring>

using namespace std;

int main(int argc, char **argv)
{
	if(argc != 2)
	{
		cout << "Wrong args" << endl;
		return 1;
	}

	ifstream f(argv[1]);
	ofstream o("coutput.txt", ofstream::out);

	int T;
	f >> T;
	char buf[20];
	char val[20];
	char *p;
	map<string,bool> result;
	int count = 0;

	for(int i = 0 ; i < T; i++)
	{
		count = 0;
		result.clear();
		int A,B;
		f >> A;
		f >> B;
		int s, m;
		string res;
		if(B >= 21)
		{
			for	(int n = A; n <= B; n++)
			{
				sprintf(buf, "%d", n);
				p = buf;
				s = strlen(buf);
				for(int k = 0; k < s-1; k++)
				{
					p[s] = p[0];
					p++;
					p[s] = 0;
		
					//cout << p << " ";

					if(p[0] == '0') continue;
					sscanf(p, "%d", &m);
					if(m <= n || m > B) continue;
					sprintf(val, "%d,%d", n,m);
					//cout << val;
					if(result.count(val) == 0)
					{
						//cout << val << endl;
						result[val] = true;
						count++;
					}
					//cout << endl;
				}
			}
		}
		o << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}
