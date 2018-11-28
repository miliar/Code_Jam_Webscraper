#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	for (int i=0; i<t; i++){
		int n, l, h;
		cin>>n>>l>>h;
		vector<int> frec;
		for(int j=0; j<n;j++){
			int aux;
			cin>>aux;
			frec.push_back(aux);
		}
		bool toca=0;
		int frecuencia;
		for (int k=l; k<=h; k++){
			for (int j=0; j<n; j++){
				if ((frec[j]%k==0)||(k%frec[j]==0)){
					toca=1;
					frecuencia=k;
				}
				else{
					toca=0;
					break;
				}
			}
			if (toca)
				break;
		}
		if (toca)
			cout<<"Case #"<<i+1<<": "<<frecuencia<<endl;
		else
			cout<<"Case #"<<i+1<<": NO "<<endl;
	}
	return 0;
}

