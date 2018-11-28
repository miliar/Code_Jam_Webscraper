
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back

using namespace std;

int main(){
	int i,j,k,l,m,n,T,c;
	scanf("%d",&T);
	for(int p=1;p<=T;p++){
		scanf("%d",&n);
		k=0;c=1000000000;
		l=0;
		for(i=0;i<n;i++){
			scanf("%d",&m);
			if(m<c)
				c=m;
			l+=m;
			k= k^m;
		}
		printf("Case #%d: ",p);
		if(k!=0)
			printf("NO\n");
		else
			printf("%d\n",l-c);
	}
	return 0;
}
