#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <cmath>

using namespace std;
#define  MAX 10005

bool isPrim(int a,int b)
{
	if(a%b==0 || b%a==0)
		return true;
	else return false;
}
int main()
{
	ifstream cin("e:\\c.in");
	ofstream cout("e:\\c.out");
	
	int T;
	cin>>T;
	int i,j,k;
	for (i=0;i<T;i++)
	{
		int N,L,H;
		cin>>N>>L>>H;
		int freqs[MAX];
		
		for (j=0;j<N;j++)
		{
			cin>>freqs[j];
		}
		bool ok=true;
		for (j=L;j<=H;j++)
		{
			ok=true;
			for (k=0;k<N;k++)
			{
				if(!isPrim(j,freqs[k]))
				{
					ok=false;
					break;
				}
			}
			if (ok)
			{
				cout<<"Case #"<<(i+1)<<": "<<j<<endl;
				break;
			}
		}
		if(!ok)
			cout<<"Case #"<<(i+1)<<": NO"<<endl;
	}
	return 0;
}