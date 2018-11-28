#include<iostream>
#include<cmath>

using namespace std;

int main (){
    int T,Case=1;
    cin>>T;
    
    while(T>0){
        int A,B,Pairs=0;
        cin>>A;
        cin>>B;
        int Num;
        Num = A;
        int digits = floor(log10(Num));
        int *array= new int [10];
        if(digits > 0){             
            while(Num <= B){
                for(int i=1;i<=digits;i++){
                    int part1 = Num % (int)(pow(10, i));
                    if(part1 >0){
                        int part2 = Num / (pow(10, i));
                        int newNum = part1* pow(10,digits+1-i) + part2;
                        array[i]=newNum;
                        if(newNum <= B && newNum >= A && newNum > Num){
                           bool flag = false;
                           for(int j=1;j<i;j++){
                               if(newNum == array[j]){
                                 flag = true;
                               }
                           }
                           if(flag == false){
                              Pairs++;
                           }    
                                         
                        }
                    }     
                }                   
            Num++;
            }
        }
        cout<<"Case #"<<Case<<": "<<Pairs<<endl;
        Case++;
        delete array;
        T--;
    }    
    return 0;
}    
