// dummy.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdlib.h>
#include <fstream>
#include <stack>
#include <vector>

using namespace std;

int main()
{
	
	ifstream in("A-small.in");
	ofstream out("A-small.out");
	int ncases=0;

	in >> ncases;

	for(int i=0; i<ncases; i++)
	{
		int n=0,k=0;

		in >> n;

		int *a=new int[n];
		int *b=new int[n];
		

		for(int i=0; i<n; i++)
		{
			in >> a[i] >> b[i];
		}



		int TheAnswer=0;

		for(int i=0; i<n;i++)
			for(int j=1; j<n; j++)
			{
				int egim1=a[i]-b[i];
				int egim2=a[j]-b[j];
				float fark=a[i]-a[j];
				float res=fark/(egim1-egim2);
				
				if(res>0 && res < 1)
					TheAnswer++;

			}

			out << "Case #" << (i+1) <<": " << TheAnswer << endl;
	}
	
	return 0;
}

