#include<fstream>
#include<iostream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fout.open("tic_tac_toe_tomek.txt");
    fin.open("A-small-attempt1.in");
    int T,i,j,k,ctr,l,x,y,ctrH=0,ctrV=0,ctrD1=0,ctrD2=0;
    char a[4][4],sp;
    fin>>T;
    for(k=1;k<=T;k++)
    {
        ctr=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>a[i][j];
                if(a[i][j]=='.')
                ctr++;
            }
        }
        //fin>>sp;
        for(l=0;l<4;l++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]!='.')
                {
                    x=l,y=j;
                    ctrH=0,ctrV=0,ctrD1=0,ctrD2=0;
                    for(i=0;i<4;i++)
                    {
                        if(i!=y)
                        {
                            if(a[x][i]=='T')
                            ctrH++;
                            else if(a[x][i]==a[x][y])
                            ctrH++;
                        }
                        if(i!=x)
                        {
                            if(a[x][i]=='T')
                            ctrV++;
                            else if(a[i][y]==a[x][y])
                            ctrV++;
                        }

                        if(x==y)
                        {
                            if(i!=x)
                            {
                            if(a[i][i]=='T')
                            ctrD1++;
                            else if(a[i][i]==a[x][y])
                            ctrD1++;
                            }
                        }
                        if(x+y==3)
                        {
                            if((i!=x)||(3-i!=y))
                            {
                            if(a[i][3-i]=='T')
                            ctrD2++;
                            else if(a[i][3-i]==a[x][y])
                            ctrD2++;
                            }
                        }
                    }
                    if(ctrV==3||ctrH==3||ctrD1==3||ctrD2==3)
                    {
                        if(a[x][y]=='X'||a[x][y]=='O')
                        {
                            fout<<"Case #"<<k<<": "<<a[x][y]<<" won\n";
                            goto end;
                        }
                    }
                }
            }
        }
        if(ctr==0)
        fout<<"Case #"<<k<<": Draw\n";
        else
        fout<<"Case #"<<k<<": Game has not completed\n";
        end:;
    }
    fin.close();
    fout.close();
    return 0;
}
