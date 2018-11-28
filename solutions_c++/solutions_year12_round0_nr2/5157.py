#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{
	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");
	int T,N,S,p,t,count,x,y,z;
	in>>T;
	for(int i=0;i<T;i++)
	{
		count=0;
		in>>N;
		in>>S;
		in>>p;
		for(int j=0;j<N;j++)
		{
			in>>t;
			//out<<"total:"<<t<<" ";
			if(p*3<=t)
			{
				//out<<"clear  ";
				count++;
			}
			else 
			{
				x=t-p;
				if(x<=p-2)
				{
					continue;
				}
				else
				{
					y=p-2;
					z=x-y;
					if(z>=p)
					{
						//out<<"y:"<<y<<" z:"<<z<<" ";
						count++;
					}
					if((z==y+1||z==y)&&S!=0)
					{
						//out<<"y:"<<y<<" z:"<<z<<" ";
						S--;count++;
					}
				}
			}
		}
		if(i+1==T)
		{
			out<<"Case #"<<i+1<<": "<<count;
		}
		else
		{
			out<<"Case #"<<i+1<<": "<<count<<endl;
		}
	}
	return 0;
}