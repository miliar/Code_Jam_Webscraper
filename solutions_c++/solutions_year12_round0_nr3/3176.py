//============================================================================
// Name        : Codejam.cpp
// Author      : Guru
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include<stdio.h>
#include<fstream>
#include<math.h>
using namespace std;

int main() {
	int T,b,n,A,B,tot,dig,dig2,m,lim;
	ofstream myfile;
	myfile.open ("example.txt");

	scanf("%d",&T);


	for(b=0;b<T;b++)
	{
		scanf("%d %d",&A,&B);
		tot=0;
		dig=log(A)/log(10)+1;
		printf(" Case #%d: ",b+1);
		myfile << "Case #"<<b+1<<": ";

		for(n=A;n<B;n++)
		{
			dig2=dig;
			dig2--;

			while(dig2>0)
			{
				m=(n%((int)pow(10,dig2)))*(int)pow(10,dig-dig2) + n/(int)pow(10,dig2);
				if(m<=B && m>n)
					tot++;



				dig2--;


			}
		}
		printf("%d\n",tot);
		myfile << tot/2<<"\n";
	}
	myfile.close();
	return 0;
}
