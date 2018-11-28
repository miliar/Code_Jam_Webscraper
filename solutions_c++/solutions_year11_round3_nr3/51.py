#include <cstdio>
#include <iostream>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;
int tc = 1;
int T,N,M;
int x[200000];
int L,H;
int main() {
	freopen("C.txt","w",stdout);
	freopen("Cin.txt","r",stdin);
	
scanf("%d",&T);
while (T--){
	scanf("%d%d%d",&N,&L,&H);
	for (int i=0;i<N;i++)
	scanf("%d",&x[i]);
	
	int res = -1;
	
	for (int i=L;i<=H;i++) {
		bool val = 1;
		for (int j=0;val && j<N;j++) {
			if (x[j]%i!=0 && i%x[j]!=0) val = 0;
			}
		if (val) 
		{
			res = i;
			break;
		}
		}
	
	printf("Case #%d: ",tc++);
	if (res!=-1) {
		printf("%d\n",res);
		}
	else printf("NO\n");
	}
}
