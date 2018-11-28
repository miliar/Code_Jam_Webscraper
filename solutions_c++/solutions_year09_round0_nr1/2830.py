#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main ()
{
	ofstream out;
	out.open("output");
	string dictionary[10000],s;
	int L, D,N, x, currposition, count;
	bool flag, flag2;
	while (cin >> L>>D>>N)
	{
		
		for (int i=0; i<D; i++)
		{
			cin>>dictionary[i];
		}
		for (int j=0; j<N; j++)
		{
			count = 0;
			cin >> s;

			for (int y=0; y<D; y++)
			{
				currposition =0;
				x =0;
				flag = true;
				while(currposition < L && flag)
				{
					if (s[x] == '(')
					{
						flag2= false;
						while (s[x]!= ')' && !flag2)
						{
							if (s[x] == dictionary[y].at(currposition))
								flag2 = true;
							else x++;
						}
						if (!flag2)
							flag = false;
						else
						{
							while (s[x]!= ')')
								x++;
							x++;
							currposition ++;
						}
					}
					else 
					{
						if (dictionary[y].at(currposition)!= s[x])
						{
							flag = false;
						}
						else 
						{
							currposition++;
							x++;
						}
					}
					
				}
				if (flag)
					count++;
			}
			out<<"Case #"<<j+1<<": "<<count<<endl;
		
		}
		
		
	}
	
	return 0;
}