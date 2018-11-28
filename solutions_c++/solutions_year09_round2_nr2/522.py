#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char num[30];

int myc(const void *p1, const void *p2)
{
	return *(char *)p1 - *(char *)p2;
}

int main()
{
	int t, Case=0, len, i, j, k;
	char tmp;
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &t);
	while(t--){
		Case++;
		scanf("%s", num);
		len = strlen(num);
		printf("Case #%d: ", Case);
		for(i=len-1; i>0; i--)
			if(num[i-1]<num[i]) break;
		if(i==0){
			qsort(num, len, sizeof(char), myc);
			if(num[0]=='0'){
				for(j=0; j<len; j++)
					if(num[j]!='0') break;
				tmp = num[j], num[j] = num[0], num[0] = tmp;
			}
			printf("%c0%s\n", num[0], num+1);
		}
		else{
			k = i;
			for(j=i+1; j<len; j++)
				if(num[i-1]<num[j] && num[j]<num[k])
					k = j;
			tmp = num[k], num[k] = num[i-1], num[i-1] = tmp;
			qsort(num+i, len-i, sizeof(char), myc);
			printf("%s\n", num);
		}	
	}
}
