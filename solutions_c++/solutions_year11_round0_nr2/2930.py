#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <cstring>
using namespace std;

int cmap[30][30];
int cmap2[30][30];
char str[10];
char handle[200];
char temp[300];
char ans[300];
int len;
int lentemp;

int index(char c)
{
    return (int)(c-'A'+1);
}
char fromindex(int i)
{
    return (char)(i+'A'-1);
}

bool find(int start)
{
    for(int i=0;i<lentemp;i++)
    {
        if(cmap2[index(temp[i])][index(handle[start])]==1)
            return true;
    }
    return false;
}

int main()
{
    int a,b;
    int n;
    int cntt=0;
    FILE *in=fopen("B-large.in","r");
    FILE *out=fopen("B-large.out","w");
    fscanf(in,"%d",&n);
    //scanf("%d",&n);
    while(n--)
    {
        cntt++;
        memset(cmap,0,sizeof(cmap));
        memset(cmap2,0,sizeof(cmap2));
        fscanf(in,"%d",&a);
        //scanf("%d",&a);
        for(int i=0;i<a;i++)
        {
            fscanf(in,"%s",str);
            //scanf("%s",str);
            cmap[index(str[0])][index(str[1])]=index(str[2]);
            cmap[index(str[1])][index(str[0])]=index(str[2]);
        }
        fscanf(in,"%d",&b);
        //scanf("%d",&b);
        for(int i=0;i<b;i++)
        {
            fscanf(in,"%s",str);
            //scanf("%s",str);
            cmap2[index(str[0])][index(str[1])]=1;
            cmap2[index(str[1])][index(str[0])]=1;
        }

        fscanf(in,"%d",&len);
        fscanf(in,"%s",handle);
        //scanf("%d",&len);
        //scanf("%s",handle);
        lentemp=0;
        int k;
        if(len>0) temp[lentemp++]=handle[0];
        for(int i=1;i<len;i++)
        {
            if(lentemp>0 && cmap[index(temp[lentemp-1])][index(handle[i])]!=0)
            {
                temp[lentemp-1]=fromindex(cmap[index(temp[lentemp-1])][index(handle[i])]);
                continue;
            }
            if(find(i))
            {
                lentemp=0;
                continue;
            }
            temp[lentemp++]=handle[i];
        }
        int anslen=0;
        ans[anslen++]='[';
        for(int i=0;i<lentemp-1;i++)
        {
            ans[anslen++]=temp[i];
            ans[anslen++]=',';
            ans[anslen++]=' ';
        }
        if(lentemp>=1)
            ans[anslen++]=temp[lentemp-1];
        ans[anslen++]=']';
        ans[anslen++]='\0';
        fprintf(out,"Case #%d: %s\n",cntt,ans);
        //printf("Case #%d: %s\n",cntt,ans);
    }
    return 0;
}
