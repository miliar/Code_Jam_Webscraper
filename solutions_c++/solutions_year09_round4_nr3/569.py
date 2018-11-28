#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define INF 1000000

int n,k;
long long precios[20][32];
int tabla[20][20];
int puedo[1<<16];

int minim[1<<16];

int calc(int mask){
	int &rta=minim[mask];
	if (rta!=-1) return rta;
	if (puedo[mask]) return rta=1;
	int nmask=(mask-1)&mask;
	
	rta=INF;
	while (nmask>0){
		if (puedo[nmask]){
			rta=min(rta,1+calc(mask-nmask));
			//cout<<mask<<" "<<nmask<<" "<<rta<<endl;
		}
		nmask=(nmask-1)&mask;
	}
	return rta;
}

int main(){
	int i,j,casos,c,h;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cin>>n>>k;
		
		for (i=0;i<n;i++) for (j=0;j<k;j++){
			cin>>precios[i][j];
		}
		
		for (i=0;i<n;i++) tabla[i][i]=true;
		for (i=0;i<n;i++) for (j=i+1;j<n;j++){
			tabla[i][j]=tabla[j][i]=true;
			for (h=0;h+1<k;h++) if ((precios[i][h]-precios[j][h])*(precios[i][h+1]-precios[j][h+1])<=0LL){
				tabla[i][j]=tabla[j][i]=false;
				break;
			}
			//cout<<tabla[i][j]<<" "<<i<<" "<<j<<endl;
		}
		//for (i=0;i<n;i++){ for (j=0;j<n;j++) cout<<tabla[i][j]<<" "; cout<<endl; }
		int mask;
		for (mask=0;mask<(1<<n);mask++){
			if (bits(mask)<1) puedo[mask]=true;
			else{
				puedo[mask]=true;
				for (i=0;i<n;i++) if (mask&(1<<i)){
					for (j=0;j<n && puedo[mask];j++) if (mask&(1<<j)){
						if (!tabla[i][j]){
							puedo[mask]=false;
						}
					}
					if (!puedo[mask-(1<<i)]) puedo[mask]=false;
					break;
				}
			}
			//if (puedo[mask]) cout<<mask<<endl;
		}
		memset(minim,-1,sizeof(minim));
		cout<<"Case #"<<(c+1)<<": ";
		cout<<calc((1<<n)-1)<<endl;
	}
	
	return 0;
}
