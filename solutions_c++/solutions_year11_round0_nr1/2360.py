
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back

using namespace std;

int main(){
	int i,j,k,l,m,T,n,x,y,z,po,pb;
	char c;
	scanf("%d",&T);
	for(int p=1;p<=T;p++){
		printf("Case #%d: ",p);
		scanf("%d",&n);
		k=l=0;
		z=0;
		po=pb=1;
		for(i=0;i<n;i++){
			scanf(" %c %d",&c, &x);
			if(c=='B'){
				j = z-k;
				if(po<x){
					po = (po+j<x)?(po+j):x;
					z+=x-po;
				}
				else if(po>x){
					po = (po-j>x)?(po-j):x;
					z+=po-x;
				}
				z++;
				k=z;
				po=x;
			}
			else{
				j = z-l;
				if(pb<x){
					pb = (pb+j<x)?(pb+j):x;
					z+=x-pb;
				}
				else if(pb>x){
					pb = (pb-j>x)?(pb-j):x;
					z+=pb-x;
				}
				z++;
				l=z;
				pb=x;
			}
			//printf("%d$$ o%d b%d\n",z,k,l);
		}
		printf("%d\n",z);
	}
	return 0;
}
