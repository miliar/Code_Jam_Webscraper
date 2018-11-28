#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
using namespace std;

int main()
{
	freopen("Dancers.in","r",stdin);
	freopen("Dancers.out","w",stdout);
	
	int test, num, sup, max, total[102], g=0;
	cin >> test;
	for (int k=1; k<=test; k++)
	{
		g=0;
		cin >> num >> sup >> max;
		for (int l=0; l<num; l++)
		{
			cin >> total[l];
		}
		for (int i=0; i<num; i++)
		{
			int b=total[i] % 3, c=total[i]/3, d=c, e=c, f=c;
			if (b==2) {d=d+1; e=e+1;}
			if (b==1) d=d+1;
			if ((b==0 or b==2) and sup>0 and d==max-1 and d!=0 and total[i]!=1) {d=d+1; e=e-1; sup=sup-1;}
			if (d>=max) g=g+1; 
		}
		cout<<"Case #"<<k<<": "<<g<< endl;
	}
	return 0;
}
