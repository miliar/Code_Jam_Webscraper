
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

inline int max(int a,int b){
   return(a>b)?a:b;
}

inline int min(int a,int b){
   return(a<b)?a:b;
}

inline int abs(int a){
    return(a<0)?-a:a;
}
//qsort(array,arraysize,sizeof(int),compare);
int compare(const void*a,const void*b){
    return (*(int*)a-*(int*)b);
}
int comp(const void* p1, const void* p2) {
  int* arr1 = (int*)p1;
  int* arr2 = (int*)p2;
  int diff1 = arr1[0] - arr2[0];
  if (diff1) return diff1;
  return arr1[1] - arr2[1];
}

int main(){
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);

	int t;
	scanf("%d",&t);

    int answer;
    int L,T,N,C;
    int series[1000];
    int time[1000];
    for(int z=1;z<=t;z++){
        scanf("%d%d%d%d",&L,&T,&N,&C);
        int maxidx=0;
        for(int i=0;i<C;i++){
            scanf("%d",&series[i]);
            series[i]*=2;
            if(series[maxidx]<series[i]){
                maxidx=i;
            }
        }

        for(int i=0;i<N;i++){
            time[i]=series[i%C];
        }

        int dww = T;
        int sum = 0;
        int boosterfinish=-1;
        int before=0;
        for(int i=0;i<N;i++){
            sum+=time[i];
            if(sum>=dww){
                boosterfinish=i+1;
                before=sum-dww;
                break;
            }
        }
        //printf("bsfh=%d\n",boosterfinish);
        //printf("before=%d\n",before);
        int stmp=N-boosterfinish+1;
        int tmp[stmp];
        tmp[0]=before;
        for(int i=1;i<stmp;i++){
            tmp[i]=time[boosterfinish+i-1];
        }
        qsort(tmp,stmp,sizeof(int),compare);
        answer = T;
        //printf("answer=%d\n",answer);
        int loop=stmp-L;
        for(int i=0;i<loop;i++){
            answer+=tmp[i];
            //printf("in\n");
            //printf("tmp%d\n",tmp[i]);
            //printf("answer=%d\n",answer);
        }
        for(int i=loop;i<stmp;i++){
            answer+=(tmp[i]/2);
            //printf("tmp%d\n",tmp[i]/2);
            //printf("answer=%d\n",answer);
        }
        printf("Case #%d: %d\n",z,answer);
    }
	return 0;
}
