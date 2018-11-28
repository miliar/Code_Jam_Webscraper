#include <cstdlib>
#include <iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[])
{
    int compute(int *candy, int candyNum, int s, int x, int p, int max);
    
    FILE *input;
    int i, j, x, sum, ans;
    int looptime, candyNum;
    int candy[64];
    char buff[256];
    input = fopen("D:\\Dev-Cpp\\3-test.txt","ro");
    fscanf(input,"%d",&looptime);
    for(i=0; i<looptime; i++) {
        fscanf(input,"%d",&candyNum); 
        sum = 0;
        x = 0;
        for(j=0; j<candyNum; j++) {
            fscanf(input,"%d",&candy[j]);             
//            sum += candy[j];
        }
        for(j=0; j<candyNum; j++) {
            //printf("%d ", candy[j]);        
            sum += candy[j];
            x ^= candy[j];
        }      
        //printf("=%d",sum);

        ans = compute(candy, candyNum, sum, x, 0, 0);        
        printf("Case #%d: ", i+1); 
        if(ans==0) {
            printf("NO\n");         
        }else{
            printf("%d\n", ans);         
        }
         
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}

int compute(int *candy, int candyNum, int s, int x, int p, int max) {
    int max1,max2;
    int a, b;
    
    if( candyNum == 0 ) {
        return max;
    }
    
    a = x ^ candy[0];
    b = p ^ candy[0];
    

    if(a == b) {
        max = (max<(s - candy[0]))? (s - candy[0]): max;            
    }
    //printf("[ a=%d, b=%d, x=%d, p=%d, max=%d ]", a, b, x, p, max);

    max1 = compute(candy+1, candyNum-1, s-candy[0], a, b, max);
    max2 = compute(candy+1, candyNum-1, s,          x, p, max);
    
    return (max1>max2)?max1:max2;      
}













