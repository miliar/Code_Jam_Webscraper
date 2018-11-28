#include<iostream>
#include<stdio.h>
#include<cmath>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include <utility>
#include <bitset>
#define pb push_back

using namespace std;


int main(){
    string ans="yhesocvxduiglbkrztnwjpfmaq";
    int t,i=0;
    char a[105];
  //  freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    
    scanf("%d",&t); getchar();
    
    for(i=1;i<=t;i++){
               printf("Case #%d: ",i);
               gets(a);
               for(int j=0;j<strlen(a);j++)
                   if(a[j]>='a'&&a[j]<='z')
                        printf("%c",ans[a[j]-'a']);
                   else
                         printf("%c",a[j]);
              
              printf("\n");                         
               
    }
    return 0;
}
