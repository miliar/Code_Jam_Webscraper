// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <stdlib.h>

int L,D,N;
int charcount[15];
char charlist[15][26];
char dic[5000][15];
int start;

int count(int charnum, char *str)
{
	char newstr[16];
	int i,c,m;
	
	strcpy(newstr,str);
	newstr[charnum+1]='\0';
	c=0;
	for(i=0;i<charcount[charnum];i++) {
		newstr[charnum]=charlist[charnum][i];
		while((start<D)&&((m=memcmp(newstr,dic[start],charnum+1))>0)) start++;
		if(start==D) return c;
		if(m==0)
			if((charnum+1)==L)
				c++;
			else
				c+=count(charnum+1, newstr);
	}
	return c;
}	
	
int compare (const void * a, const void * b)
{
  return ( strcmp( (char*)a, (char*)b ));
}

void sort(char array[], int len) {
	int i, j;
	char check;

	for(i=1; i<len; i++) {
		check = array[i];
		for(j=i; j>=1 && (check < array[j-1]); j--) {
			array[j] = array[j-1];
			array[j-1] = check;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,c;
	char str[500], *pos;

	scanf("%d %d %d\n", &L, &D, &N);
	for (i=0;i<D;i++) 
		scanf("%s\n", dic[i]);
	
	qsort (dic, D, 15, compare);

	
	for (i=0;i<N;i++) {
		scanf("%s\n",str);
		pos=str;
		for (j=0;j<L;j++) {
			if (pos[0]=='(') {
				charcount[j]=0;
				pos++;
				while (pos[0]!=')') {
					charlist[j][charcount[j]++]=pos[0];
					pos++;
				}
				pos++;
			}
			else {
				charcount[j]=1;
				charlist[j][0]=pos[0];
				pos++;
			}
			if (charcount[j]>1) sort(charlist[j],charcount[j]);
		}
		start=0;
		c=count(0,"");
		printf("Case #%d: %d\n",i+1, c);
	}
	return 0;
}   
