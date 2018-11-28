#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <queue>
#include <list>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <fstream>
using namespace std;

#define abs(A) (((A)>=0)?(A):(-(A)))
#define present(c,x) (find(c.begin(),c.end(),x) != (c).end())
#define pb push_back
template<class A, class B> A cvt(B x) { stringstream s; s<<x; A r; s>>r; return r; }
typedef long long int64;

int tests;
int n;
int t[50];

int main() {
	ifstream fin("A-large.in");
	FILE *fout=fopen("A-large.out","w");
	fin >> tests;
	for (int test=1;test<=tests;test++) {
		fin >> n;
		for (int i=1;i<=n;i++) {
			t[i]=0;
			string row;
			fin >> row;
			for (int j=0;j<n;j++) {
				if (row[j]=='1') t[i]=j+1;
			}
		}
		int st=0;
		for (int i=1;i<=n;i++) {

			/*for (int k=1;k<=n;k++) {
				printf("%d ",t[k]);
			}
			printf("\n");*/

			int j=i;
			while (j<=n) {
				if (t[j]<=i) break;
				j++;
			}
			while (j>i) {
				t[j]=t[j-1];
				j--;
				st++;
			}
		}

		/*for (int k=1;k<=n;k++) {
			printf("%d ",t[k]);
		}
		printf("\n");*/

		fprintf(fout,"Case #%d: %d\n",test,st);
	}
    return 0;
}
