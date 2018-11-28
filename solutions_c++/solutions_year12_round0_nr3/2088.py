#include<iostream>
using namespace std;

int d[7];
int digitCount = 0;

int pre[10];

void setDigits(int i){
     int c = 0;
     int k = i;
     while(k>0){
                k/= 10;
                c++;
     }
     digitCount = c;
     c=1;
     while(i>0){
                d[digitCount-c] = i%10;
                i/= 10;
                c++;
     } 
}

int getNumber(int i , int shift){
    int num = 0;
    int k =1;
    int digit = 0;
    while( digit<digitCount ){
           num = num*10;
           num += d[(digit+shift)%digitCount];
           digit++;
    }
    pre[shift] = num;
    return num;
}

int isRepeat(int num , int shift){
     int k = 0;
     for(int i = 1 ; i < shift ; i++)
     if(num == pre[i])
     k = 1;
     return k;
}

int output(int a , int b){
    int num = 0;
    int count = 0;
    for(int i = a; i <b ; i++){
         setDigits(i);

         for( int d = 1 ; d < digitCount ; d++ ){
              num = getNumber(i,d);
              if(num>i && num<=b && !isRepeat(num ,d)){
                                //cout<<"Number: "<<i <<"; num :"<<num<<endl;
              count++;
              }
         }
    }
    return count;
}

int main(){
    int n ,a,b;
    cin>>n;
    int i = 1;
    int count ;
    while(i<=n){
               count = 0;
               cin>>a;
               cin>>b;
               cout<<"Case #"<<i<<": ";
               cout<<output(a,b)<<endl;
               i++;
    }
    return 0;
}
