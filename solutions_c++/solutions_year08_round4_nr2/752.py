#include<fstream>
#include<iostream>
using namespace std;

int tests, n, m, A, a, b, c,a1,b1,c1;
bool spr(int n, int m)
{
	//for(a1 = 0; a1 <=n; a1++)
	//{
		for(b1 = 0; b1<=n; b1++)
		{
			for(c1=0; c1<=n; c1++)
			{
				//for(a = 0; a <= m; a++)
				//{
					for( b = 0; b <= m; b++)
					{
						for( c = 0; c <=m; c++)
						{
							if(a1*(c-b) + b1*(a-c) + c1*(b-a) == A)
								return true;
						}
					}
				//}
			}
		}
	//}
return false;
}
int main()
{
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");	
	cin>>tests;
	for(int d = 0; d < tests; d++)
	{	a1 = 0; a = 0;	
		cin>> n >>m>> A;
		//n/=2; m/=2;
		if(spr(n,m))
			cout <<"Case #"<<d+1<<": "<< a1 << " " << a<<" " << b1 << " " <<b<<" "<<c1<<" " <<c<< '\n';
		else
			cout <<"Case #"<<d+1<<": IMPOSSIBLE\n";
	}
	//cin.close();
	//cout.close();
	return 0;
}