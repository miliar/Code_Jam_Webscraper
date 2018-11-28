#include<iostream>
using namespace std;

int main(){
  long long int n,pd,pg;
  int t,td,tg;
  int flag;

  cin >> t;

  for(int i=0;i<t;i++){
    cin >> n >> pd >> pg;
    if( (pg==100 && pd !=100) || (pg==0 && pd !=0))flag = 0;
    else flag = 1;

    td = 100;
    tg = 100;

    if( !(pd%2) ){
      if( !( (pd/2)%2 ) )td /= 4;
      else td /= 2;
    }
    if( !(pd%5) ){
      if( !( (pd/5)%5 ) )td /= 25;
      else td /= 5;
    }

    if(td>n)flag = 0;

    cout << "Case #" << i+1 << ": ";
    if(flag)cout << "Possible" << endl;
    else cout << "Broken" << endl;

  }
}
