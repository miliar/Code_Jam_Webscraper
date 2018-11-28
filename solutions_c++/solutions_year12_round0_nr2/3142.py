#include<cstdio>
#include<iostream>
#include<cmath>
#include<fstream>
#include<string>
using namespace std;

int max(int c[100])
{
	int max=0;
	for(int i=0;i<100;i++)
	{
		(c[i]>max)?max=c[i]:max;
	}
	return max;
}
int main()
{
	int t,n,s,p,n_cases=0,s_cases=0,both_cases=0,output,j;
	int c[100],x[100],y[100];
	bool s_poss;
	ifstream infile ("test small.txt");
	ofstream outfile;
	outfile.open("output test.txt");
	infile>>t;
	for(int i=0;i<t;i++)
	{
		n_cases=0,s_cases=0,both_cases=0;
		infile>>n>>s>>p;
		for(j=0;j<n;j++)
		{
			infile>>c[j];
			x[j]=c[j]/3;
			y[j]=c[j]%3;
			switch (y[j])
			{
			case 0:
				{
					if(x[j]>=p)
					{
						if(x[j]+1>=p && x[j]<10 && x[j]>0)
						{
							both_cases++;
						}
						else
						{
							n_cases++;
						}
						break;
					}
					if(x[j]+1>=p && x[j]<10 && x[j]>0)
					{
						s_cases++;
						break;
					}
					break;
				}
			case 1:
				{
					if(x[j]+1>=p)
					{
						if(x[j]+1>=p && x[j]<10 && x[j]>0)
						{
							both_cases++;
						}
						else 
						{
							n_cases++;
						}
						break;
					}
					if(x[j]+1>=p && x[j]<10 && x[j]>0)
					{
						s_cases++;
						break;
					}
					break;
				}
			case 2:
				{
					if(x[j]+1>=p)
					{
						if(x[j]+2>=p && x[j]<9)
						{
							both_cases++;
						}
						else
						{
							n_cases++;
						}
						break;
					}
					if(x[j]+2>=p && x[j]<9)
					{
						s_cases++;
						break;
					}
					break;
				}
			}
		}
		if(s_cases>=s)
		{
			output=n_cases+both_cases+s;
		}

		else if(s>s_cases)
		{
			output=n_cases+both_cases+s_cases;
		}
		outfile<<"Case #"<<i+1<<": "<<output<<endl;
	}
	return 0;
}
