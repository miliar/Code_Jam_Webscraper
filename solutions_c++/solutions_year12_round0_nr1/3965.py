#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	char m[27];
	m[0]='y'; m[1]='h'; m[2]='e'; m[3]='s'; m[4]='o'; m[5]='c';
	m[6]='v'; m[7]='x'; m[8]='d'; m[9]='u'; m[10]='i'; m[11]='g';
	m[12]='l'; m[13]='b'; m[14]='k'; m[15]='r'; m[16]='z'; m[17]='t';
	m[18]='n'; m[19]='w'; m[20]='j'; m[21]='p'; m[22]='f'; m[23]='m';
	m[24]='a'; m[25]='q';
	int c;
	scanf("%d\n",&c);
	int x=1;
	while(x<=c) {
		char w[101];
		gets(w);
		int l=strlen(w);
		for(int i=0;i<l;i++){
			if(w[i]==' ')
				continue;
			w[i]=m[w[i]-97];
		}
		printf("Case #%d: %s\n",x,w);
		x++;
	}
	return 0;
}

