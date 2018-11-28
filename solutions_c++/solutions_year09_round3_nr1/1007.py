#include <iostream>
#include <fstream>
#include <stdlib.h>;
#include <math.h>
using namespace std;

bool p(char x)
{
	if (x <= '9' && x>='0')
	{
		return true;
	}
	else return false;
}
int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	long long t;
	cin>>t;
	long long i,j,k;
	char a[70];
	long long b[30];
	long long d[10];
	bool c[10];
	long long num;
	long long w1,w2,w3;
	for (i = 0 ; i < t;i++)
	{
		cin>>a;
		for (j = 0 ; j < 30;j++)
		{
			b[j] = -1;
		}

		for (j = 0 ; j < 10;j++)
		{
			c[j] = true;
			d[j] = -1;
		}
		
		for (j = 0 ; j < strlen(a);j++)
		{
			if (!p(a[j]) && b[a[j]-'a'] == -1)
			{
				if (j == 0)
				{
					num = 1;
				}
				else num = 0;
				for (k = num; k < 10; k++)
				{
					if (c[k])
					{
						c[k] = false;
						b[a[j]-'a'] = k;
						break;
					}
				}
			}
			else if (p(a[j]) && d[a[j] - '0'] == -1)
			{
				if (j == 0)
				{
					num = 1;
				}
				else num = 0;
				for (k = num; k < 10; k++)
				{
					if (c[k])
					{
						c[k] = false;
						d[a[j]-'0'] = k;
						break;
					}
				}
			}
		}
		for (j = 9; j >=0;j--)
		{
			if (!c[j])
			{
				num = j+1;
				break;
			}
		}
		w2 = 0;
		w1 = 1;
		for ( j = strlen(a) - 1;j>=0;j--)
		{
			if (p(a[j]))
			{
				w2 += d[a[j] - '0']*w1;
			}
			else
			{
				w2 += b[a[j] - 'a']*w1;
			}
			
			w1 = num * w1;
		}
		cout<<"Case #" << i+1 << ": " << w2 <<endl;
	}
		
	

	
	return 0;
}