#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream f("read2.txt");
	ofstream g("output2.txt");
	int	t,s,n,p,res[101],i,count,j;
	f>>t;
	for(j=0;j<t;j++)
	{
		count=0;
		f>>n;
		f>>s;
		f>>p;
		for(i=0;i<n;i++)
			f>>res[i];
		for(i=0;i<n;i++)
		{
			if(res[i]>=29)
			{
				if(p<=10)count++;
			}
			else if(res[i]==1)
			{
				if(p<=1)count++;
			}
			else if(res[i]==0)
			{
				if(p<=0)count++;
			}
			else
			{
				if(res[i]%3==0)
				{
					if(res[i]/3>=p)count++;
					else if((res[i]/3+1)>=p && s>0)
					{
						count++;s--;
					}
				}
				else if(res[i]%3==1)
				{
					if(res[i]/3+1>=p)count++; // 16=5+5+6 or 6+6+4 13=4+4+5 or 3+5+5
				}
				else
				{
					if(res[i]/3+1>=p)count++;// 14=4+4+6 or 4+5+5
					else if((res[i]/3+2)>=p && s>0)
					{
						count++;s--;
					}
				}
			}
		}
		cout<<"Case #"<<j+1<<": "<<count<<endl;
		g<<"Case #"<<j+1<<": "<<count<<"\n";
	}
	return 0;
}
