#include <stdio.h>
#include <iostream>

using namespace std;

int main ()
{
int casos, jug, sdif, min, tot, val;

cin >> casos;

for(int i=0; i<casos; i++){
  tot=0;
  cin >> jug >> sdif >> min;
  
  for(int j=0; j<jug; j++){
    cin >> val;
    if( (val/3)>=min ){tot++;}
    else if( (val%3)!=0 && ((val/3)+1)>=min ){tot++;}
    else if(sdif>0 && (((val%3)==2 && ((val/3)+2)>=min) || ((val/3)==(min-1) && (val/3)!=0) )  ){tot++; sdif--;}
  }
  
  cout << "Case #"<<(i+1)<<": " << tot << endl;
}

}
