#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Tdata{
  int a;
  int b;
};

bool operator< (Tdata a, Tdata b){
  return a.a<b.a;
}

Tdata data[1010];
int stevec,n,t,k;



int main(){
  Tdata temp;
  
  scanf("%d", &t);
  for(int tt=0;tt<t;tt++){
    scanf("%d", &n);
    stevec = 0;
    for(int i=0;i<n;i++){
      scanf("%d %d", &temp.a, &temp.b);
      data[i] = temp;
    }
    sort(data, data+n);
    for(int i=0;i<n-1;i++){
      for(int j=i+1;j<n;j++){
	if(j==i) continue;
	if(data[i].b > data[j].b && data[i].a < data[j].a) stevec++;
	if(data[i].b < data[j].b && data[i].a > data[j].a) stevec++;
      }
    }
    printf("Case #%d: %d\n", tt+1, stevec);
  }
  
  
  

  



  return 0;
}