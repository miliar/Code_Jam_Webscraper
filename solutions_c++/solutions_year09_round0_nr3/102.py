#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>

using namespace std;

const char* str = "welcome to code jam";
const int Z=10000;

int counts[1024][64];

int main()
{
	int n; cin>>n; cin.ignore();
	string s;
	for(int i=0; i<n; ++i) {
		getline(cin, s);
		memset(counts, 0, sizeof(counts));
		counts[0][0]=1;

		for(int j=0; j<s.size(); ++j) {
			for(int k=0; k<=strlen(str); ++k) {
				counts[j+1][k]=counts[j][k];
//				if (counts[j][k]<0) printf("%d %d %d\n", j, k, counts[j][k]);
				assert(counts[j][k]>=0);
			}
			char c=s[j];
			for(int k=0; str[k]; ++k)
				if (str[k]==c) counts[j+1][k+1] = (counts[j][k+1] + counts[j][k]) % Z;// printf("jee %d %d %d\n", i, j, k);
		}
		printf("Case #%d: %04d\n", i+1, counts[s.size()][strlen(str)]);
	}
}
