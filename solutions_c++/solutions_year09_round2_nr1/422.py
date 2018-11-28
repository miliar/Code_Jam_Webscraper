/*

TASK:
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
int comparez(const void *x, const void *y)
{
    return (*(int*)x - *(int*)y);
}

//-----------------------------------------------------

int tl;
int l,q;
int now;
char fea[10000][12];
char liz[10000][12];
double pp[10000];
int lx[10000],rx[10000];

int reader(int noa)
{
    char c;
    char temp[50],it;
    //number
    do {c = getc(fin);} while (c==10 || c==32);
    it = 0;
    do {temp[it++] = c; c = getc(fin);} while (c!=10 && c!=32 && c!=')');
    temp[it] = 0;
    sscanf(temp,"%lf",&pp[noa]);
    while (c==10 || c==32) {c = getc(fin);}
    //printf("%d %s %lf %d %d\n",noa,fea[noa],pp[noa],lx[noa],rx[noa]);
    if(c!=')')
    {
        //text
        it = 0;
        do {fea[noa][it++] = c; c = getc(fin);} while (c!=10 && c!=32);
        fea[noa][it] = 0;
        //printf("%d %s %lf %d %d\n",noa,fea[noa],pp[noa],lx[noa],rx[noa]);
        //tree
        do {c = getc(fin);} while (c!='(');
        now++;
        lx[noa] = now; reader(now);
        do {c = getc(fin);} while (c!='(');
        now++;
        rx[noa] = now; reader(now);
        do {c = getc(fin);} while (c!=')');
    }
    else {lx[noa] = -1; rx[noa] = -1;}
    //printf("%d %s %lf %d %d\n",noa,fea[noa],pp[noa],lx[noa],rx[noa]);
    //system("PAUSE");
    return 0;
}

int main()
{
    int i,j,jj;
    char temp[50],it;
    fin = fopen("A-large.in","r");
    fout = fopen("cutelr.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        fprintf(fout,"Case #%d:\n",tt+1);
        fscanf(fin,"%d",&l);
        char c;
        c = getc(fin);  //read \n = 10
        do {c = getc(fin);} while (c!='(');
        now = 0;
        reader(0);
        
        //for(i=0;i<10;i++) printf("%s %lf %d %d\n",fea[i],pp[i],lx[i],rx[i]);
        //system("PAUSE");
        fscanf(fin,"%d",&q);
        for(i=0;i<q;i++)
        {
            fscanf(fin,"%s %d",temp,&j);
            for( jj=0;jj<j;jj++) fscanf(fin,"%s",liz[jj]);
            double ans = 1.0;
            now = 0;
            while(1)
            {
                ans = ans * pp[now];
                if(lx[now]==-1) break;
                for( jj=0;jj<j;jj++) if(strcmp(fea[now],liz[jj])==0) break;
                if(jj<j) now = lx[now];
                else now = rx[now];
            }
            fprintf(fout,"%.9lf\n",ans);
        }
    }
    system("PAUSE");
    return 0;
}
