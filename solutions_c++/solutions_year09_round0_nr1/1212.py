#include <cstdio>
using namespace std;

char T[6000][30];//[ilosc prawdziwych wyrazow][dlugosc wyrazow]
bool B[30][30];//[dlugosc wyrazu][litery alfabetu] czy mamy dana litere na pozycji

int main(){
  int l, d , n;
  scanf("%d%d%d", &l, &d, &n);
  for(int i=0; i<d; i++){
    scanf("%s", T[i]);
  }
  long long wynik;
  for(int i=0; i<n; i++){
    wynik=0;
    for(int j=0; j<30; j++)
      for(int u=0; u<30; u++)
	B[j][u]=0;
    /*for(int j=0; j<30; j++){
      for(int u=0; u<30; u++){
	printf("%d", B[j][u]);
      }
      printf("\n");
    }*/
    int j=0,t;
    getchar();
    while(j<l){
      t = getchar();
      if(t=='('){
	t = getchar();
	while(t!=')'){
	  B[j][t-'a']=1;
	  t=getchar();
	}
      }else{
	B[j][t-'a']=1;
      }
      j++;
    }
    /*for(int j=0; j<30; j++){
      for(int u=0; u<30; u++){
	printf("%d", B[j][u]);
      }
      printf("\n");
    }*/
    for(int h=0; h<d; h++){
      bool error=false;
      for(int j=0; j<l; j++){
	if(B[j][ T[h][j] - 'a']==false){
	  error=true;
	  break;
	}
      }
      if(!error)
	wynik++;
    }
    printf("Case #%d: %lld\n", i+1, wynik);
  }
  return 0;
}
