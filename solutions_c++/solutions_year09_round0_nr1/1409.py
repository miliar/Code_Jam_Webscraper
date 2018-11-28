#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
using namespace std;

main(){
	ofstream fout ("A-small.out");
	ifstream fin ("A-small.in");
	int L,D,N;
	fin>>L>>D>>N;
	vector<string> a;
	for(int i=0;i<D;i++){
		string pom;
		fin>>pom;
		a.push_back(pom);
	}
	for(int i=0;i<N;i++){
		string s;
		fin>>s;
		vector<vector<int> > b(L);
		int akt=0;
		int pocet_ok=0;
		for(int k=0;k<L;k++){
			if (s[akt]=='('){
				akt++;
				while (s[akt]!=')'){
					b[k].push_back(s[akt]);
					akt++;
				}
			}
			else{
				b[k].push_back(s[akt]);
			}
			akt++; //zatvorku i pripadne pismeno
		}
		//pre kazde slovo
		for(int j=0;j<a.size();j++){
			for(int k=0;k<L;k++){
				bool ok=false;
				for(int l=0;l<b[k].size();l++){
					if (b[k][l]==a[j][k]){
						ok=true;
					}
				}
				if (!ok){
					pocet_ok--;
					break;
				}
			}
			pocet_ok++;
		}
		fout<<"Case #"<<i+1<<": "<<pocet_ok<<endl;
	}
	fout.close();
}
