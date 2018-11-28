#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
#include <fstream>
using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define lg length
#define sz size
#define forn(i,n) for(i=0;i<n;i++)
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int main () {
	char temp[100];
	int T;
	long long rta;
	ifstream fin("A.in");
	ofstream fout("A.out");
	fin>>T;
	fin.get();
	int i,j;
	for(i=1;i<=T;i++) {
		fout<<"Case #"<<i<<": ";
		int s[200] = {0};
		long long base = 0;
		fin.getline(temp,100,'\n');	
		//cout<<temp<<endl;
		// Cantidad de simboles:
		for(j=0;j<strlen(temp);j++) {
			if(s[temp[j]]==0) {
				base++;
				s[temp[j]] = -1;	
			}	
		}
		if(base==1) base++;
		//cout<<base<<endl;
		long long v[100] = {0};
		// Construir rta:
		v[0] = 1;
		s[temp[0]] = 1; 
		int a = 0;
		for(j=1;j<strlen(temp);j++) {
			if(a==1) a++;
			if(s[temp[j]]==-1) {
				s[temp[j]] = a;
				v[j] = a;
				a++;	
			}
			else {
				v[j] = s[temp[j]];	
			}
		}
		//for(j=0;j<strlen(temp);j++) cout<<v[j]<<" ";
		//cout<<endl;
		// convertir:
		int t = strlen(temp);
		long long r = 1;
		rta = 0;
		for(j=t-1;j>=0;j--) {
			rta += v[j]*r;
			r *= base;
		}
		fout<<rta<<endl;
		//cin.get();
	}

return 0;	
}
