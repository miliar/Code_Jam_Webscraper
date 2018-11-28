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
		cin>>n;
		//vector<int> v(n);
		double d=0.0;
		for(int i=1;i<=n; i++){
			int cur;
			cin>>cur;
			if(i!=cur) d++;
		}
		cout<<"Case #"<<casen<<": "<<d <<endl; 
		//cout<< max(fint[0], fint[1])<<endl;

	}
	//cout<<"-\n";


	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}