#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T;
	in>>T;
	for(int i=0;i<T;i++)
	{
		int N,S,p;
		in>>N>>S>>p;
		int nComply=0,nMayComply=0;
		for(int j=0;j<N;j++)
		{
			int t;
			in>>t;
			int t1 = t/3;
			if(t1 >= p)
			{
				nComply++;
			}
			else
			{
				switch(t%3)
				{
					case 0:
						if((t1) && ((t1+1) == p))
						{
							nMayComply++;
						}
						break;
					case 1:
						if((t1+1) == p)
						{
							nComply++;
						}
						break;
					case 2:
						if((t1+1) == p)
						{
							nComply++;
						}
						else if((t1+2) == p)
						{
							nMayComply++;
						}
						break;
					default:
						cout<<"??????"<<endl;
				}
			}
		}
		nMayComply = min(nMayComply,S);
		out<<"Case #"<<i+1<<": "<<nMayComply+nComply<<endl;
	}
}
