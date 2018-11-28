#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

#define ll long long
#define MM  1000


int main()
{   int N,C=1;
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
char a[] ={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    scanf("%d\n",&N); 
    
    while(N--)
{

char b[110];
gets(b);
printf("Case #%d: ",C);
C++;
for(int i=0;b[i]!=0;i++)
{
        if(b[i]==' ')
        printf(" ");
        else
        {
            printf("%c",a[b[i]-97]);
            }
}
            

printf("\n");







}



//system("pause");
return 0;
}
