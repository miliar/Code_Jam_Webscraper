#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

int mat[105][1005];
int mapa[1005];
int main() {
	int n;
	scanf("%d\n",&n);
	for (int i=1;i<=n;i++) {
		int q,s;
		vector<string> search;
		vector<string> queries;

		scanf("%d\n",&s);
		for (int k=0;k<s;k++) {
			string a="";
			char c=getchar();
			do {
				a+=c;
				c=getchar();
			}
			while (c!='\n');
			search.push_back(a);
		}
		scanf("%d\n",&q);
		for (int k=0;k<q;k++) {
			string a="";
			char c=getchar();
			do {
				a+=c;
				c=getchar();
			}
			while (c!='\n');
			queries.push_back(a);
			for (int l=0;l<s;l++)
				if (queries[k]==search[l]) {
					mapa[k]=l;
					break;
				}
		}


		for (int l=0;l<s;l++)
		for (int k=0;k<q;k++)
			mat[l][k]=(mapa[k]==l)?-1:10000000;

		for (int l=0;l<s;l++)
			if (mat[l][0]>=0)
				mat[l][0]=0;

		int ant=0;
		for (int k=1;k<q;k++) {
			int ant2=10000000;
			for (int l=0;l<s;l++) {
				if (mat[l][k]==-1)
					continue;
				if (mat[l][k]>=0 && mat[l][k-1]>=0)
					mat[l][k]=min(mat[l][k],mat[l][k-1]);
				mat[l][k]=min(mat[l][k],ant+1);
				ant2=min(ant2,mat[l][k]);
			}
			ant=ant2;
		}


		int minimum=10000000;
		for (int l=0;l<s;l++)
			if (mat[l][q-1]>=0)
				minimum=min(minimum,mat[l][q-1]);

		printf("Case #%d: %d\n",i,minimum);
		
	}
	return 0;
}

