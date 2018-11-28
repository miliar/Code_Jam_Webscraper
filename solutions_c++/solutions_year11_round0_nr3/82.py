#include <iostream>
#include<stdio.h>
#include<set>
#include<map>
#include<cstring>
using namespace std;


int main (int argc, char * const argv[]) {
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int caso=1;caso<=t;caso++)
	{
		int n;
		int suma=0;
		int mn=1<<30;
		int o=0;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			int x;
			cin>>x;
			o=o^x;
			suma=suma+x;
			mn=min(mn,x);
		}
		if(o!=0)cout<<"Case #"<<caso<<": NO"<<endl;
		else {
			cout<<"Case #"<<caso<<": "<<suma-mn<<endl;
		}

		
		
	}
    return 0;
}
