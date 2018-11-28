#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <stdlib.h> // Отсюда берём rand()
#include <time.h> // Здесь находится time()
#include <vector>

int main(){ 
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n;
	//yhesocvxduiglbkrztnwjpfmaq 
	char s[]="yhesocvxduiglbkrztnwjpfmaq",s2[345];
	scanf("%d",&n);	
	for(int i = 0;i<n;i++){
	gets(s2);
	printf("Case #%d: ",i+1);
	int len = strlen(s2);
	for(int i =0;i<len;i++){
	if(s2[i]==' ')printf(" "); else printf("%c",s[s2[i]-'a']);
	}
	printf("\n");
	}
	return 0;
   
}