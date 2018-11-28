#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int n=0;
    
    char input[101];
    char output[101];
    int j=0;
    char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    scanf("%d\n",&n);
    for(int i=0;i<n;i++)
    {
            gets(input);
            //printf("%s\n",input);
            j=0;
            while(input[j]!='\0' && j<100){
                 	if(input[j]==' ')
                        	output[j]=input[j];    
			else
                        	output[j]=mapping[input[j]-'a'];
                        j++;                      
            }
            output[j]='\0';
            printf("Case #%d: %s\n",i+1,output);
    }
    cin>>n;
    return 0;   
}
