#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int totalcases;
	int P,K,L;

	int res=0;
	int kint=1;
	int temp;

	ifstream file;
	ofstream file1;
	file.open("A-small-attempt0.in");
	file1.open("output.txt");

	file>>totalcases;

	for(int t=0;t<totalcases;t++)
	{
		file>>P;
		file>>K;
		file>>L;

		int *arr1=new int[L];

		for(int i=0;i<L;i++)
		{
			file>>arr1[i];
		}

		for(int j=0;j<L;j++)
		{
			for(int k=j+1;k<L;k++)
			{
				if(arr1[k]>arr1[j])
				{
					swap(arr1[k],arr1[j]);
				}
			}
		}

		temp=K;

		for(int l=0;l<L;l++)
		{
			if(l<temp)
			{
				res=res+(arr1[l]*kint);
			}
			else
			{
				temp=temp+K;
				kint++;
				res=res+(arr1[l]*kint);
			}
		}

		file1<<"Case #"<<t+1<<": "<<res<<endl;
		res=0;
		kint=1;

	}

	return 0;
}