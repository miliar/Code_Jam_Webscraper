#include<iostream>
#include<unistd.h>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<algorithm>

using namespace std;

char arr[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w'
,'j','p','f','m','a','q'};

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    getchar();
    char a[100000];
    for(int i=1;i<=t;i++)
    {
        gets(a);
        printf("Case #%d: ",i);
        int len=strlen(a);
        for(int j=0;j<len;j++)
        {
            if(isalpha(a[j]))
            {
                a[j]=arr[a[j]-'a'];
            }
        }
        printf("%s\n",a);

    }

    return 0;
}
