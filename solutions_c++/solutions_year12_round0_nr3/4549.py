#include <iostream>
#include <algorithm>
#include<stdio.h>
using namespace std;

int main () {
  //freopen("input.txt","r",stdin);

  //freopen("output.txt","w",stdout);
  int t ;
  cin>> t;
    int cases = 1;
  while(t--){
    int digit = 1 ;
    int a ,b , c ;
    cin>>a>>b;
    c = a;
    cout<<"Case #"<<cases<<": ";cases++;
    int jumlah = 0;
    while(c>=10){c/=10;digit++;}
    if(digit == 1) cout<<"0"<<endl;
    else if (digit == 2){
        for(int i = b  ; i>=a ; i--){
            int myints[] = {1,2};
            myints[0] = i / 10;
            myints[1] = i % 10 ;
            int result = myints[1] * 10 + myints[0];

            if(result <= i || result<10) continue;
            if(result<= b ){jumlah++;}
        }
        cout<<jumlah << endl;
    }
    else {
        int count2 = 0;
        int count3 = 0;
        for(int i = b ; i>=a ; i--){
            int angka1,angka2,angka3;
            angka1 = i / 100;
            angka2 = (i % 100)/10 ;
            angka3 = i % 10 ;
            int result1 = angka2 * 100 + angka3 * 10  + angka1 ;
            int result2 = angka3 * 100 + angka1 * 10  + angka2 ;
            if(result1 < i ||result1==i||result1<100)result1 = 0;
            else if(result1<=b)jumlah++;
            if(result2 < i ||result2==i||result2<100)result2 = 0;
            else if(result2<=b)jumlah++;
        }
        cout<<jumlah<<endl;
    }
 }
  return 0;
}
