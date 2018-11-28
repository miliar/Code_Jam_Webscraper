#include <iostream>
#include <stdio.h>
using namespace std;

const int LAST=18;
int main()
{
	int smap[LAST+1][500], N, count, len;
	char *tl="welcome to code jam";
	string line;

	//cin>>N;
	getline(cin,line);
	N=atoi(line.c_str());
	for (int t=1; t<=N; t++) {
		getline(cin,line);
		len=line.length();
		memset(smap,0,sizeof(smap));
		for (int n=0; n<len; n++) if (line[n]==tl[0]) smap[0][n]++;
		for (int c=1; c<=LAST; c++) {
			for (int n=0; n<len; n++) {
				if (line[n]==tl[c]) {
					for (int m=0; m<n; m++) smap[c][n]+=smap[c-1][m];
				}
			}
		}			
		count=0;
		for (int n=0; n<len; n++) count+=smap[LAST][n];
		printf("Case #%d: %04d\n",t,count%10000);
	}
	return 0;
}

