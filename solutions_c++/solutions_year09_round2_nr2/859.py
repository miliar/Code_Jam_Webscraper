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
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int T;
	fin>>T;
	fin.get();
	int j;
	for(int i=1;i<=T;i++) {
		char temp[100];
		fout<<"Case #"<<i<<": ";
		fin.getline(temp,100,'\n');
		// Verificar orden:
		bool flag = true;
		for(j=0;j<strlen(temp)-1 && flag;j++) {
			if(temp[j]<temp[j+1]) flag = false; 		
		}
		// Estan en orden creciente, agrego cero:
		if(flag) {
			int L = strlen(temp);
			for(j=L;j>0;j--) temp[j] = temp[j-1];
			temp[0] = '0';
			temp[L+1] = '\0';
		}
		next_permutation(temp,temp+strlen(temp));
		fout<<temp<<endl;	
	}
	fin.close();
	fout.close();	 
return 0;	
}
