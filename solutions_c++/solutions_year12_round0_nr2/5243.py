#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;
using std::cin;
using std::cout;
using std::endl;

void main()
{
	ifstream test;
	test.open("B-small-attempt7.in");
	ofstream testo;
	testo.open("CaseTest.txt");

	int T,S,p,N,tempi;
	//char tempc;
	//int *tp;
	int count=0;
	int ti[100];
	//tp=ti;
	test>>T;
	for (int Ti=0;Ti<T;Ti++)
	{
		test>>N>>S>>p;
		for (int i=0;i<N;i++)
		{
			test>>ti[i];
		}
		tempi = S;
		for (int i=0;i<N;i++)
		{
			int ping=ti[i] / 3;
			int yu=ti[i] % 3;
			
			if (ping >= p)
			{
				count++;
			}
			else if (yu == 0 && ping != 0 && tempi != 0)
			{
				if ((ping+1) >= p)
				{
					count++;
					tempi--;
				}
			}
			else if (yu ==1)
			{
				if ((ping+1) >= p)
					count++;
			}
			else if (yu == 2 && tempi != 0)
			{
				if ((ping+2) >= p)
				{
					count++;
					tempi--;
				}
			}
			else if (yu == 2)
			{
				if ((ping+1) >= p)
				{
					count++;
				}
			}
		}
		testo<<"Case #"<<(Ti+1)<<": "<<count<<endl;
		count=0;
	}
	testo.close();
	test.close();
	/*
	for (int i=0;i<N;i++)
	{
		
	}*/
}