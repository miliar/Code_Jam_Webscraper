/*
TASK: A_universe
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<map>
#define INFINI 123456789

using namespace std;
map<string,int> m_chan;

FILE *fin,*fout;
int ans[105][1005];
int s,q;
char buff[105];
int b[1005];

int main()
{
    int ss,sss,i,j,k;
    int mini,uguu;
    //don't forget to change file name!
    fin = fopen("A-large.in.enc.txt","r");
    fout = fopen("A-large.out","w");
    fscanf(fin,"%d",&ss);
    for(sss=1;sss<=ss;sss++)
    {
        printf("--%d--\n",sss);
        m_chan.clear();
        fscanf(fin,"%d\n",&s);
        for(i=1;i<=s;i++)
        {
            fgets(buff,102,fin);
            //printf("%s",buff);
            m_chan.insert(pair<string,int>(buff,i));
        }
        fscanf(fin,"%d\n",&q);
        for(i=1;i<=q;i++)
        {
            fgets(buff,102,fin);
            b[i] = m_chan[buff];
            //printf("%d\n",b[i]);
        }
        for(i=0;i<105;i++) for(j=0;j<1005;j++) ans[i][j] = 0;
        ans[b[1]][1] = INFINI;
        
        for(j=2;j<=q;j++)
        {
            for(i=1;i<=s;i++)
            {
                if(i==b[j]) {ans[i][j] = INFINI; continue;}
                ans[i][j] = INFINI;
                for(k=1;k<=s;k++)
                {
                    if(k!=i) uguu = ans[k][j-1]+1;
                    else uguu = ans[k][j-1];
                    if(uguu<ans[i][j]) ans[i][j] = uguu;
                }
                //printf("ans[%d][%d] = %d\n",i,j,ans[i][j]);
            }
        }
        mini = INFINI;
        for(i=1;i<=s;i++)
        {
            if(mini>ans[i][q]) mini = ans[i][q];
        }
        fprintf(fout,"Case #%d: %d\n",sss,mini);
    }
    system("PAUSE");
    return 0;
}
