#include<stdio.h>
#include<stdlib.h>
#include<string.h>


char M[150]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char R[150]="our language is impossible to understand";
char v[150],s[200];

int main(){
//	freopen("i.IN","r",stdin);
//	freopen("w.txt","w",stdout);

	int i,T,j,l;
	l=strlen(M);
	for(i=0;i<l;i++){
		v[M[i]]=R[i];
	}
	strcpy(M,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(R,"there are twenty six factorial possibilities");

	l=strlen(M);
	for(i=0;i<l;i++){
		v[M[i]]=R[i];
	}

	strcpy(M,"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	strcpy(R,"so it is okay if you want to just give up");
	l=strlen(M);
	for(i=0;i<l;i++){
		v[M[i]]=R[i];
	}


	v['q']='z';
	v['z']='q';

	scanf("%d",&T);
	getchar();

	for(i=1;i<=T;i++){
		gets(s);
		printf("Case #%d: ",i);
			l=strlen(s);
		for(j=0;j<l;j++)
			printf("%c",v[s[j]]);
		printf("\n");
	}

	//gets(c);



  return 0;
}