#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <queue>
using namespace std;

fstream fin("A-small-attempt0.in.txt",ios::in);
fstream fout("A-small-attempt0.out.txt",ios::out);

int main() {
	int caseNum, caseNo;
	fin>>caseNum;
	for (caseNo=1; caseNo<=caseNum; caseNo++) {
		fout<<"Case #"<<caseNo<<": ";
		//add code here
		int p,k,L;
		int freq[1100];
		int i,j;
		fin>>p>>k>>L;
		for(i=0; i<L; i++)
			fin>>freq[i];
		sort(freq,freq+L,greater<int>());
		int res = 0;
		for (i=0; i<p; i++) {
			for (j=0; j<k && i*k+j<L; j++) {
				res += (i+1)*freq[i*k+j];
			}
		}
		if ( freq[0] == freq[L-1] )
			fout<<"Impossible"<<endl;
		else fout<<res<<endl;
	}
	return 0;
}