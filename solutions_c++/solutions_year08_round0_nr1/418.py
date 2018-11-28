#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int N;
string S[1000], T[10000];

int main() {
	freopen("cpp1.out","w",stdout);
	ifstream fin("cpp1.in");
	fin>>N;
	int i,j,n,Ns,Nt,mj,cj,cnt=0;
	for(n=1;n<=N;n++) {
		fin>>Ns;
		getline(fin,S[0]);
		for(i=0;i<Ns;i++) {
			getline(fin,S[i]);
		}
		fin>>Nt;
		getline(fin,T[0]);
		for(i=0;i<Nt;i++) {
			getline(fin,T[i]);
		}
		cj = 0;
		cnt = 0;
		while(cj<Nt) {
			mj = cj;
			for(i=0;i<Ns;i++) {
				for(j=cj;j<Nt;j++) {
					if(S[i]==T[j]) {
						break;
					}
				}
				if(j>mj) mj=j;
			}
			cj = mj;
			cnt++;
		}
		if(cnt==0) cnt = 1;
		printf("Case #%d: %d\n",n,cnt-1);
	}
	return 0;
}