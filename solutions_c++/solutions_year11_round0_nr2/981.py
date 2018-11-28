
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
    freopen("MK.in","r",stdin);
    freopen("MK.out","w",stdout);

	int t;
	scanf("%d",&t);

	char combine[36][4];
	char oppose[28][3];
	char list[101];
	char answer[100];
	int ncom;
	int nopp;
	int nlist;

	for(int z=0;z<t;z++){
        scanf("%d",&ncom);
        for(int i=0;i<ncom;i++){
            scanf("%s",&combine[i]);
        }
        scanf("%d",&nopp);
        for(int i=0;i<nopp;i++){
            scanf("%s",&oppose[i]);
        }
        scanf("%d",&nlist);
        scanf("%s",&list);

        //PROCESSING PHASE
        int loop = nlist-1;
        bool isFound;
        char op1,op2;
        char opp1,opp2;
        char current,next;
        char com1,com2;
        for(int i=0;i<loop;i++){
            isFound=false;
            current=list[i];
            next=list[i+1];
            for(int j=0;j<ncom;j++){
                com1=combine[j][0];
                com2=combine[j][1];
                if((current==com1&&next==com2)
                ||(current==com2&&next==com1)){
                    list[i++]=combine[j][2];
                    list[i]=0;
                    isFound=true;
                    break;
                }
            }
            if(!isFound){
                for(int j=0;j<nopp;j++){
                    opp1=oppose[j][0];
                    opp2=oppose[j][1];
                    if((current==opp1&&next==opp2)
                    ||(current==opp2&&next==opp1)){
                        list[i++]=0;
                        list[i]=0;
                        isFound=true;
                        for(int p=0;p<i;p++)list[p]=0;
                        break;
                    }
                }
                if(isFound)continue;
            }
            next = list[i+1];
            for(int k=0;k<nopp;k++){
               if(next==oppose[k][0]||next==oppose[k][1]){
                  isFound=true;
                  break;
               }
            }
            if(!isFound)continue;
            for(int j=0;j<i;j++){
                if(list[j]==0)continue;
                isFound=false;
                current = list[j];
                for(int k=0;k<nopp;k++){
                     op1=oppose[k][0];
                     op2=oppose[k][1];
                     if((current==op1&&next==op2)
                     ||(current==op2&&next==op1)){
                        isFound=true;
                        for(int p=0;p<=i+1;p++){
                           list[p]=0;
                        }
                        i++;
                        break;
                     }
                }
            }
        }

        printf("Case #%d: [",z+1);
        //ANSWER
        int a=0;
        for(int i=0;i<nlist;i++){
            if(list[i]!=0)
                answer[a++]=list[i];
        }
        a--;
        for(int i=0;i<a;i++){
            printf("%c, ",answer[i]);
        }
        if(a>=0)printf("%c",answer[a]);
        printf("]\n");
	}
	return 0;
}
