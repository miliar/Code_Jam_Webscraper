// Problem B. Dancing With the Googlers.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("Input.in");
	ofstream out("Data.txt");
	int T,N,S,p;
	int num,ggs;
	in>>T;
	for(int t=1;t<=T;++t)
	{
		in>>N>>S>>p;
		ggs=0;
		while(N--)
		{
			in>>num;
			if(num>=p)
			{
				if(num%3==0)
				{
					num/=3;
					if(num>=p)
					{
						ggs++;
					}
					else if(S)
					{
						if(num+1==p)
						{
							ggs++;
							S--;
						}
					}
				}
				else if(num%3==2)
				{
					num/=3;
					if(num+1>=p)
					{
						ggs++;
					}
					else if(S)
					{
						if(num+2==p)
						{
							ggs++;
							S--;
						}
					}
				}
				else
				{
					num/=3;
					if(num+1>=p)
					{
						ggs++;
					}
				}
			}
		}
		out<<"Case #"<<t<<": "<<ggs<<endl;
	}
	return 0;
}

