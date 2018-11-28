#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;


int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int t=0;
	cin>>t;
	for(int casen=1; casen<=t; casen++){
		int n=0;
		int cur=0;
		int mmin = 1<<30;
		cin>>n;
		int bitmask = 0;
		int sum = 0;
		for(int i=0;i<n;i++){
			cin>>cur;
			sum+=cur;
			bitmask = bitmask ^ cur;
			mmin = min(mmin, cur);
		}
		if(bitmask == 0)
			cout<<"Case #"<<casen<<": "<<sum-mmin<<endl; 
		else
			cout<<"Case #"<<casen<<": NO"<<endl; 
		
		

	}
	
	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}