#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <time.h>

using namespace std;

long long s[21];
long long i,j,k,l,m,n,t,w;
long long r[10000];

int main(){
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (int ii=1;ii<=t;ii++){
		cout<<"Case #"<<ii<<": ";
		srand ( time(NULL) );
		cin>>n>>w>>l;
		for (i=0;i<n;i++)
			cin>>r[i];
		long long rw = (long long) sqrt(1.0*w);
		long long lw = (long long) sqrt(1.0*l);
		long long ansx[1000], ansy[1000];
		ansx[0]=0;
		ansy[0]=0;
		for (i=1;i<n;i++){
			int d=1;
			while(d){
				ansx[i]=(rand()%rw)*rw+rand()%rw;
				ansy[i]=(rand()%lw)*lw+rand()%lw;
				int dd=1;
				for (j=0;j<i;j++)
					if ((ansx[i]-ansx[j])*(ansx[i]-ansx[j])+(ansy[i]-ansy[j])*(ansy[i]-ansy[j])<(r[i]+r[j])*(r[i]+r[j])){
						dd=0;
						break;
					}
				if (dd) break;
			}
		}
		for (i=0;i<n;i++)
			cout<<ansx[i]<<' '<<ansy[i]<<' ';
		cout<<endl;
	}
	return 0;
}