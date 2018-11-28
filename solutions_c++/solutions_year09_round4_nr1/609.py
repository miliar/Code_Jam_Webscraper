#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
int main(){
  int t;
  scanf("%d", &t);
  for(int i=1; i<=t; i++){
    int n;
    scanf("%d", &n);
    int TAB[60];
    char String[60];
    for(int j=0; j<60; j++)
      TAB[j]=0;
    for(int j=0; j<n; j++){
      scanf("%s", String);
      int t=0;
      for(int k=strlen(String); k>=0; k--){
	if(String[k]=='1'){
	  t=k+1;
	  break;
	}
      }
      TAB[j]=t;
    }
    //for(int j=0; j<n; j++)
      // printf("%d ", TAB[j]);
    //printf("\n");
    long long wynik=0;
    for(int j=0; j<n; j++){
      int wybrany=-1;
      for(int k=j; k<n; k++){
	if(TAB[k]<=(j+1)){
	  wybrany=k;
	  break;
	}
      }
      //printf("Wybrany: %d\n", wybrany);
      for(int k=wybrany; k>j; k--){
	wynik++;
	swap(TAB[k], TAB[k-1]);
      }
      //for(int j=0; j<n; j++)
      //printf("%d ", TAB[j]);
      //printf("\n");
    }
    printf("Case #%d: %lld\n", i, wynik);
  }
  return 0;
}
