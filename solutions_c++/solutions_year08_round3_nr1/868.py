#include <iostream>
#include <fstream>
#include <string>
using namespace std;


void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("1.txt");
	fout.open("ouput.txt");
	
	int n=0;
	
	fin>>n;
	int count=0,ans;
	
	int p,k,l;
	int *arr;
	int **mob;

	while(count<n)
	{
		ans=0;
		fin>>p;
		fin>>k;
		fin>>l;

		arr=new int [l];
		mob=new int* [k];
		
		for(int q=0;q<k;q++)
			mob[q]=new int [p];

		for(q=0;q<k;q++)
		{
			for(int w=0;w<p;w++)

			mob[q][w]=0;
		}


		for(int i=0;i<l;i++)
			fin>>arr[i];

		for(i=0;i<l;i++)
		{
			for(int j=0;j<i;j++)
			{
				int temp=arr[i];
				if (arr[i]>arr[j])
				{
					arr[i]=arr[j];
					arr[j]=temp;
				}
			}
		}

		i=0;
		int j=0,m=0;
		bool t=false;

		while(i<l)
		{
			m=0;
			t=false;

			while (m<p && !t)
			{
				j=0;
				while(j<k)
				{
					if (mob[j][m]==0)
					{
						mob[j][m]=arr[i];
						t=true;
						break;
					}

					j++;
				}
				m++;
			}
			i++;
		}

		
		for(q=0;q<k;q++)
		{
			for(int w=0;w<p;w++)
				ans+=(mob[q][w]*(w+1));
		}
		
		count++;
		fout<<"Case #"<<count<<": "<<ans<<endl;
	}
		
	fin.close();
	fout.close();
}