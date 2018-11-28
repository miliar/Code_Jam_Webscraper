#include <iostream>
#include <math.h>
#include <set>

using namespace std;

int power(int a){
    int temp,p;
temp = a;
p = 0;
while(temp>=1){
    temp = temp/10;
    p++;
}
return p;
}

int reverse(int a,int b){
    int temp,p,count,count1;
    set <int> S;
temp = a;
p = power(a);
count = 0,count1 = 0;
while(count!=p-1){
    temp = temp/10 + (temp%10)*pow(10,p-1);
    if(temp>a && temp<=b && S.count(temp) == 0){
        count1++;
        S.insert(temp);
    }
    count++;
}
return count1;
}

int main(){
int T,A,B,ub,i,j;
cin>>T;
j = 0;
while(T--){
cin>>A>>B;
ub = (A+B)/2;
int count = 0;
for(i=A;i<B;i++){
count = count + reverse(i,B);
}
cout<<"Case #"<<j+1<<": "<<count<<endl;
j++;
}
return 0;
}
