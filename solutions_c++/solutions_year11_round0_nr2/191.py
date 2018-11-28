#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int cls[300][300];
int tra[300][300];
int T,C,D,len; char inp[100000];
char tmp[100];
char str[100000]; int now,f=0;
int main(){
    scanf("%d",&T);
    while(T--){
	memset(cls,0,sizeof(cls));
	memset(tra,0,sizeof(tra));
	scanf("%d",&C);
	while(C--){
	    scanf("%s",tmp);
	    tra[tmp[0]][tmp[1]] = tmp[2];
	    tra[tmp[1]][tmp[0]] = tmp[2];
	}
	scanf("%d",&D);
	while(D--){
	    scanf("%s",tmp);
	    cls[tmp[0]][tmp[1]] = 1;
	    cls[tmp[1]][tmp[0]] = 1;
	}
	scanf("%d",&len);
	scanf("%s",inp);
	now = 0;
	for(int i=0;i<len;i++){
	    str[now++] = inp[i];
	    while(now>1 && tra[str[now-1]][str[now-2]]){
		str[now-2] = tra[str[now-1]][str[now-2]];
		now--;
	    }
	    for(int j=0;j<now-1;j++){
		if(cls[str[now-1]][str[j]]){
		    now = 0;
		    break;
		}
	    }
	}
	printf("Case #%d: ",++f);
	printf("[");
	for(int i=0;i<now;i++){
	    printf("%c",str[i]);
	    if(i!=now-1){
		printf(", ");
	    }
	}
	printf("]\n");
    }
}
