
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<math.h>
#include<string.h>

using namespace std;



int compare(const void*a,const void*b){
    return (*(int*)a-*(int*)b);
}

int main(){
    freopen("GS.in","r",stdin);
    freopen("GS.out","w",stdout);
	int t;
	scanf("%d",&t);
	int answer=0;
	int num;
	int data[1000];
	int map[1000];
	for(int z=1;z<=t;z++){
	    answer=0;
        scanf("%d",&num);
        for(int i=0;i<num;i++){
            scanf("%d",&data[i]);
            map[i]=data[i];
        }
        qsort(map,num,sizeof(int),compare);
        for(int i=0;i<num;i++){
            if(data[i]!=map[i]){
                answer++;
            }
        }
        printf("Case #%d: %d.000000\n",z,answer);
	}
	return 0;
}
