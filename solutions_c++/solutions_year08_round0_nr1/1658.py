#include<stdio.h>
#include<string.h>
#define INF (1<<30)

char buscador[1002][102],palabra[1002][102],buff[102];
int consultas[1002],tabla[1002];
int casos,nbus,npal,min;

void solve(){
	int min;
	for(int i=0; i<nbus; i++)
		tabla[i] = 0;
	for(int i=npal-1; i>=0; i--)
	{
		min=INF;
		for(int j=0; j<nbus; j++)
			if(tabla[j]<min && consultas[i] != j)
				min= tabla[j];
		if(consultas[i] != -1)
			tabla[consultas[i]] = min + 1;
	}
}

void rollo(int ncaso){
   gets(buff);
   sscanf(buff,"%d",&nbus);
   for(int i=0;i<=nbus;i++)
      gets(buscador[i]);
   sscanf(buscador[nbus],"%d",&npal);
   for(int i=0;i<npal;i++){
      gets(palabra[i]);
      for(int j=0;j<nbus;j++)
         if( strcmp(palabra[i],buscador[j])==0 ){
            consultas[i]=j;
            break;
         }
   }
   solve();
	int res = INF;
	for(int i=0; i<nbus; i++)
		if(res > tabla[i])
			res = tabla[i];
   printf("Case #%d: %d\n",ncaso,res);
}

int main(){
   scanf("%d\n",&casos);
   for(int i=1;i<=casos;i++)
      rollo(i);
   return 0;
}
