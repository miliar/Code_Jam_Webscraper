#include<iostream>
#include<fstream>

bool calc(int sum, int& eo, int p)
{
    int n=sum/3,diff=p-n,sp=sum%3;

    if(diff<=0) return 1;

    if(diff==1)
    {
        if(sp==0)
        {
            if(eo)
            {
                eo--;
                return 1;
            }
            else
                return 0;
        }

        if(sp==1 || sp==2)
        {
            return 1;
        }
    }
    if(diff==2)
    {
        if(eo && sp==2)
        {
            eo--;
            return 1;
        }

        if(sp==1 || sp==0)
            return 0;
    }

    return false;
}

int main(void)
{
    int T=0,nd,eo,p,sum,op;

    std::ifstream fin("B-large.in");
    std::ofstream fout("Output-gcj2-L.in");
    if(!fin || !fout)
    {
        printf("Erroro!");
        return 1;
    }

    //assert(fscanf(fin,"%d",&T)==1);
    fin>>T;

    for(int i=1;i<=T;i++)
    {
        nd=0,eo=0,p=0;
        //assert(fscanf(fin,"%d%d%d",&nd,&eo,&p)==3);
        fin>>nd>>eo>>p;

        op=0;

        for(int j=1;j<=nd;j++)
        {
            sum=0;

            //assert(fscanf(fin,"%d",&sum)==1);
            fin>>sum;

            if(sum==0 && p==0)
            {
                op++;
                continue;
            }
            if(sum!=0 && calc(sum,eo,p)) op++;
        }

        fout<<"Case #"<<i<<": "<<op;

        if(i!=T)
        fout<<"\n";
    }

    return 0;
}
