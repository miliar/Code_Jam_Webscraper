#include<iostream>
#include<string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <math.h>
using namespace std;
bool ifRecycable(int, int, int);

int main(){
    int caseNum=0;
    string wordNum1, wordNum2;
    int num1, num2;
    int size1, size2;
    int counter = 0;
    cin>>caseNum;

    for (int i=1; i<=caseNum; i++) {
        counter = 0;
        cin>>wordNum1>>wordNum2;
//    wordNum1 = "1";
//    wordNum2 = "9";
        num1=atoi(wordNum1.c_str());
        num2=atoi(wordNum2.c_str());
//        cout<<num1<<endl;
//        cout<<num2<<endl;
        size1=wordNum1.size();
//        cout<<size1<<endl;
        for (int j=num2; j>num1; j--) {
            for (int k=num1; k<j; k++) {
//                cout << k << " " << j <<endl;
                if(ifRecycable(j,k,size1)){
                    counter++;
                }
            }
        }
cout << "Case #"<<i<<": "<< counter<<endl;

    }
    return 0;
}

bool ifRecycable(int a, int b, int size){

    for (int z=1; z<=size; z++) {
        int p1 = pow(10,z);
        int p2 = pow (10,size-z);
        if(a%p1 == b/p2 && a/p1 == b%p2){
            return true;
        }
    }
    
    return false;
        
}