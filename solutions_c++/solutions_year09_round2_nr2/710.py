#include <iostream>
#include <algorithm>
using namespace std;
char s[1000];
int x;

void tuker(int a,int b){
     char tmp2=s[a];
     s[a]=s[b];
     s[b]=tmp2;
     
     }
     
int main(){int T;
freopen("B2.txt","r",stdin);
freopen("B.out","w",stdout);
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++){
    s[0]='0';
    scanf("%s",s+1);
    
    x=strlen(s);
    //cout<<x<<endl;
    int z=x-2;
    while (z>0 && s[z]>=s[z+1]) z--;
   // cout<<z<<endl;
    char tmp='9'+1;
    int ind=9999;
      for (int i=x-1;i>z;i--)
      if (tmp>s[i] && s[i]>s[z]){tmp=s[i]; ind=i;}

    //cout<<ind<<endl;
    if (ind==9999) {cout<<"Case #"<<ii<<": ";
    cout<<s[0];
    cout<<0;
    for (int i=1;i<x;i++)
    printf("%c",s[i]);
    
    printf("\n");
                 } else
    {
                 tuker(ind,z);
    sort(s+z+1,s+x);
    
                 cout<<"Case #"<<ii<<": ";
                 if (s[0]!='0') cout<<s[0];
                 for (int i=1;i<x;i++)
    printf("%c",s[i]);
    
    printf("\n");             
}
    
    }
    //system("pause");
    }
