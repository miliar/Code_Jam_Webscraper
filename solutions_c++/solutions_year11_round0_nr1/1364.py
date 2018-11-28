#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <sstream>
#include <cmath>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n;
struct tp{
	int x;
	char c;
}a[200],b[200],c[300];
int na,nb;

int main(){
	int i,j,k,test,cases=0;
	scanf("%d",&test);
	while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		
		scanf("%d",&n);
		na=nb=0;
		foru(i,1,n) {
			scanf(" %c%d",&c[i].c,&c[i].x);
			if (c[i].c=='O') {
				na++;
				a[na]=c[i];
			}
			else {
				nb++;
				b[nb]=c[i];
			}
		}
		int x,y;
		x=y=1;
		int ans=0;
		int s1,s2;
		s1=s2=1;
		foru(i,1,n) {
			//cout<<x<<" "<<y<<endl;
			while (1){
				if (s1<=na && c[i].c==a[s1].c) {
					if (x==a[s1].x) {
						ans++; s1++; 
						if (b[s2].x>y) y++; else
						if (b[s2].x<y) y--;						
						break;
					}
				}else
				if (s2<=nb && c[i].c==b[s2].c) {
					if (y==b[s2].x) {
						ans++; s2++; 
						if (a[s1].x>x) x++;else
						if (a[s1].x<x) x--;
						break;					
					}
				}
				ans++;
				if (a[s1].x>x) x++;else
				if (a[s1].x<x) x--;
				if (b[s2].x>y) y++; else
				if (b[s2].x<y) y--;
			}
		}
		printf("%d\n",ans);
		
	}
}    
