#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <math.h>
#include <stdio.h>
using namespace std;


int main(){
	//freopen("sample.in","r",stdin);
	//freopen("sample.out","w",stdout);
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int N=0,PD=0,PG=0;
		cin>>N>>PD>>PG;
		if ((PG==100 && PD<100) || (PD>0 && PG==0)) {
			cout<<"Case #"<<i+1<<": Broken"<<endl;
		} else {
			bool bok = false;
			for(int j=1;j<=N;j++){
				if (j*PD % 100 == 0) {
					bok = true;
					break;
				}
			}
			if (!bok) {
				cout<<"Case #"<<i+1<<": Broken"<<endl;
			} else {
				cout<<"Case #"<<i+1<<": Possible"<<endl;
			}
		}
	}
	
	
}