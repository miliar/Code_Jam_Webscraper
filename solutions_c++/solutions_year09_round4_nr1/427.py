#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;
typedef long long ll;

int n;
char s[41];
int x[41];

main(){

    int T; scanf("%d",&T); for(int test=1;test<=T;test++){

	printf("Case #%d: ",test);

	scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%s",s);
	    x[i]=0;
	    for(int j=0;j<n;j++)
		if(s[j]=='1')
		    x[i]=j;
	}

	int res=0;
	for(int i=0;i<n-1;i++){
	    if(x[i]<=i) continue;
	    for(int j=i+1;j<n;j++)
		if(x[j]<=i){
		    for(int k=j;k>i;k--){
			swap(x[k],x[k-1]);
			res++;
		    }
		    break;
		}
	}
	cout<<res<<endl;
    }
}
