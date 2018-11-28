//Bismillahir Rahmanir Rahim




#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	long i,n,ks,j,k,l,m,a[1009],b[1009];
	cin>>ks;
	for(i=0;i<ks;i++)
	{
		cin>>n;
		for(j=0;j<n;j++)
		cin>>a[j]>>b[j];


		int coun=0;
		for(j=0;j<n;j++)
		{
			for(k=j+1;k<n;k++)
			{
				if((a[k]>a[j]&&b[k]<b[j])||(a[k]<a[j]&&b[k]>b[j])){
					coun++;
				}
			}
		}
		printf("Case #%d: ",i+1);
		cout<<coun<<endl;
	}
	return 0;
}