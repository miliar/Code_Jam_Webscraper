#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("in");
ofstream fout("out");

const int SIZE = 2*1000*1000+1;
bool used[SIZE];
int p10[10];

int main() {
	p10[0]=1;
	for(int i=1; i<10; i++)
		p10[i] = p10[i-1]*10;

	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int A,B; fin>>A>>B;
		for(int i=A; i<=B; i++)
			used[i] = false;
		int cnt=0;
		int ndigits=0; int temp=A;
		while(temp>0) {
			ndigits++;
			temp /= 10;
		}
		for(int n=A; n<=B; n++) {
			if(!used[n]) {
				used[n]=true;
				int nnums = 1;
				int m=n;
				for(int i=0; i<ndigits; i++) {
					int next = m%10;
					m = (m/10) + next*p10[ndigits-1];
					if(next>0 && m>=A && m<=B && !used[m]) {
						nnums++;
						used[m]=true;
					}
				}
				cnt += nnums*(nnums-1)/2;
			}
		}
		fout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}

