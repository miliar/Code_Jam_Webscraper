#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <cstdio>
using namespace std;
int ar[10];
bool bi[3000][3000];
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int a,b,c,d,e,z,i,j,ans,ten,f,g,h;
	scanf("%d",&z);
	for(int t=1;t<=z;t++){
		scanf("%d %d",&i,&j);
		for(a=i;a<=j;a++) for(b=i;b<=j;b++) bi[a][b]=0;
		e=-1; d=i;
		ans=0;
		ten=1;
		while(d>=1){ e++; d=d/10; ten=ten*10; }
		ten=ten/10;
		for(a=i;a<=j;a++){
			f=e; g=ten;
			h=10;
			while(f--){
				d=a%g;
				c=d*h+(a/g); 
				h=h*10; g=g/10;
				if(c>a && c<=j && bi[a][c]==0){ bi[a][c]=1; ans++; }
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;	
	}
	return 0;
}
