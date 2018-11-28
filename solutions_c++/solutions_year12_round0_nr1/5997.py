#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
using namespace std;
int a[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
int main()
{
    int t;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    scanf("%d\n",&t);
    char str[105];
    for(int cc=1;cc<=t;cc++)
    {
            gets(str);
            printf("Case #%d: ",cc);
            for(int i=0;str[i]!='\0';i++)
            if(str[i]>='a'&&str[i]<='z')
            str[i]=a[str[i]-'a']+'a';
            printf("%s\n",str);
    }
}
