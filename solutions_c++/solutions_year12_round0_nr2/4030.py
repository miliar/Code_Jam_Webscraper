#include <vector>
#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <climits>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>

using namespace std;

bool istrip(int a, int b , int c)
{
	if( abs(a-b) <= 2 && abs(a-c) <= 2 && abs(c-b) <= 2)
	{
		return true;
	}

	return false;
}

bool issur(int a, int b , int c)
{
	if( abs(a-b) == 2 || abs(a-c) == 2 || abs(c-b) == 2)
	{
		return true;
	}

	return false;
}

int main()
{

	ifstream cin("B-small-attempt0.in");
	ofstream cout("google2.out");

	int t;
	cin >> t;

	for(int cn=1;cn<=t;cn++)
	{

		int n,s,p;
		cin >> n >> s >> p;

		vector<int> vec;

		while(n--)
		{
			int x;
			cin >> x;
			vec.push_back(x);
		}

		int res = 0;

		for(int i=0;i<vec.size();i++)
		{

			bool canwithout = false;
			bool canwith = false;

			for(int a=0;a<=10;a++)
			{
				for(int b=0;b<=10;b++)
				{
					for(int c=0;c<=10;c++)
					{
						if(a+b+c == vec[i]  )
						{
							
							if(istrip(a,b,c) && !issur(a,b,c)&& max(max(a,b),c)>= p)
							{
								canwithout = true;
							}
							
							if(istrip(a,b,c) && issur(a,b,c) && s>0 && max(max(a,b),c)>= p)
							{
								canwith = true;
							}

							
						}
					}
				}
			}

			if(canwithout  )
			{
				res++;
			}
			else if(!canwithout && canwith && s>0)
			{
				res++;
				s--;
			}

		}

		cout << "Case #" << cn << ": " << res << endl;

	}

	system("pause");
}