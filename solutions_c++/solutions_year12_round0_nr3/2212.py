#include <cstdio>
#include <map>
#include <math.h>
using namespace std;
map<long long, map<long long, int> > esta;
int resultado;
void reciclados(long long a, long long b);
void obten(long long num, long long min, long long max);
int dame(int numDigitos, int pos, long long numero);
int longitud(long long num);
int main(){

	long long casos, a,b;

	scanf("%lld\n",&casos);

	for(int i=0; i<casos; i++){

		scanf("%lld%lld",&a,&b);
		esta.clear();
		resultado=0;
		reciclados(a,b);
		printf("Case #%d: %d\n", i+1,resultado);
	}
}

void reciclados(long long a, long long b){
long long aux;
	for(int num=a;num<=b;num++){
		if(esta.count(num)==0){
			esta[num].clear();
		}
		obten(num,a,b);
			
	}
}
long long traduce(long long num){
	long long result=0;
	while(num>0){
		int aux=num%10;
		result=result+pow(10.0,(double)aux);
		num/=10;
	}
return result;
}
void obten(long long num, long long min, long long max){
int a, b, j;
long long aux;
j=longitud(num);

	for(int i=1; pow(10,(double)i)<num; i++){
		a=dame(i,0,num);
		b=dame(j-i,i,num);
		aux=b;
		aux+=a*pow(10,(double)j-i);
				if(aux>num)
				if(aux>=min && aux<=max){
					if(esta[num].count(aux)==0){
						esta[num][aux]=1;
							resultado++;
					}
				}
	}
}
int dame(int numDigitos, int pos, long long numero){
int mod=pow(10,(double)numDigitos);
for(int i=0; i<pos; i++){
numero/=10;
}
return numero%mod;
}
int longitud(long long num){
	int result=0;
	while(num>0){
		num/=10;
		result++;
	}
return result;
}
