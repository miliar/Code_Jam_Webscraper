#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
const int N=102;
int main(){
	char R[N];
	int P[N],C,ccc,i,n,Po,No,T,dT,Pb,Nb;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&C);
	for(ccc=1;ccc<=C;++ccc){
		scanf("%d",&n);
		for(i=0;i<n;++i){
			scanf(" %c %d",R+i,P+i);
		}
		P[n]=1000000;
		Po=Pb=1;
		T=0;
		for(i=0;i<n;++i){
			for(No=i;No<n && R[No]!='O';++No);No=P[No];
			for(Nb=i;Nb<n && R[Nb]!='B';++Nb);Nb=P[Nb];
			if(R[i]=='O'){
				dT=abs(Po-No)+1;Po=No;
				if(abs(Pb-Nb)<=dT)Pb=Nb;
					else Pb+=Nb>Pb? dT:-dT;
				T+=dT;
			}else{
				dT=abs(Pb-Nb)+1;Pb=Nb;
				if(abs(Po-No)<=dT)Po=No;
					else Po+=No>Po? dT:-dT;
				T+=dT;
			}
		}
		printf("Case #%d: %d\n",ccc,T);
	}
	return 0;
}
