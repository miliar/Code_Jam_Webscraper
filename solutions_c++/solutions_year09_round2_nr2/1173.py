#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

char str[30];
char temp[30];
char ret[30];

int main()
{
    FILE *in=fopen("nex.in","r");
    freopen("nex.out","w",stdout);
    int tests;
    fscanf(in,"%d",&tests);
    for (int test=1;test<=tests;test++)
    {
        printf("Case #%d: ",test);
        fscanf(in,"%s",str);
        int n=strlen(str);
        int c,c2;
        memcpy(temp,str,sizeof(str));
        sort(temp,temp+n);
        reverse(temp,temp+n);
        if (strcmp(temp,str))
        {
            next_permutation(str,str+n);
            printf("%s\n",str);   
        }
        else
        {
            reverse(temp,temp+n);
            for (c=0;c<n;c++)
            if (temp[c]!='0')break;
            ret[0]=temp[c];
            for (c2=0;c2<c;c2++)ret[c2+1]=temp[c2];
            ret[c2+1]='0';
            for (c2=c+2;c2<=n;c2++)ret[c2]=temp[c2-1];
            ret[n+1]='\0';
            printf("%s\n",ret);
        }
    }
//    system("pause");
    return 0;
}
