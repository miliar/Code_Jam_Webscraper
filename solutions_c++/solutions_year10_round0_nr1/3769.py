#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <vector>

using namespace std;

int test,n,k;

int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	int i;
	scanf("%d",&test);
	for (i=1;i<=test;i++){
		scanf("%d%d",&n,&k);
		if ((k+1)%(1<<n)==0) printf("Case #%d: ON\n",i); else
			printf("Case #%d: OFF\n",i); 
	}
}
