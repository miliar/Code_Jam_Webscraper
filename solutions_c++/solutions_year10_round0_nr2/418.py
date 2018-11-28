#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;


int main()
{
	ifstream cin("b.in");
	ofstream cout("b.out");
	int c;
	cin>>c;
	int i;
	int n;
	long long t1,t2,t3;
	long long s,s1,s2;
	int j;
	for ( i= 0 ; i < c; i++)
	{
		cin>>n;
		cout<<"Case #"<<i+1<<": "; 
		if (n == 2)
		{
			cin>>t1>>t2;
			if (t1 > t2)
			{
				t3 = t1 - t2;
			}
			else
			{
				t3 = -(t1 - t2);
			}
			if (t1%t3 == 0)
			{
				cout<<'0'<<endl;
			}
			else
			cout<<t3 - (t1%t3)<<endl;

		}
		else
		{
			cin>>t1>>t2>>t3;
			if (t1 > t2)
			{
				s1 = t1 - t2;
			}
			else
			{
				s1 = -(t1 - t2);
			}

			if (t2 > t3)
			{
				s2 = t2 - t3;
			}
			else
			{
				s2 = -(t2 - t3);
			}
			
			if (s1 == 1 || s2 == 1)
			{
				cout<<'0'<<endl;
				
			}
			else
			{
				while (s1!=0&&s2!=0)
				{
					if (s1 >= s2)
					{
						s1 = s1%s2;
					}
					else
					{
						s2 = s2%s1;
					}
				}

				if (s1 == 0)
				{
					s = s2;
				}
				else
				{
					s = s1;
				}
				if (t1%s == 0)
				{
					cout<<'0'<<endl;
				}
				else
				cout<<s - (t1%s)<<endl;
			}
		}

		
	}
}