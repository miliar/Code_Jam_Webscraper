/*
LANG: C++
TASK: B
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T,N,P,S;
int score[101];

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
	    scanf("%d %d %d",&N,&S,&P);
	    for(int j=0; j<N; j++){
	        scanf("%d",&score[j]);
	    }
	    int cntBoth=0,cntSecondOnly=0,cntFirstOnly=0;
	    for(int j=0; j<N; j++){
	        if(score[j]>=2 && score[j]<=28){
                if((score[j])%3==0){
                    if(score[j]/3>=P){
                        cntBoth++;
                    }
                    else{
                        if((score[j]+3)/3>=P){
                            cntSecondOnly++;
                        }
                    }
                }
                else if((score[j]-1)%3==0){
                    if((score[j]+2)/3>=P){
                        cntBoth++;
                    }
                }
                else{
                    if((score[j]+1)/3>=P){
                        cntBoth++;
                    }
                    else{
                        if((score[j]+4)/3>=P){
                            cntSecondOnly++;
                        }
                    }
                }
	        }
	        else{
	            if((score[j])%3==0){
                    if(score[j]/3>=P){
                        cntFirstOnly++;
                    }
                }
                else if((score[j]-1)%3==0){
                    if((score[j]+2)/3>=P){
                        cntFirstOnly++;
                    }
                }
                else{
                    if((score[j]+1)/3>=P){
                        cntFirstOnly++;
                    }
                }
	        }
	    }
        //cntFirstOnly+cntBoth+cntSecondOnly - okay;
        //
		cout<<"Case #"<<i<<": "<<cntFirstOnly+cntBoth+min(cntSecondOnly,S)<<endl;
	}
	return 0;
}
