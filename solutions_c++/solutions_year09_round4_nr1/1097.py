#include <fstream>
#include <iostream>
using namespace std;



void switchn(int *a,int *b)
{
	int temp=*a;
	*a=*b;
	*b=temp;
}

int main()
{
	ifstream fin("A-large.in",ios::in);
	ofstream fout("output.txt",ios::out);
	int i,j,k;
	int t,n;
	int Matrix[40][40];
	char TempLine[50];
	int a[40],b[40];
	int count;
	fin>>t;
	for(i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		cout<<"Case #"<<i+1<<": ";
		fin>>n;
		count=0;
		fin.get();
		for(j=0;j<n;j++)
		{
			fin.getline(TempLine,50);
			a[j]=0;
			b[j]=j;
			for(k=0;k<n;k++)
			{
				if(TempLine[k]=='1')
				{
					a[j]=k;
					Matrix[j][k]=1;
				}
				else
				{
					Matrix[j][k]=0;
				}
			}
		}
		for(j=0;j<n;j++)
		{
			if(a[b[j]]>j)
			{
				for(k=j+1;k<n;k++)
				{
					if(a[b[k]]<=j)
					{
						break;
					}
				}
				for(;k>j;k--)
				{
					switchn(&b[k],&b[k-1]);
					count++;
				}
			}
		}
		cout<<count<<endl;
		fout<<count<<endl;
		/*
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				cout<<Matrix[j][k];
			}
			cout<<endl;
		}*/
	}
	system("pause");
	return 0;
}