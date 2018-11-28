#include <algorithm>
#include <cstdio>
using namespace std;

char y[507];
int ntc,ys;
int wyn[20];
void act(int x) {
	wyn[x]+=wyn[x-1]; wyn[x]%=10000;
}
int main() {
	scanf("%d ", &ntc);
	for(int xx=1; xx<=ntc; ++xx) {
		ys=0;
		do
			scanf("%c",&y[ys]);
		while(y[ys++]!='\n');
		--ys;
		y[ys]='\0';
		for(int i=0; i<ys; ++i) {
			if(y[i]=='w') { ++wyn[0]; wyn[0]%=10000; }
			if(y[i]=='e') { act(1); act(6), act(14); }
			if(y[i]=='l') { act(2); }
			if(y[i]=='c') { act(3); act(11); }
			if(y[i]=='o') { act(4); act(9); act(12); }
			if(y[i]=='m') { act(5); act(18); }
			if(y[i]==' ') { act(7); act(10); act(15); }
			if(y[i]=='t') { act(8); }
			if(y[i]=='d') { act(13); }
			if(y[i]=='j') { act(16); }
			if(y[i]=='a') { act(17); }
		}
		printf("Case #%d: ",xx);
		int res=wyn[18];
		if(res<10) { printf("000"); printf("%d\n", res); }
		else if(res<100) { printf("00"); printf("%d\n", res); }
        else if(res<1000) { printf("0"); printf("%d\n", res); }
        else printf("%d\n", res);
		for(int i=0; i<20; ++i) wyn[i]=0;
	}
}
