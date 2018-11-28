#include <iostream>
#include "stdio.h"
#include "math.h"
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#define DEBUG 0 

void func(void) {
    return ;
}

int main(void) {
    
    //1. define all the virables first
    int T;
    long A,B;
    
    long count;
   
    long tmp[10]; 
    char bitMap[2000000];    
    cin>>T;
    for(int c=1; c<=T; c++) {
        cin>>A>>B;
        count = 0;
        int numOfDigits = 1;
        long test = A;
        while(test /= 10)
            numOfDigits ++;
        for(int i=A; i<=B; i++) {
            bitMap[i] = '1';
        }
        for(long n=A; n<=B; n++) {
           if('0' == bitMap[n] ) 
               continue;
           bitMap[n] = '0';
           int num = 1;
           int flag = 0;
           tmp[0] = n;
           tmp[1] = tmp[2] = tmp[3] = tmp[4] = tmp[5] = -1;
           tmp[6] = tmp[7] = tmp[8] = tmp[9] = -1;
           for(int i=1; i<numOfDigits; i++) //can be optimized
           {
               flag = 0;
               long div = (long)pow(10, numOfDigits-i);
               long mul = (long)pow(10, i);
               long left = n/div;
               long right = n%div;    
               long newV = right*mul+left;
             
               for(int jj = 0; jj<num; jj++) {
                    if(tmp[jj] == newV)
                    {
                        flag =1 ;
                        break;
                    } 
               }   
               if(newV <=B && newV >=A && !flag) {
                    bitMap[newV] = '0';
                    tmp[num++] = newV;
               }
           }         
          
           if(num <2) ;
           else
              count += (num-1)*num/2; 
        }    
        cout<<"Case #"<<c<<": "<<count<<endl;
    } 
    return 0;

}
