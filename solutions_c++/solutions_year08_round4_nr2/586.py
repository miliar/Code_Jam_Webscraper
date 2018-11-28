#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>

using namespace std;

int n,m;
double A;
int check ,savei ,savej ,stat;

void calc(void) {
	int i,j;
	for(i=1;i<=n;i++) {
		for(j=1;j<=m;j++) {
			
			if(A == 0.5 * (double)i * (double)j) {
				check = 1;
				savei = i;
				savej = j;
				return;
			}
		}
	}
}

int main(int argc, char *argv[])
{
	int x,ncase;
	scanf("%d",&ncase);
	for(x=1;x<=ncase;x++) {
		check = 0;
		scanf("%d%d%lf",&n,&m,&A);
		A /= 2;
		calc();

		printf("%d\n",check);
		
		/*if(!check) {
			swap(n,m);
			calc();
		}*/
	}
	return 0;
}
