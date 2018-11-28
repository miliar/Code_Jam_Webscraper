#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <bitset>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#define SZ(A) int(A.size())
#define pb push_back
using namespace std;

int main()
{
	int numCases=0;
	int serialNo=0;
	cin>>numCases;
	while(numCases)
	{
		serialNo++;

		vector <string> vecCharArr;
		vector <string> vecCharArrQueries;
		int S=0,Q=0;

		cin>>S;
		cin.ignore(100,'\n');
		while(S)
		{
			string searchEngine;
			getline(cin,searchEngine);	
			vecCharArr.pb(searchEngine);
			S--;
		}
		cin>>Q;
		cin.ignore(100,'\n');
		while(Q)
		{
			string searchQueries;
			getline(cin,searchQueries);	
			vecCharArrQueries.pb(searchQueries);	
			Q--;
		}

		int i=0,count=0;
		while(i<SZ(vecCharArrQueries))	
		{
			int max=INT_MIN;
			for(int j=0;j<SZ(vecCharArr);j++)
			{
				int k=i;
				while(k<SZ(vecCharArrQueries) && vecCharArr[j] != vecCharArrQueries[k])
				{
					k++;
				}
				if(max<(k-i))
				{
					max = k-i;	
				}
			}	
			i = i+max;
			if(i < SZ(vecCharArrQueries))
			count++;
			
		}
		
		cout<<"Case #"<<serialNo<<": "<<count<<endl;
		numCases--;	
	}
	return 0;
}
