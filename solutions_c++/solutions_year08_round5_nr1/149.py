/*
TASK: A
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;
vector<int> lir[6010],lic[6010];

FILE *fin,*fout;
int n,m;
int l;
char map[6010][6010];
char s[35];
int t;

int main()
{
    int i,j,jj,cnt;
    int ss,sss;
    int xx,yy,di,lenz;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.out","w");
    fscanf(fin,"%d",&sss);
    for(ss=1;ss<=sss;ss++)
    {
        printf("----- %d -----\n",ss);
        fprintf(fout,"Case #%d: ",ss);
        memset(map,0,sizeof map);
        xx = 3002; yy = 3002; di = 0;
        for(i=0;i<6010;i++) {lir[i].clear(); lic[i].clear();}
        fscanf(fin,"%d",&l);
        for(i=0;i<l;i++)
        {
            fscanf(fin,"%s %d",s,&t);
            lenz = strlen(s);
            for(j=0;j<t;j++)
            {
                for(jj=0;jj<lenz;jj++)
                {
                    if(s[jj]=='L') di = (di+3)%4;
                    else if(s[jj]=='R') di = (di+1)%4;
                    else if(s[jj]=='F')
                    {
                        if(di==0)
                        {
                            lir[yy].push_back(xx); yy++;
                        }
                        else if(di==1)
                        {
                            lic[xx].push_back(yy); xx++;
                        }
                        else if(di==2)
                        {
                            yy--; lir[yy].push_back(xx);
                        }
                        else if(di==3)
                        {
                            xx--; lic[xx].push_back(yy);
                        }
                    }
                }
            }
        }
        cnt = 0;
        int uuu,pp;
        vector<int>::iterator itr,itr2;
        for(i=0;i<6010;i++)
        {
            sort(lic[i].begin(),lic[i].end());
            uuu = lic[i].size();
            for(pp=1;pp+1<uuu;pp+=2)
            {
                for(j=lic[i][pp];j<lic[i][pp+1];j++)
                {
                        map[i][j] = 1; cnt++;
                }
            }
        }
        for(i=0;i<6010;i++)
        {
            sort(lir[i].begin(),lir[i].end());
            uuu = lir[i].size();
            for(pp=1;pp+1<uuu;pp+=2)
            {
                
                for(j=lir[i][pp];j<lir[i][pp+1];j++)
                {
                    if(!map[j][i])
                    {
                        map[j][i] = 1; cnt++;
                    }
                }
            }
        }
        fprintf(fout,"%d\n",cnt);
    }
    system("PAUSE");
    return 0;
}
