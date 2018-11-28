#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int l,d,n;
	cin>>l>>d>>n;
	char a[5001][20];
	char b[500];
	char c[30][501];
	int e[20];
	

	int i;
	for (i = 0 ; i < 16; i++)
	{
		e[i] = 0;
	}
	int k1,k2,k3,k4;
	bool p;
	for (i = 0 ; i < d; i++)
	{
		cin>>a[i];
	}
	for (i = 0 ; i < n; i++)
	{
		cin>>b;
		for (k1= 0; k1 < l; k1++)
		{
			e[k1] = 0;
		}
		k1 = 0;k2 = -1;k4 = 0;
		p = false;
		
		while (b[k1])
		{
			if (b[k1] == '(')
			{
				p = true;
				k2 = k1;
			}
			else if (b[k1] == ')')
			{
			     p =false;
				 k4++;
				 
			}
			else if (!p)
			{
				c[k4][0] = b[k1];
				e[k4] = 1;
				k4++;
			}
			else
			{
				c[k4][e[k4]] = b[k1];
				e[k4]++;
			}
			k1++;
		}
		/*
		for(k1 = 0; k1 < l; k1++)
		{
			cout<<e[k1];
			for (k2 = 0; k2 < e[k1];k2++)
			{
				cout<<c[k1][k2];
			}
			
			
			
		}
		
		cout<<endl;*/
		k3 = 0;bool q;
		for (k1 = 0 ; k1 < d; k1++)
		{
			p = true;
			for (k2 = 0 ; k2 < l; k2++)
			{
				q = false;
				for (k4 = 0 ; k4 < e[k2] ; k4++)
				{
					if (a[k1][k2] == c[k2][k4])
					{
						
						q = true;
						break;
					}
				}
				if (!q)
				{
					//cout<<k1<<" "<<k2<< endl;
					p = false;
					break;
				}
			}
			if (p)
			{
				k3++;
			}
		}
		//cout<<endl;
		cout<<"Case #" << i+1 << ": " << k3<<endl;

	}
	return 0;
}