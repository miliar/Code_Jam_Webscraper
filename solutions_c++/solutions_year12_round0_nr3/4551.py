#include <fstream>
#include <sstream>
#include <string.h>
using namespace std;

class pars {
	public:
	pars(){
		total = 0;
	}
	bool equals(string n1, string m1, string n2, string m2){
		return ((n1 == n2 && m1 == m2) || (n1 == m2 && m1 == n2));
	}
	bool exists(string n, string m){
		for(unsigned int i=0;i<total;i++){
			if(equals(ps[i][0],ps[i][1],n,m)){
				return true;
			}
		}
		return false;
	}
	bool add(string n, string m){
		if(!exists(n,m)){
			ps[total][0]=n;
			ps[total][1]=m;
		} else {
			return false;
		}
		total++;
		return true;
	}
	private:
	unsigned int total;
	string ps[100000][2];
};

int main(){
	ifstream fin("C-small-attempt0.in");
	ofstream fout("gcj2.out");
	
	string sn,sm;
	unsigned int i,j,ncases,A,B,n,m,ndigs,total;
	fin >> ncases;
	for(i=0;i<ncases;i++){
		pars spars = pars();
		total = 0;
		fout << "Case #" << i+1 << ": ";
		fin >> A;
		fin >> B;
		if(B>9){
			m=A+1;
			for(n=A;n<m;n++){
				ostringstream auxsn;
				auxsn << n;
				sn = auxsn.str();
				ndigs=sn.size();
				string mapa[ndigs];
				for(j=1;j<ndigs;j++){
					char sc[10];
					strcpy(sc,sn.substr(ndigs-j,j).c_str());
					strcat(sc,sn.substr(0,ndigs-j).c_str());
					mapa[j-1]=sc;
				}
				for(m=n+1;m<=B;m++){
					ostringstream auxsm;
					auxsm << m;
					sm = auxsm.str();
					for(j=1;j<ndigs;j++){
						if((strcmp(mapa[j-1].c_str(),sm.c_str()) == 0) && (spars.add(sn,sm))){
							total++;
						}
					}
				}
			}
		}
		fout << total << endl;
	}
	
	return 0;
}
