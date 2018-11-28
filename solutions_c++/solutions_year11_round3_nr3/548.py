
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
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);

	int t;
	scanf("%d",&t);
    int N,L,H;
    int note[10000];
    int answer;
    for(int z=1;z<=t;z++){
        answer=-1;
        scanf("%d%d%d",&N,&L,&H);

        for(int i=0;i<N;i++){
            scanf("%d",&note[i]);
        }
        for(int i=L;i<=H;i++){
            bool status=true;
            for(int j=0;j<N;j++){
                if(note[j]%i!=0&&i%note[j]!=0){
                    status=false;
                    break;
                }
            }
            if(status==true){
                answer=i;
                break;
            }
        }


        printf("Case #%d: ",z);
        if(answer>0)printf("%d\n",answer);
        else printf("NO\n");
    }
	return 0;
}
