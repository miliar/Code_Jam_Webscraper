#include<iostream>
#include<fstream>
#include<vector>
#include<stdlib.h>
using namespace std;
int compare( const void *arg1, const void *arg2){
    int* a=(int*)(arg1);
    int* b=(int*)(arg2);
	return (*a-*b);
}
int main(){
	ifstream in("A-small.in");
	ofstream out("A-small.out");
int con1[9];
int con2[9];
    int num,T=0,n;
    in>>T;
    int i=0;
    while(i<T){
       in>>n;
       int j=0;
       int result=0;
       while(j<n){
           in>>num;
           con1[j]=num;
           j++;           
       }
       j=0;
        while(j<n){
           in>>num;
           con2[j]=num;
           j++;           
       }
       qsort(con1,n,sizeof(int),compare);
       qsort(con2,n,sizeof(int),compare);
       j=0;
       while(j<n){
          result+=con1[j]*con2[n-1-j];
          j++;
       }
       i++;
       out<<"Case #"<<i<<": "<<result<<endl;
    }	
}
