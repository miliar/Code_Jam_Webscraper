 #include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;

char s[50][50];


int ans;
int a[50];



void work(){
	int i,j,k;
	int ans=0;
	foru(i,1,n) {
		k=0;
		foru(j,i,n) if (a[j]<=i) {
			k=j;
			break;
		}
		while (k!=i) {
			swap(a[k],a[k-1]);
			k--;
			ans++;
		}
	}	
	printf("%d\n",ans);
	
	
}


int main(){
    freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases;
	scanf("%d",&test);
	cases=0;
    while (test){
		test--;
		cases++;
		scanf("%d",&n);
		printf("Case #%d: ",cases);
		rep(i,n) scanf("%s",s[i]);
		
		rep(i,n) {
			k=0;
			rep(j,n) if (s[i][j]=='1') k=j+1;
			a[i+1]=k;
		}
		work();
		//printf("%d\n",ans);
		
		
		
	}
    return 0;
}
    
