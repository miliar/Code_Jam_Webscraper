#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;

int main(){
	int test = 0;
	int len = 0;
	char new_char[27] =	{'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','q','p','d','r','j','g','t','h','a','z'};
	char res_char[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char output_char[27] = 
{'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char input[1100], output[1100];
	scanf("%d\n",&test);
	for(int x = 1; x <= test; x++){
		gets(input);
		len = strlen(input);
		for(int i = 0; i<len;i++){
			if(input[i]>='a' && input[i]<='z'){
				output[i] = output_char[(int)(input[i] - 'a')];
			}
			else output[i] = input[i];
		}
		output[len] = '\0';
		printf("Case #%d: %s\n",x,output);
	}
	return(0);
}
	
