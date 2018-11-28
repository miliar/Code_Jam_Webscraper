/*Written by Vladimir Ignatiev*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(A=0;A<B;++A)

char abc[256];

int Init()
{	
	memset(abc,'?',256);
	char nLen;
	int i;
	
	abc['q']='z';
	abc['e']='o';
	abc['y']='a';
		
	char g1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char a1[]="our language is impossible to understand";
	nLen=strlen(g1);
	rep(i,nLen) abc[g1[i]]=a1[i];

	
	char g2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char a2[]="there are twenty six factorial possibilities";
	nLen=strlen(g2);
	rep(i,nLen) abc[g2[i]]=a2[i];


	char g3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char a3[]="so it is okay if you want to just give up";
	nLen=strlen(g3);
	rep(i,nLen) abc[g3[i]]=a3[i];
	
	abc['z']='q'; //Only mapping not present in examples

	return 0;
}

int main()
{
	FILE* In=fopen("A-small-attempt0.in","r");if(!In) return 1;
	FILE* Out=fopen("A-small-attempt0.res","w");if(!Out) return 2;

	Init();
	int nCount,i;
	fscanf(In,"%d",&nCount);
	char strIn[101];
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"\n%[^\n]",strIn);
		char *pStr=strIn;
		while(*pStr!='\0') {*pStr=abc[*pStr];pStr++;}
		fprintf(Out,strIn);
		fprintf(Out,"\n");
	};
	fclose(In);
	fclose(Out);
	return 0;
}