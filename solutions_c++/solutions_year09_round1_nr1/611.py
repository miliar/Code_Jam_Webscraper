#include<iostream>
#include<string>
#include<stack>
using namespace std; 

const int N = 1000001;
const int K = 11;
int dasie[N][K];
int tab[K];

stack<int> S;
bool check(int a, int pod){
//if(pod==3)     printf("wyw(%d,%d)\n",a,pod);
  if(dasie[a][pod] == 1) return 1;
  S.push(a);
  bool ok = 0;
  while(1){
    int y = S.top();
    if(y == 1){ ok = 1; break; }
//if(pod==3)    printf("sciagam : %d\n",y);
   int z = 0;
    while(y){
//if(pod==3)         printf("y,z : %d,%d\n",y,z);
      z += (y%pod)*(y%pod);
      y/=pod;
    }
//if(pod==3)       printf("dostaje : %d\n",z);
    if(z>=N || dasie[z][pod] == -1 || dasie[z][pod]==-2){
      break;
    }
    else if(dasie[z][pod] == 1){
      ok = 1;
      break;
    }
    else{
      dasie[z][pod] = -2;
      S.push(z);
    }
  }
  while(!S.empty()){
    if(ok){
      dasie[S.top()][pod]=1;
    }
    else{
      dasie[S.top()][pod]=-1;
    }
    S.pop();
  }
  return dasie[a][pod] == 1;
}
int n;
void parse(string a){
  int z = 0,i=0;
  n=0;
  while(i < a.size()){
    while(isdigit(a[i])){
      z *= 10;
      z += a[i]-'0';
      i++;
    }
    tab[++n] = z;
    z=0;
    i++;
  }
}

int licz( string k){
  int z = 0;
  for(int i=0;i<k.size();i++){
    z*= 10;
    z += k[i]-'0';
  }
  return z;
}

main(){
  for(int i=2;i<K;i++){
    dasie[i][1] = 1;
    for(int j=2;j<N/10;j++)
      if(dasie[j][i] == 0) check(j,i);
  }
  string k;
  int z;
  getline(cin,k);
  z=licz(k);
  string a;
  for(int t=1;t<=z;t++){
    getline(cin,a);
    parse(a);
    for(int i=2;i<N;i++){
      bool tak = 1;
      for(int j=1;j<=n;j++)
        if(dasie[i][tab[j]] == -1){ tak = 0; break; }
      if(tak){printf("Case #%d: %d\n",t,i); break;}
    }
  }
}
