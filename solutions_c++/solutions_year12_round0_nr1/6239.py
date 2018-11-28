#include"cstdio"
char ctrl[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[100000];
FILE *a,*b;
void oku(){
	for(int i=0;feof(a)!=1;i++){
		fscanf(a,"%c",&str[i]);
		if(str[i]=='\n')return;
	}
}
int main(){
	a=fopen("A-small-attempt0.in","r");
	b=fopen("A-small-attempt0.out","w");
	int i,n,cnt=0;
	fscanf(a,"%d ",&n);
	while(cnt<n){
		oku();
		for(i=0;str[i] and str[i]!='\n';i++){
			if(i==0)fprintf(b,"Case #%d: ",++cnt);
			if(str[i]==' ')
					fprintf(b," ");
			else 
				fprintf(b,"%c",ctrl[str[i]-'a']);
		}
		fprintf(b,"\n");
	}
	return 0;	
}
