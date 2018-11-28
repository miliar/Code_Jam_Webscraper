#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
char s[109];
int n,tran[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{    
    int cas=0,T;
    cin>>T;
    gets(s);
    while(T--){
        gets(s);
        for(int i=0;s[i];i++) if(s[i]!=' ') s[i]=tran[s[i]-'a']+'a';
        printf("Case #%d: %s\n",++cas,s);
    }    
}
