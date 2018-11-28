#include <stdio.h>

char map[300];

char str1[50]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char str2[50]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char str3[50]="de kr kd eoya kw aej tysr re ujdr lkgc jv";

char ans1[50]="our language is impossible to understand";
char ans2[50]="there are twenty six factorial possibilities";
char ans3[50]="so it is okay if you want to just give up";

char str[105];

int n;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int i,j;
    map['y']='a';
    map['e']='o';
    map['q']='z';
    map['z']='q';
    for(i=0;str1[i]!='\0';i++){
    	map[str1[i]]=ans1[i];
    }
    for(i=0;str2[i]!='\0';i++){
    	map[str2[i]]=ans2[i];
    }
    for(i=0;str3[i]!='\0';i++){
    	map[str3[i]]=ans3[i];
    }/*
    for(i='a';i<='z';i++){
    	printf("%c %c\n",i,map[i]);
    }*/
    scanf("%d\n",&n);
    for(int zz=1;zz<=n;zz++){
    	printf("Case #%d: ",zz);
    	gets(&str[1]);
    	for(i=1;str[i]!='\0';i++){
    		if(str[i]==' '){
    			printf(" ");
    		}else{
    			printf("%c",map[str[i]]);/*
                if(map[str[i]]==0){
                    printf("###%c###",str[i]);
                }*/
    		}
    	}
    	printf("\n");
    }
	return 0;
}


