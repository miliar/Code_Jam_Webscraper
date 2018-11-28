#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char str[5001][20];
char correct[5001];
char pattern[5001];
int main(){
	int l,d,n;
	while(scanf("%d %d %d",&l,&d,&n) == 3){
		for(int i=0;i<d;i++)
			scanf("%s ",str[i]);
		for(int t=0;t<n;t++){
			for(int i=0;i<d;i++)
				correct[i] = 1;
			int ans = 0;
			int count = 0;
			char input[51111];
			scanf("%s",input);
			int len = strlen(input);
			input[len] = '\n';
			input[len + 1] = '\0';
			len = 0;
			while(1){
				char c;
				c = input[len++];
				if(c == '\n'){
					break;
				}else if(c != '('){
					for(int i=0;i<d;i++){
						if(str[i][count] != c){
							correct[i] = 0;
						}
					}
					count++;
				}else if(c == '('){
					int k = 0;
					pattern[k++] = c;
					while((c = input[len++]) && c != ')'){
						pattern[k++] = c;
					}
					for(int i=0;i<d;i++){
						int flag = 0;
						for(int j=0;j<k;j++){
							if(pattern[j] == str[i][count]){
								flag = 1;
								break;
							}
						}
						if(flag == 0)correct[i] = 0;
					}
					count++;
				}

			}
			for(int i=0;i<d;i++){
				if(correct[i] == 1){ans++;}
			}
			printf("Case #%d: %d\n",t + 1,ans);
		}
	}
	return 0;
}
