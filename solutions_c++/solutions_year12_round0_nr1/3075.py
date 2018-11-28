#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("asmall_out.txt","w",stdout);
    
    char mapping[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int i,t,tests;
    string s;
       
    scanf("%d",&tests);
    getchar();
    for(t=1;t<=tests;t++){        
        getline(cin,s);
        printf("Case #%d: ",t);
        for(i=0;i<s.length();i++){
            if(s[i]==' ') printf(" ");
            else printf("%c",mapping[s[i]-97]);
        }    
        printf("\n");
    }   
       
    //getchar();getchar();
    return 0;
}
