#include <iostream>
#include<string>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<fstream>
#include<vector>
using namespace std;


int main()
{
    ofstream fout ("aman.out");
    ifstream fin ("A-large.in");
    int t,case_no,i,j;
    vector< string > inp(4);
    vector< int > rowx(4),rowo(4),rowt(4),colx(4),colo(4),colt(4);
    int diag1x,diag1o,diag1t;
    int  diag2x,diag2o,diag2t;
    int dot;

    //fin>>t;
    fin>>t;

    for(case_no=1;case_no<=t;case_no++)
    {
        inp.clear();
        inp.resize(4);
        for(i=0;i<4;i++)
        {
            //fin>>inp[i];
            fin>>inp[i];

        }
        for(i=0;i<4;i++)
        {
            rowx[i]=0;
            rowo[i]=0;rowt[i]=0;colx[i]=0;colo[i]=0;colt[i]=0;
            diag1x=0;diag1o=0;diag1t=0;
            diag2x=0;diag2o=0;diag2t=0;
            dot=0;

        }

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(inp[i][j]=='X')
                {
                    rowx[i]++;
                }
                if(inp[i][j]=='O')
                {
                    rowo[i]++;
                }
                if(inp[i][j]=='T')
                {
                    rowt[i]++;
                }
                if(inp[i][j]=='.')
                {
                    dot=1;
                }
            }

        }
        for(j=0;j<4;j++)
        {
            for(i=0;i<4;i++)
            {
                if(inp[i][j]=='X')
                {
                    colx[j]++;
                }
                if(inp[i][j]=='O')
                {
                    colo[j]++;
                }
                if(inp[i][j]=='T')
                {
                    colt[j]++;
                }
            }

        }
        for(i=0;i<4;i++)
        {
            if(inp[i][i]=='X')
            {
                diag1x++;
            }
            if(inp[i][i]=='O')
            {
                diag1o++;
            }
            if(inp[i][i]=='T')
            {
                diag1t++;
            }
            if(inp[i][3-i]=='X')
            {
                diag2x++;
            }
            if(inp[i][3-i]=='O')
            {
                diag2o++;
            }
            if(inp[i][3-i]=='T')
            {
                diag2t++;
            }

        }
        int flag=-1;//INDICATES NO ONE HAS BEEN CONFIRMED TO WIN
        // CHECK X wins

        for(i=0;i<4&&flag==-1;i++)
        {
            if(rowx[i]==4||rowx[i]==3 &&rowt[i]==1)
            {
                flag=1;
                break;
            }
        }
        for(i=0;i<4&&flag==-1;i++)
        {
            if(colx[i]==4||colx[i]==3 &&colt[i]==1)
            {
                flag=1;
                break;
            }
        }
        if(flag!=1)
        {
            if(diag1x==4||diag1x==3 &&diag1t==1)
               {
                  flag=1;
               }
        }
        if(flag!=1)
        {
            if(diag2x==4||diag2x==3 &&diag2t==1)
               {
                  flag=1;
               }
        }
        if(flag==1)
        {
            fout<<"Case #"<<case_no<<":"<<" X won\n";
            continue;
        }
        for(i=0;i<4&&flag==-1;i++)
        {
            if(rowo[i]==4||rowo[i]==3 &&rowt[i]==1)
            {
                flag=2;
                break;
            }
        }
        for(i=0;i<4&&flag==-1;i++)
        {
            if(colo[i]==4||colo[i]==3 &&colt[i]==1)
            {
                flag=2;
                break;
            }
        }
        if(flag!=2)
        {
            if(diag1o==4||diag1o==3 &&diag1t==1)
               {
                  flag=2;
               }
        }
        if(flag!=2)
        {
            if(diag2o==4||diag2o==3 &&diag2t==1)
               {
                  flag=2;
               }
        }
        if(flag==2)
        {
            fout<<"Case #"<<case_no<<":"<<" O won\n";
            continue;
        }
        if(dot==1)
        {
             fout<<"Case #"<<case_no<<":"<<" Game has not completed\n";
        }
        else
        {
            fout<<"Case #"<<case_no<<":"<<" Draw\n";
        }


    }
    return 0;
}
