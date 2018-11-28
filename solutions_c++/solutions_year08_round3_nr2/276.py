#include <cstdio>
#include <cstring>

using namespace std;

typedef long long int lli;

char tab[20];
int len;
int znak[20];
lli wynik=0;

lli liczba(int a,int b){
  lli mn=1;
  lli wyn=0;
  while(b!=a){
    wyn+=(lli)(((lli)(tab[b]-'0'))*mn);
    mn*=10;
    b--;
  }
  wyn+=(lli)((lli)(tab[b]-'0')*mn);
  return wyn;
}

bool isUgly(lli a){
  if(a==0){
    return true;
  }
  if(a<0){
    a*=-1;
  }
  if(a%2==0 || a%3==0 || a%5==0 || a%7==0){
    return true;
  }else{
    return false;
  }
}

lli licz(){
  int i=0;
  lli wyn=0;
  int ip=0;
  int zn=1;
  while(i<len){
    //printf("kolejny znak=%d i=%d\n",zn,i);
    while(i<len && znak[i]==0){
      i++;
    }
    i--;
    if(zn==1){
      wyn+=liczba(ip,i);
    }else{
      wyn-=liczba(ip,i);
    }
    i+=2;
    ip=i-1;
    zn=znak[ip];
  }
  if(ip<len){
    if(zn==1){
      wyn+=liczba(ip,len-1);
    }else{
      wyn-=liczba(ip,len-1);
    }
  }
  return wyn;
}


void znakuj(int a){
  if(a<len){
    znak[a]=0;
    znakuj(a+1);
    znak[a]=1;
    znakuj(a+1);
    znak[a]=2;
    znakuj(a+1);
  }else{
    lli w=licz();
    if(isUgly(w)==true){
      //printf("suma %lld jest ugly\n",w);
      wynik++;
    }
    else{
      //printf("suma %lld nie jest ugly\n",licz());
    }
  }
}



int main(){
  int N;
  scanf("%d",&N);
  for(int zest=1;zest<=N;zest++){
    scanf("%s",tab);
    len=strlen(tab);

    wynik=0;
    znakuj(1);

    printf("Case #%d: %lld\n",zest,wynik);
  }

  return 0;
}
