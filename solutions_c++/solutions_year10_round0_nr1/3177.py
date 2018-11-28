#include<cstdio> 
#include<cstdlib> 
#include<cstring> 
#include<cmath> 
#include<iostream> 
#include<sstream> 
#include<string> 
#include<string.h>
#include<algorithm> 
#include<map> 
#include<set> 
#include<vector> 
#include<queue> 

#define ALL(x) (x).begin(),(x).end()
#define FOR(x,a,b) for (int x=a; x<b;++x)
#define CLR(a,b) memset(a,b,sizeof(a)) //rellenar de 0's

using namespace std;

int main(){
	int n;
	cin>>n;
	FOR(i,0,n){
		int f,s;
		cin>>f>>s;
		int pot = 1<<f;
		if ((s+1)%pot==0)
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n",i+1);
	}
}