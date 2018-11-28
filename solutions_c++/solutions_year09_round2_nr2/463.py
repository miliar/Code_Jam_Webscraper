/*
TASK: B
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<set>
#include<algorithm>
#define INF 123456789

using namespace std;
FILE *fin,*fout;

inline int MAXX(int x,int y) {return x > y ? x : y ;}
inline int MINN(int x,int y) {return x < y ? x : y ;}

//-----------------------------------------------------

int tl;
char num[30];
int mui[30];
int a[10];

int comparez(const void *x, const void *y)
{
    return -(*(int*)x) + (*(int*)y);
}

int main()
{
    int i,j;
    fin = fopen("B-large.in","r");
    fout = fopen("nextlr.out","w");
    fscanf(fin,"%d",&tl);
    for(int tt=0;tt<tl;tt++)
    {
        for(i=0;i<30;i++) {num[i]=0; mui[i] = 0;}
        fscanf(fin,"%s",num);
        for(i=0;i<10;i++) a[i] = 0;
        int lenz = strlen(num);
        for(i=0;i<lenz;i++) a[num[i]-'0']++;
        //for(i=0;i<10;i++) printf("%d ",a[i]);
        for(i=0;i<lenz;i++) mui[i] = num[lenz-i-1] - '0';
        i = 0;
        while(mui[i] <= mui[i+1]) i++;
        //find the minimum
        j = 0;
        while(mui[j] <= mui[i+1] && j<=i) j++;
        printf("\n%d %d %d\n",tt,i,j);
        if(j>i)
        {
            printf("?"); system("PAUSE");
        }
        else
        {
            //swap
            int a;
            a = mui[j]; mui[j] = mui[i+1]; mui[i+1] = a;
            for(int ll=0;ll<5;ll++) printf("%d",mui[ll]); printf("\n");
            //sort
            qsort(mui,i+1,sizeof(mui[0]),comparez);
            for(int ll=0;ll<5;ll++) printf("%d",mui[ll]);
        }
        fprintf(fout,"Case #%d: ",tt+1);
        i = 29;
        while(mui[i]==0) i--;
        for(;i>=0;i--) fprintf(fout,"%d",mui[i]);
        fprintf(fout,"\n");
    }
    system("PAUSE");
    return 0;
}
