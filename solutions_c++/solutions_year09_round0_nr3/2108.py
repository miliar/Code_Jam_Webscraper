#include <cstdio>
#include <list>
using namespace std;
int main(){
  char tekst[]=" welcome to code jam";
  int N;
  scanf("%d\n",&N);
  for(int id=1; id<=N; id++){
     int result[20];
     result[0]=1;
     for(int i=1; i<=19; i++)
	result[i]=0;
     char c;
     for(scanf("%c",&c);c!=10;scanf("%c",&c)){
	for(int i=1; i<=19; i++)
	   if(tekst[i]==c)
		result[i]+=result[i-1];
      }
      printf("Case #%d: ",id);
      if(result[19]<1000)printf("0");
      if(result[19]<100)printf("0");
      if(result[19]<10)printf("0");
      printf("%d\n",result[19]);
  }
  
}
