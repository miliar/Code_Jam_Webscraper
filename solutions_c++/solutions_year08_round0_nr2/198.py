/*
TASK: B_train
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

FILE *fin,*fout;
int t;
int na,nb;
int ta[1005][2],tb[1005][2];
int e[2005],g[2005],n;
multiset<int> atb,ata;


int comparez(const void *x, const void *y)
{
    return (*(int*)x - *(int*)y);
}


int main()
{
    int i,j,sss,ss,uu,vv,ww;
    int ra,rb;
    fin = fopen("B-large.in","r");
    fout = fopen("B-large.out","w");
    fscanf(fin,"%d",&ss);
    for(sss=1;sss<=ss;sss++)
    {
        printf("---%d---\n",sss);
        fscanf(fin,"%d",&t);
        fscanf(fin,"%d %d",&na,&nb);
        n = na+nb;
        for(i=0;i<na;i++)
        {
            fscanf(fin,"%d:%d",&uu,&vv);
            ta[i][0] = uu*60+vv;
            fscanf(fin,"%d:%d",&uu,&vv);
            ta[i][1] = uu*60+vv+t;
            //printf("A: %d %d\n",ta[i][0],ta[i][1]);
            g[i] = ((ta[i][0]*3000)+ta[i][1])*2;
            //e[i] = i;
        }
        for(i=0;i<nb;i++)
        {
            fscanf(fin,"%d:%d",&uu,&vv);
            tb[i][0] = uu*60+vv;
            fscanf(fin,"%d:%d",&uu,&vv);
            tb[i][1] = uu*60+vv+t;
            //printf("B: %d %d\n",tb[i][0],tb[i][1]);
            g[i+na] = ((tb[i][0]*3000)+tb[i][1])*2+1;
            //e[i+na] = i+na;
        }
        //printf("%d %d\n",uu,vv);
        qsort(g,n,sizeof(g[0]),comparez);
        ra = 0; rb = 0;
        atb.clear(); ata.clear();
        for(i=0;i<n;i++)
        {
            uu = g[i]/6000; vv = g[i]/2%3000;
            ww = g[i]&1;
            //printf("%d %d %d ",uu,vv,ww);
            if(ww) //b to a
            {
                if(atb.empty() || (*atb.begin()>uu)) rb++; //printf("*");}
                else atb.erase(atb.begin());
                ata.insert(vv);
            }
            else //a to b
            {
                if(ata.empty() || (*ata.begin()>uu)) ra++; //printf("*");}
                else ata.erase(ata.begin());
                atb.insert(vv);
            }
            //printf("\n");
        }
        fprintf(fout,"Case #%d: %d %d\n",sss,ra,rb);
        printf("Case #%d: %d %d\n",sss,ra,rb);
        //system("PAUSE");
    }
    system("PAUSE");
    return 0;
}
