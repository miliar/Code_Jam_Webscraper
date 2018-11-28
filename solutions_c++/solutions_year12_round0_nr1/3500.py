#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

char a[30]="yhesocvxduiglbkrztnwjpfmaq";
char s[10005];
int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&p);
    getchar();
    for1(o,1,p+1){
         gets(s);
         l=strlen(s);
         printf("Case #%d: ",o);
         for1(i,0,l)
           if(s[i]==' ') printf(" ");
            else printf("%c",a[s[i]-97]);
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
