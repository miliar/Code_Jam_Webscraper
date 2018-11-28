#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

char f[32]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

string str;
char op[100];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    char ch=getchar();
    for(int tt=1;tt<=cases;tt++){
        getline(cin,str);
        int sz=str.size();
        //printf("size = %d\n",sz);
        for(int i=0;i<sz;i++){
            if(str[i]==' ') continue;
            else str[i]=f[str[i]-'a'];
        }
        op[sz]='\0';
        cout<<"Case #"<<tt<<": "<<str<<"\n";
    }
    return 0;
}
