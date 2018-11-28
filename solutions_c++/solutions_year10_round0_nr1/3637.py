#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int on[31];
int main(){

for(int i=0; i<31; i++){
on[i] = (1<<i) -1;
}

ofstream out;
out.open ("prob_a_answers.out");
int n,k;
int numCases;
cin>>numCases;

for(int i=1;i<=numCases; i++){
cin>>n>>k;
int isOn= k%(1<<n);
if(isOn == on[n]){
out<<"Case #"<< i <<": ON"<<endl;
}else{
out<<"Case #"<< i <<": OFF"<<endl;
}

}



}

