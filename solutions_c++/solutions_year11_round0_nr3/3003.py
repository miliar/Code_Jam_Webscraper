/*
 * main.cpp
 *
 *  Created on: 2011/5/7
 *      Author: lauer
 */
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ofstream fout("ans");
	int t;
	int n,k,s,r,a;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cin >> n;
		r = a = 0;
		s = 100000000;
		for(int j=0;j<n;j++)
		{
			cin >> k;
			r ^= k;
			if(k<s)
				s = k;
			a+= k;
		}
		if(r!=0)
			fout << "Case #" << i << ": NO" << endl;
		else
			fout << "Case #" << i << ": " << a-s << endl;
	}
}
