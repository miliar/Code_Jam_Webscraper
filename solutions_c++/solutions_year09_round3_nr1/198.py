#include <cstdio>
#include <cstring>
int main(){
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; t++){
    unsigned long long wynik=0;
    long long T[300];
    for(int i=0; i<300; i++)
      T[i]=-1;
    char st[70];
    long long sti[70];
    unsigned long long POT[70]; 
    scanf("%s", st);
    bool jedynka=0, zero=0;
    unsigned long long liczba=2;
    unsigned int dlu=strlen(st);
    for(unsigned int i=0; i<dlu; i++){
      if(T[ (int)st[i] ]==-1){
	if(jedynka==false){
	  T[ (int)st[i] ]=1;
	  jedynka=true;
	}else if(zero==false){
	  T[ (int)st[i] ]=0;
	  zero=true;
	}else{
	  T[ (int)st[i] ]=liczba++;
	}
      }
      sti[i]=T[ (int)st[i] ];
    }
    POT[0]=1;
    for(unsigned int j=1; j<dlu; j++){
      POT[j]=POT[j-1]*liczba;
    }
    for(unsigned int i=0; i<dlu; i++){
      //printf("%lld^%lld ", sti[i], POT[dlu-i-1]);
      wynik+=sti[i]*POT[dlu-i-1];
    }
    printf("Case #%d: %llu\n", t, wynik);
  }
  return 0;
}
