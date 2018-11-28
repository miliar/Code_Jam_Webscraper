#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void flow(char **arr, int x, int y, int i , int j, int& a, int& b)
{
	int min=arr[i][j];
	a=i;b=j;
	if(i-1>=0 && arr[i-1][j]<min)
	{
		min=arr[i-1][j];
		a=i-1;b=j;
	}
	if(j-1>=0 && arr[i][j-1]<min)
	{
		min=arr[i][j-1];
		a=i;b=j-1;
	}
	if(j+1<y && arr[i][j+1]<min)
	{
		min=arr[i][j+1];
		a=i;b=j+1;
	}
	if(i+1<x && arr[i+1][j]<min)
	{
		min=arr[i+1][j];
		a=i+1;b=j;
	}
}
void replace(char **arr,int x,int y,char key,char replacement)
{
	for(int i=0;i<x;++i)
	{
		for(int j=0;j<y;++j)
		{
			if(arr[i][j]==key)
				arr[i][j]=replacement;
		}
	}
}
void normelize(char **arr,int x,int y)
{
	char ch='a';
	int totalcount=0;
	int i;
	int j;
	while(totalcount<x*y)
	{
		int count=0;
		for(i=0;i<x;++i)
		{
			for(j=0;j<y;++j)
			{
				if(arr[i][j]==ch)
					count++;
			}
		}
		if(count==0)
		{
			for(i=0;i<x;++i)
			{
				for(j=0;j<y;++j)
				{
					if(arr[i][j]>ch)
						arr[i][j]--;
				}
			}
			ch--;
		}
		totalcount+=count;
		ch++;
	}
}

int main()
{
	int n;
	int x;
	int y;
	int i,j,k;
	int a,b;
	char ch;
	ifstream in;
	ofstream out;
	in.open("B.in");
	out.open("out.txt");
	in>>n;
	for(k=0;k<n;++k)
	{
		in>>x;
		in>>y;
		ch='a';
		char **arr = new char*[x];
		char **arr2 = new char*[x];
		for(i=0;i<x;++i)
		{
			arr[i]=new char[y];
			arr2[i]=new char[y];
			for(j=0;j<y;++j)
			{
				in>>arr[i][j];
				arr2[i][j]=' ';
			}
		}
		
		for(i=0;i<x;++i)
		{
			for(j=0;j<y;++j)
			{
				flow(arr,x,y,i,j,a,b);
				if(arr2[a][b]!=' ')
				{
					if(arr2[i][j]!=' ')
					{
						if(arr2[a][b]<arr2[i][j])
							replace(arr2,x,y,arr2[i][j],arr2[a][b]);
						else if(arr2[a][b]>arr2[i][j])
							replace(arr2,x,y,arr2[a][b],arr2[i][j]);
					}
					arr2[i][j]=arr2[a][b];
				}
				else if(arr2[i][j]!=' ')
				{
					arr2[a][b]=arr2[i][j];
				}
				else
				{
					arr2[a][b]=ch;
					arr2[i][j]=ch;
					ch++;
				}
			}
		}
		normelize(arr2,x,y);
		cout<<"Case #"<<k+1<<":"<<endl;
		out<<"Case #"<<k+1<<":"<<endl;
		for(int i1=0;i1<x;++i1)
		{
			for(int j1=0;j1<y;++j1)
			{
				cout<<arr2[i1][j1]<<" ";
				out<<arr2[i1][j1]<<" ";
			}
			cout<<endl;
			out<<endl;
		
		}
	}

	

	return 0;
}