#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<stack>
#include<queue>
#include<string>
#include<cstring>


#define PR(x) printf("")
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define READ(x) scanf("%d",&x)
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
using namespace std;
int main() { 
int t;
int arr[100];
scanf("%d",&t);
for(int x=0;x<t;x++){
int n,s,e;
scanf("%d %d %d",&n,&s,&e);
int cnt=0;
for(int i=0;i<n;i++)
{

scanf("%d",&arr[i]);
if(arr[i]<e) continue;
int avg=arr[i]/3;
if(avg>=e) {
PR(arr[i]);
//printf("Straight average count %d \n",arr[i]);
cnt++;
continue;
}
bool fnd=false;
int min=avg-1;
for(;min<=avg+1;min++) {
		for(int toadd=0;toadd<=1;toadd++){
			int sec=min+toadd;
		for(int toA=0;toA<=1;toA++) { 
		int th=min+toA;
		//if(th>arr[i]) break;
		if(th+min+sec==arr[i]) {
		if(min>=e||sec>=e||th>=e)
		{cnt++;fnd=true;break;}
		
		}
		
		}	
		if(fnd) break;
		}
	if(fnd) break;
	}
if(fnd==true) continue;
if(!s) continue;
fnd=false;
min=avg-2;
for(;min<=avg+2;min++) {
		for(int toadd=0;toadd<=2;toadd++){
			int sec=min+toadd;
		for(int toA=0;toA<=2;toA++) { 
		int th=min+toA;
		//if(th>arr[i]) break;
		if(min+sec+th==arr[i]) {
		if(min>=e||sec>=e||th>=e)
		{cnt++;fnd=true;s--;break;}
		}
		}	
		if(fnd) break;
		}
	if(fnd) break;
	}
	}
printf("Case #%d: %d\n",x+1,cnt);

}
}
