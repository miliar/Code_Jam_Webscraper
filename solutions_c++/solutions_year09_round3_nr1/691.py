#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

string str;
int flagnum[46];
int num[200];

bool isAZ(char ch)
{
	if( ch >= 'a' && ch <= 'z')
		return true;
	else return false;
}

int returnPos(char ch)
{
	if(isAZ(ch)) return ch - 'a';
	else return ch - '0' + 26;
}

int main()
{
	int i, j;
	int T, pos, base, len;
	double sum;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	cin >> T;
	for(int ii = 0; ii < T; ii++)
	{
		cin >> str;
		base = 0;
		for( i = 0; i < 46; i++)
			flagnum[i] = -1;
		len = str.length();

		num[0] = 1;
		flagnum[returnPos(str[0])] = 1;

		for(i = 1; i < len; i++)
		{
			if(str[i] == str[0])num[i] = 1;
			else break;
		}
		if( i < len )
		{
			num[i] = 0;
			flagnum[returnPos(str[i])] = 0;
		}
		base = 2;
		for(j = i+1; j < len; j++)
		{
			pos = returnPos(str[j]);
			
			if( flagnum[pos] < 0)
			{
				flagnum[pos] = base;
				num[j] = base;
				base++;
			}
			else
			{
				num[j] = flagnum[pos];
			}

		}
		sum = 0;
		/*for(i = 0; i < len; i++)
			cout << num[i];
		cout << endl;
		cout << base << endl;*/
		cout << "Case #" << ii+1 << ": ";
		for(i = 0; i < len; i++)
			sum += num[i] * pow(base, len-i -1);
		printf("%.0lf\n", sum);
		//cout << sum <<endl;

		
	}
	return 0;
}
