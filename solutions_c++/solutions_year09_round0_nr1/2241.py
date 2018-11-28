#include<iostream>
using namespace std;

int main(){
    int l,d,n; cin>>l>>d>>n;
    char word[d][l+1];
    for(int i=0;i<d;i++)
        scanf("%s",word[i]);
    for(int i=0;i<n;i++){
         char s[10000];cin>>s;
         int sz=strlen(s);
         int a[d],b[d],li=0,az=d,bz=0;
         for(int j=0;j<d;j++) a[j]=j;
         for(int j=0;j<sz;j++){
            if( s[j]=='(' ){  j++;
               while(s[j]!=')'){
                  for(int k=0;k<az;k++)
                   if( s[j]==word[a[k]][li] ){ b[bz++]=a[k];}
                  j++;
               }
               li++;
            }
            else{
              for(int k=0;k<az;k++)
                  if( s[j]==word[a[k]][li] ){ b[bz++]=a[k];} 
              li++;  
            }
            az=bz;  bz=0;
            if( !az) break;
            for(int k=0;k<az;k++) a[k]=b[k];
         }
         printf("Case #%d: %d\n",1+i,az);
    }
    return 0;
}
