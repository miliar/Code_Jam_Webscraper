/*	Author       :	Muntasir Muzahid Chowdhury
	Problem Name :
	Algorithm    :
	Complexity   :	*/

//HEADERFILE
#include<iostream>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<ctime>
#include<cassert>
#include<string>
#include<algorithm>

using namespace std;

int N;

int main(){
		//freopen("B-large.in","r",stdin);
		//freopen("B-large.out","w",stdout);
	int cases,caseno=0,i,j,k,r;
	int comb[28][28],opp[28][28],C,D;
	char a,b,c,ar[200];
	scanf("%d",&cases);
	while(cases--){
		memset(comb,0,sizeof(comb));memset(opp,0,sizeof(opp));
	    scanf("%d",&C);
		for(i=0;i<C;i++){
			scanf(" %c %c %c",&a,&b,&c);
			comb[a-64][b-64]=comb[b-64][a-64]=c-64;
		}
		scanf("%d",&D);
		for(i=0;i<D;i++){ 
			scanf(" %c %c",&a,&b);
			opp[a-64][b-64]=opp[b-64][a-64]=1;
		}
		scanf("%d ",&N);
		for(i=0,j=0;i<N;i++){
			scanf("%c",&ar[j]);
			if(j!=0){
				if(comb[ar[j]-64][ar[j-1]-64]>0) ar[j-1]=comb[ar[j]-64][ar[j-1]-64]+64;
				else{
					r=0;
					for(k=0;k<j;k++){
						if(opp[ar[k]-64][ar[j]-64]>0) {j=0;r=1;break;}
					}
					if(r==0) j++;
				}
			}
			else j++;
		}
		printf("Case #%d: [",++caseno);
		if(j>0) printf("%c",ar[0]);
		for(k=1;k<j;k++) printf(", %c",ar[k]);
		printf("]\n");
	}
	return 0;
}

