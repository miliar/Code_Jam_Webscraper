#include<iostream>
#include<stdio.h>

#define rep(i,n) for(int i=0; i<n; i++)

using namespace std;

int main(){
	int t,teste=1, r, k, n, aux;
	long long int money, soma;
	int fila[1100], somas[1100][2];	
	cin>>t;
	rep(i, t){
		money=0;
		scanf("%d%d%d",&r,&k,&n);
		rep(j,n){
		       	scanf("%d",&fila[j]);
		}
		//Calculo das somas
		rep(j,n){
			somas[j][0]=fila[j];	
			int z=(j+1)%n;
			while((somas[j][0]+fila[z])<=k && z!=j){
				somas[j][0]+=fila[z];
				z=(z+1)%n;
			}
			somas[j][1]=z;
		}
		aux=0; money=0;
		rep(j,r){
			money+=somas[aux][0];
			aux=somas[aux][1];
		}	
		cout<<"Case #"<<teste++<<": "<<money<<endl;
	}
	
}
