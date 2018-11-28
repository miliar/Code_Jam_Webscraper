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
		freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
	int cases,caseno=0,i,j,k,result;
	int O[200],B[200],seq[200],button;char color;
	scanf("%d",&cases);
	while(cases--){
	    scanf("%d",&N);
	    j=k=0;
	    memset(seq,-1,sizeof(seq));
	    for(i=0;i<N;i++){
            scanf(" %c %d",&color,&button);
            if(color=='O') O[j++]=button,seq[i]=0;
            else B[k++]=button,seq[i]=1;
	    }
	    int poso=1,posb=1,idleo=0,idleb=0,cnt=0;int diff;
	    j=k=0;
	    for(i=0;i<N;i++){
            if(seq[i]==0){
                if(poso!=O[j]){
                     diff=abs(O[j]-poso),poso=O[j];
					 diff-=idleo;if(diff<0) diff=0,idleo-=diff;
                     cnt+=diff;if(diff>0) idleb+=diff;
                }
                if(poso==O[j]) cnt++,idleb++,j++,idleo=0;
            }
            else{
                if(posb!=B[k]){
                     diff=abs(B[k]-posb),posb=B[k];
					 diff-=idleb;if(diff<0) diff=0,idleb-=diff;
                     cnt+=diff;if(diff>0) idleo+=diff;
                }
                if(posb==B[k]) cnt++,idleo++,k++,idleb=0;
            }
	    }
		printf("Case #%d: %d\n",++caseno,cnt);
	}
	return 0;
}

