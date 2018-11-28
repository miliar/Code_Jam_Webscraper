#include <stdio.h>
#include <iostream>
using namespace std;

int res[110];
int re[110];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int N;
	cin>>N;
	for(int k=0;k<N;k++){
		int s,n;
		double p,a;
		cin>>n>>s>>p;
		for(int i=0;i<n;i++){
			res[i]=0;
			cin>>a;
			for(int j=p;j<=10;j++){
				double ar=a-j;
				if (ar>2*j) continue;
				if(ar>=0){
					ar=j-ar/2;
					if (ar>=0&&ar<=1.0) {res[i]=1;break;}
					else {if (s>0&&ar>=0&&ar<=2.0){res[i]=2;break;}
					}
				}
				else break;
			}
		}
		int r=0;
		for(int i=0;i<n;i++){
			if (s>0&&res[i]==2) {r++;s--;}
			else if (res[i]==1) r++;
		}
		cout<<"Case #"<<k+1<<": "<<r<<endl;
	}
	return 0;
}


