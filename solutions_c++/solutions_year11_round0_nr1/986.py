#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<math.h>
#include<string.h>
#include<iostream>

using namespace std;

int main(){
	freopen("BT.in","r",stdin);
    freopen("BT.out","w",stdout);
    int t;
    int count;

	int nseq;
    char robot;
    int k;
    int delta;


    int pos1=1;
    int pos2=1;
    int todwalk=0;
    char lastmove=-1;
    cin>>t;
	for(int z=0;z<t;z++){
        scanf("%d",&nseq);
        count=0;
        pos1=1;pos2=1;
        todwalk=0;
        lastmove=-1;
        for(int i=0;i<nseq;i++){
            cin>>robot;
            cin>>k;
            if(robot=='O'){
                delta=pos1-k;
                pos1=k;
            }else{
                delta=pos2-k;
                pos2=k;
            }
            delta=(delta<0)?-delta:delta;
            if(todwalk==0){
                if(robot=='O'){
                    todwalk=-(delta+1);
                }else{
                    todwalk=delta+1;
                }
                count+=(delta+1);
            }else if(todwalk<0){
                if(robot=='O'){
                    todwalk-=(delta+1);
                    count+=(delta+1);
                }else{
                    todwalk+=(delta+1);
                    if(todwalk>0)
                        count+=todwalk;
                    else{
                        count+=1;
                        todwalk=1;
                    }
                }
            }else{
                if(robot=='O'){
                    todwalk-=(delta+1);
                    if(todwalk<0)
                        count-=todwalk;
                    else{
                        count+=1;
                        todwalk=-1;
                    }
                }else{
                    todwalk+=(delta+1);
                    count+=(delta+1);
                }
            }
            lastmove=robot;
        }
        printf("Case #%d: %d\n",z+1,count);
	}
	return 0;
}
