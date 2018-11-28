// codejam1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <fstream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	vector<int> V1,V2,V3;
	fstream input,output;
	input.open("C-small-attempt0.in");
	output.open("out.txt");

	int A,B,T,counter=0;
	string S1,S2;
	char charsA[10],charsB[10];

	input>>T;
	getline(input,S1);

	for(int t=0;t<T;t++)
	{
		getline(input,S1,' ');
		getline(input,S2);
		A=0;
		B=0;
		counter=0;

		for(int k=S1.length()-1,n=1;k>-1;k--)
		{
			A+=((int)(S1[k])-48)*n;
			B+=((int)(S2[k])-48)*n;
			n*=10;
		}

		for(int i=A;i<=B;i++)
		{
			V1.clear();
			sprintf(charsA,"%d",i); 

			for(int z=0;z<S1.length();z++)
			{
				V1.push_back((charsA[z]-48));
				V3.resize(S1.length());
			}

			for(int j=i+1;j<=B;j++)
			{
				V2.clear();
				sprintf(charsB,"%d",j); 

				for(int z=0;z<S1.length();z++)
				{
					V2.push_back((charsB[z]-48));
				}

					for(int r=1;r<S1.length();r++)
					{
						V3.clear();
						for(int p=S1.length()-r;p<S1.length();p++)
							V3.push_back(V1[p]);
						for(int p=0;p<S1.length()-r;p++)
							V3.push_back(V1[p]);

						if(V3==V2 && V3[0]!=0)
						{
							counter++;
							break;
						}
					}
			}
		}
		output<<"Case #"<<t+1<<": "<<counter<<endl;
	}

	system("pause");
	return 0;
}

