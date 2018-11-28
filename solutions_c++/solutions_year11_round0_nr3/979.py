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
    freopen("CD.in","r",stdin);
    freopen("CD.out","w",stdout);
	int t;
	scanf("%d",&t);

    int candy;
    int value[1000];
    int answer;

	for(int z=1;z<=t;z++){
        answer=0;

        scanf("%d",&candy);
        for(int i=0;i<candy;i++){
            scanf("%d",&value[i]);
        }
        qsort(value,candy,sizeof(int),compare);
        int tmp=value[0];
        answer=0;
        for(int i=1;i<candy;i++){
            tmp^=value[i];
            answer+=value[i];
        }
        if(tmp==0)
            printf("Case #%d: %d\n",z,answer);
        else
            printf("Case #%d: NO\n",z);
	}
	return 0;
}
