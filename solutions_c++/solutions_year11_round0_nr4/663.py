#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
using namespace std;
int array[1005],array2[1005];
int main (){
    int T,n,i,sum,ca=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",&array[i]);
            array2[i] = array[i];
        }
        sort(array2,array2+n);
        sum = 0;
        for(i=0;i<n;i++){
            if(array[i] != array2[i]){
                sum++;
            }
        }
        ca++;
        printf("Case #%d: %d\n",ca,sum);
    }
    return 0;
}
/*
3
2
2 1
3
1 3 2
4
2 1 4 3
*/
