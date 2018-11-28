#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
void putlast(int arr[], int len)
{
	int temp = arr[0];
	for(int i=0;i<len-1;i++)
	{
		arr[i]=arr[i+1];
	}
	arr[len-1]=temp;
}
void main()
{
	int t,r,k,n;
	int sum=0;
	int pple=0;
	ifstream input;
	ofstream output;
	input.open ("C-small-attempt0.in");
	output.open ("output.txt");
	input>>t;

	for(int i=1;i<=t;i++)
	{
		input>>r>>k>>n;
		pple=0;
		int* g=new int[n];

		for(int j=0;j<n;j++)
			input>>g[j];

		for(int z=0;z<r;z++)
		{
			for(int m=0;m<n;m++)
				if(pple+g[0]<=k)
				{
					pple+=g[0];
					sum+=g[0];
					putlast(g,n);
				}
				else
				{
					pple=0;
					break;
				}
			pple=0;
		}

		output << "Case #" << i << ": " << sum << endl;
		sum=0;
	}
	input.close();
	output.close();
}