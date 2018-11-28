//ohm shri ganeshay namah
# include <iostream.h>
# include <conio.h>
# include <fstream.h>
#include <stdlib.h>
int cases;
void bubble1(long int arr[], int n)
	{
	int i,j,tmp,tmp1;
	for(i=0;i<n-1;i++)//pass
	for(j=0;j<n-i-1;j++)
	if(arr[j]>arr[j+1])
		{
		tmp=arr[j];
		arr[j]=arr[j+1];
		arr[j+1]=tmp;
		}
	}

void bubble2(long int arr[], int n)
	{
	int i,j,tmp,tmp1;
	for(i=0;i<n-1;i++)//pass
	for(j=0;j<n-i-1;j++)
	if(arr[j]<arr[j+1])
		{
		tmp=arr[j];
		arr[j]=arr[j+1];
		arr[j+1]=tmp;
		}
	}


void main()
	{
	clrscr();
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("output.txt");
	fin.seekg(0);
	fin>>cases;
	cout<<cases<<"\n";
	int count=1,nos;
	long int a[1000],b[1000];
	while(count<=cases)
	{
	fin>>nos;
	for(int i=0;i<nos;i++)
	{fin>>a[i];//cout<<a[i]<<"   ";
	}
	cout<<"\n";
	for(i=0;i<nos;i++)
	{fin>>b[i];//cout<<b[i]<<"  ";
	}
	bubble1(a,nos);
	bubble2(b,nos);
	long int result=0;
	for(i=0;i<nos;i++)
		{result+=a[i]*b[i];}
		cout<<a[i]<<" X "<<b[i]<<" = "<<result<<"\n";
	fout<<"Case #"<<count<<": "<<result<<"\n";
	count++;
	}
	fin.close();
	fout.close();

}

