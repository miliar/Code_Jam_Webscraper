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

vector<vector<int> > a;

vector<int> rozdel_na_int(const string& st, string oddelovac){
	vector<int> vystup(0);
	int odkial, kam;
	odkial=st.find_first_not_of(oddelovac,0);
	while(odkial!=-1){
		kam=st.find_first_of(oddelovac,odkial);
		if (kam==-1) kam=st.size();
		string pom=st.substr(odkial,kam-odkial);
		vystup.push_back(atoi( pom.c_str() ));
		odkial=st.find_first_not_of(oddelovac,kam);
	}
	return vystup;
}

int mult(long long num, int base){
	long long pom=0;
	while (num>0){
		pom += (num % base)*(num % base);
		num/=base;
	}
	if (pom>2000) cout<<"!!!";
	return pom;
}

main(){
	ofstream fout ("A-small.out");
	ifstream fin ("A-small.in");
	map<vector<int>,long long> mapa;
	vector<vector<int> > leads_to(2000,vector<int> (11,0));
	for(long long i=2;i<50000000;i++){
		vector<int> riadok(9,0);
		for(int j=2;j<=10;j++){
			long long num=i;
			if (leads_to[mult(num,j)][j]==1){
				//ok
				riadok[j-2]=1;
				continue;
			}
			if (leads_to[mult(num,j)][j]==2){
				//zle
				continue;
			}
			//nevieme
			vector<int> used (2000,0);
			while(true) {
				num=mult(num,j);
				if (used[num]==1){
					leads_to[mult(i,j)][j]=2;
					break;
				}
				if (num==1) {
					leads_to[mult(i,j)][j]=1;
					riadok[j-2]=1;
					break;
				}
				used[num]=1;
			}
		}
//		a.push_back(riadok);
		if (mapa.find(riadok)==mapa.end()){
			mapa[riadok]=i;
			cout<<i<<": ";
			int kk=0;
			for(int j=0;j<riadok.size();j++){
				kk+=riadok[j];
				cout<<riadok[j]<<" ";
			}
			cout<<endl;
			if (kk==9){
				cout<<i<<"!!!!!!!!!!!!!!!!!!!!!!!!!";
				break;
			}
		}
	}
	
/*	int T;
	fin>>T;
	for(int i=0;i<T;i++){
		string line;
		getline(fin,line);
	}
	fout.close();
*/
}
