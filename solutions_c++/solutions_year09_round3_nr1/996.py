#include<iostream>
#include<stdio.h>
#include<string>
#include<map>

using namespace std;

int main(){
long long num;
int n,x,nc, k, i;
char code[100];
scanf("%d",&nc);
int mymap[500] = {-1};
 //map<char,int> mymap;
 // map<char,int>::iterator it;

for(n=1;n<=nc;n++){
                   scanf("%s",code);
                   
                   //printf("hahah: %s\n",code);
                   k = 0;
                   mymap[code[0]] = 1;
                   
                   //mymap.insert ( pair<char,int>(code[0],1) );
                   
                   for(i=1; i <strlen(code) ;i++){
                            if(mymap[code[i]] == -1){
                               if(k == 1)
                               k++;
                               mymap[code[i]] = k;
                               k++;  
                            }
                   }
                   num = 0;
                   //for(i=0;i<strlen(code);i++)
                   //printf("%d",mymap[code[i]]);
                   
                   if(k<2)
                     k = 2;
                     //printf("\nhhhh: %d\n",k);
                   
                   
                   for(i=0;i<strlen(code);i++){
                                               num = num*k + mymap[code[i]];
                   }
                   
                   printf("Case #%d: %ld\n",n,num);                 
                   for(i=0;i<500;i++)
                       mymap[i] = -1;
                       
                   code[0] = '\0';
}

}
                                             
                                               
                                               

