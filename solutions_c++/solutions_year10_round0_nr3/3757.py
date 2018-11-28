#include <stdio.h>

int main(){
    int T;
    scanf("%d",&T);
    int *array,R,N,k,total_people = 0;
    for(int i=0;i<T;i++){
            scanf("%d%d%d",&R,&k,&N);
            array = new int[N];
            total_people = 0;
            for(int j=0;j<N;j++){
                    scanf("%d",&array[j]);
                    total_people += array[j];
            }
            
            int index = 0;
            int people_on_ride = 0;
            int rounds = 0;
            int profit = 0;
            if(k>=total_people){
                                delete[] array;
                                printf("Case #%d: %d\n",i+1,R*total_people);
                                continue;
            }
            while(rounds!=R){
                             if((people_on_ride + array[index]) > k){
                                               // printf("people on board =%d and k is %d\n",people_on_ride,k);
                                                profit += people_on_ride;
                                                rounds++;
                                               // printf("After round %d, profit is %d\n",rounds,profit);
                                                people_on_ride = 0;
                             }
                             else{
                                  people_on_ride += array[index];
                                  index = (index + 1)%N;
                             }
            }
            
            delete [] array;
            printf("Case #%d: %d\n",i+1,profit);
    }
    return 0;
}
