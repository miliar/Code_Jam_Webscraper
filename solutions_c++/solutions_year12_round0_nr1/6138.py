#include<iostream>
#include<string.h>
using namespace std;
char arr[105];
int ind[27]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16}; //17,?,19   and  0,?};
int main(){
    int t;
    scanf("%d",&t);
	int tr=t;
	gets(arr);
    while(t--){
              gets(arr);//cout<<"hello\n";
              //printf("\n");              
              int len=strlen(arr);
		printf("Case #%d: ",tr-t);
              for(int i=0;i<len;i++){
                      if(arr[i]!=' '){
                                   int temp=arr[i]-'a';
                                   temp=ind[temp];
                                   char ch='a'+temp;
                                   printf("%c",ch);             
                      }        
                      else{
                           printf(" ");     
                      }
              }
              printf("\n");
    }
    //system("pause);
    return 0;    
}
