#include<iostream>
#include<string>
#include<fstream>
using namespace std;
void main()
{
	ifstream fin("B-large.in");
	ofstream fout("o2.txt");
	int cases;
	fin>>cases;
	for(int c=1;c<=cases;c++)
	{
	int n,s,p;
	fin>>n>>s>>p;
	int *a=new int[n*5];
	int score;
	for(int i=0;i<n;i++)
	{
		fin>>score;
		a[i*5+0]=a[i*5+1]=a[i*5+2]=score/3;
		a[i*5+3]=score%3;
		a[i*5+4]=score%3;
	}
	int temp=s,count=0;
	for(int i=0;i<n;i++)
	{
		if(a[i*5+3]==2)
		{
			if(temp>0 && a[i*5+0]<9 && a[i*5+0]==p-2)
			{
				a[i*5+0]+=2;
				temp--;
			}
			else
			{
				a[i*5+0]++;
				a[i*5+1]++;
			}
		    a[i*5+3]=0;
		}
		if(a[i*5+3]==1)
		{
			a[i*5+0]++;
		    a[i*5+3]=0;
		}
		if(a[i*5+0]>=p || a[i*5+1]>=p || a[i*5+2]>=p)
			count++;
	}
	if(temp!=0)
	{
		for(int i=0;i<n;i++)
		{
			if(a[i*5+4]==0 && a[i*5+0]==p-1 && a[i*5+0]>0)
			{
					a[i*5+0]++;
					a[i*5+1]--;
					temp--;
					count++;
					if(temp==0)
						break;
				
			}
		}
	}
	fout<<"Case #"<<c<<": "<<count<<"\n";
    }
	fout.close();
	fin.close();

}