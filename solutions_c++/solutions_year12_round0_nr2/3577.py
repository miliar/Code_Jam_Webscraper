
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <math.h>
#include <cstring>

using namespace std;



int
main()
{  
	int n;
	ofstream fout("3ton.out");
    ifstream fin("ton.in");
	fin>>n;
	string qw[n];
	string qw1[n];
	cout<< n;
	string na;
	
	getline (fin,na);

	for (int i=0;i<n;i++){
		int n1,s,q;
		int ans=0;
		fin>>n1;
		fin>>s;
		fin>>q;
		cout<< n1<<s<<q<<endl;
		int d[n1];
		for (int j=0; j<n1;j++){
			fin>>d[j];
			cout<<d[j];

			if (d[j]>q*3-3){
				d[j]=-23;
				ans++;
			}
			else if (s>0&&q==1){
				if (d[j]>0){
					s--;
					ans++;
					cout<<"SDFDS"<<d[j]<<endl;
				}
			
			}
			else if (s>0&&q==2){
				if (d[j]>1){
					s--;
					ans++;
					cout<<"SDFDS"<<d[j]<<endl;
				}
			}
			else if (s>0){
				if (d[j]>q*3-5){
					s--;
					ans++;
					cout<<"SDFDS"<<d[j]<<endl;
				}
			}
		}

	fout<<"Case #"<<i+1<<": "<<ans<<endl;	
	}
	

	

  //  system("Pause");
	cout<<0<<endl;
    return 0;
}


