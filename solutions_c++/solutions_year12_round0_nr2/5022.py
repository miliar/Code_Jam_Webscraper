#include<stdio.h>
#include <algorithm>
using namespace std;

int main(){
    int nCase,round,i,Count,nGoogler,nSurprise,MinPoint,Point;
    int MinerPoint,MinestPoint;
    scanf("%d",&nCase);
    for(round=0;round<nCase;round++){
        scanf("%d %d %d",&nGoogler,&nSurprise,&MinPoint);
        Count=0;
        MinerPoint=max(MinPoint-1,0);
        MinestPoint=max(MinPoint-2,0);
        for(i=0;i<nGoogler;i++){
            scanf("%d",&Point);
            if(Point >= MinPoint+MinerPoint+MinerPoint){
                Count++;
            }
            else if((Point >= MinPoint+MinestPoint+MinestPoint) && nSurprise > 0 ){
                Count++;
                nSurprise--;
            }
        }
        printf("Case #%d: %d\n",round+1,Count);
    }
    return 0;
}
