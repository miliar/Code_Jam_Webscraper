#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int test = 0; test < t; test++)
	{
	//	int arr[40][40];
		int max[40];
		int n; 
		in >> n;
		for(int i=0; i < n; i++)
		{
			max[i]=0;
			for(int j=0; j<n; j++)
			{
				char temp;
				in >> temp;
				if( temp == '1')
					max[i]=j;

			}
		}

		int res=0;
		for(int i=0; i < n; i++)
		{
			if( max[i] > i )
			{
				int j=i+1;

				while( max[j] > i)
				{

					j++;
				}
				for(j; j!=i; j--)
				{
					swap(max[j], max[j-1]);
					res++;
				}

			}
			
		}
		out<<"Case #"<<test+1<<": "<< res << endl;



	}
	return 0;
}