#include <iostream>

using namespace std;


int t;

int A[1000];
int B[1000];
int main(){
cin>>t;
for(int i=1;i<=t;i++){
 int a=0;
 int n;
 cin>>n;
 for(int j=0;j<n;j++){
    cin>>A[j];
    cin>>B[j];
    for(int i2=0;i2<j;i2++){
        if((A[i2]>A[j]&&B[i2]<B[j] )||(A[i2]<A[j]&&B[i2]>B[j] ))
            a++;
    }
 }

 cout<<"Case #"<<i<<": "<<a<<endl;
}

}
