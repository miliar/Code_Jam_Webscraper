#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <cstdio>
#include <vector>
#include <math.h>
#include <list>
#include <map>
using namespace std;

int power10(int n)
{
	static int memo[10]={1};
	if (memo[n]) return memo[n];
	return memo[n]=power10(n-1)*10;
}

int main()
{
	freopen("number.in","r",stdin);
	freopen("number.out","w",stdout);
	
	unordered_set<int>set1;
	int test, a, b, g=0, d, h=0;
	cin >> test;
	for (int k=1; k<=test; k++)
	{
		cin >> a >> b;
		set1.clear();
		g=0;
		for (int p=0; a<=b; a++)
		{
			h=0;
			if (set1.count(a)>0) p=0;
			else
			{
			for (int i=0, j=0; i<=log10(a)+1; i++, j--)
			{
				d=((a-(a%(power10(i+1))))/(power10(i+1)))+((a%(power10(i+1)))*(power10(log10(a)+j)));
				if (d<=b and d>=a and set1.count(d)<1) {h=h+1; set1.insert(d);}
			}
			}
			h=h-1;
			g=g+((h*h+h)/2);	 
		}
		cout<<"Case #"<<k<<": "<<g<< endl;	
	}
	return 0;
}
		
