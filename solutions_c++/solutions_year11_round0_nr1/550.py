#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    FILE *fin;
    FILE *fout;
    fin=fopen("A-large.in","r");
    fout=fopen("A-large.out","w");
    int t,n,des,lastdes,part,pos[2],time;
    char robot;
    bool turn,laststep;
    fscanf(fin,"%d",&t);
    //cin>>t;
    for (int i=1;i<=t;++i)
    {
        fscanf(fin,"%d",&n);
        //cin>>n;
        pos[0]=1;
        pos[1]=1;
        part=0;
        time=0;
        for(int j=1;j<=n;++j)
        {
            fscanf(fin," %c%d",&robot,&des);
            //cin>>robot>>des;
            if(robot=='O')
                turn=0;
            else
                turn=1;
            if(j==1)
                laststep=turn;
            if(turn==laststep)
            {
                part=part+abs(des-pos[turn])+1;
                pos[turn]=des;
                continue;
            }
            
            if(part>=abs(des-pos[turn])+1)
            {
                time=time+part;
                pos[turn]=des;
                part=1;
                laststep=turn;
            }
            else
            {
                time=time+part;
                if(des-pos[turn]>=0)
                    pos[turn]=pos[turn]+part;
                else
                    pos[turn]=pos[turn]-part;
                part=abs(des-pos[turn])+1;
                pos[turn]=des;
                laststep=turn;
            }
        }
        time=time+part;
        fprintf(fout,"Case #%d: %d\n",i,time);
        //cout<<time<<endl;
    }
}
