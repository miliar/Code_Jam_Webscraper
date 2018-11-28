// next.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <stdlib.h>

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
	int t, size, i, j, k;
	char str[500], m;

    scanf("%d\n",&t);
	for (i=0;i<t;i++) {
		gets(str);
		size=strlen(str);
		m=str[size-1];
		for(j=size-2;(j>=0)&(str[j]>=m);j--) m=str[j];

		if (j==-1) {
			strcat(str, "0");
			sort(str, strlen(str));
			for (j=0; str[j]=='0'; j++);
			str[0]=str[j];
			str[j]='0';
		} else {
			k=size-1;
			if (j==0) for(;str[k]=='0';k--);
			for(;str[k]<=str[j];k--);
			m=str[j];
			str[j]=str[k];
			str[k]=m;
			sort(&str[j]+1,strlen(&str[j]+1));
		}
		printf("Case #%d: %s\n",i+1,str);
	}
	return 0;

}

