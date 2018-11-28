
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include<map>

using namespace std;



int main () {
	int t;
	int n, s,p;
	int g[200];
	int sa, total;
	cin>>t;
	for(int k=0;k<t;k++){
		cout<<"Case #"<<k+1<<": ";
		cin>>n>>s>>p;
		sa=0;total=0;
		for(int i=0;i<n;i++){
			cin>>g[i];
			//cout<<g[i]<<"w";
			if(g[i]/3>=p||(g[i]/3+1==p&&g[i]%3==2)||(g[i]/3+1==p&&g[i]%3==1)){
				total++;
				//cout<<"-"<<g[i]<<"-\n";
			}else if((g[i]/3+2==p&&g[i]%3==2)||(g[i]/3+1==p&&g[i]%3==0&&g[i]!=0)){
				sa++;
				if(sa<=s)total++;
			//	cout<<"x"<<g[i]<<"x\n";
			}
		}
		cout<<total<<'\n';
	}

	return 0;
}
