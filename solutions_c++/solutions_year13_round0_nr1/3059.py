#include <fstream>
#include<iostream>
#include <string.h>

using namespace std;

int main()
{
    int nc,k=0;
    ifstream cinner("A-large.in",ios::in);
    cinner>>nc;
    cout<<nc;
    cinner.get();
    ofstream coutter("out.txt",ios::out);
    for(; k<nc; k++)
    {
        char state[1000][4];
        int x=0,o=0,t=0,d=0,flag=-1,D=0;
        //Hori check
        for(int i=0; i<4; i++)
        {
            cinner.getline(state[i],5);
            cout<<state[i]<<'\n';
            x=0,o=0,t=0,d=0;
            for(int j=0; j<4; j++)
            {
                if(state[i][j]=='.')
                {
                    d++;
                    D++;

                    break;
                }
                else if(state[i][j]=='X')
                {
                    x++;
                }
                else if(state[i][j]=='O')
                    o++;
                else if(state[i][j]=='T')
                    t++;
            }
            if(d)
            {
                continue;
            }
            else if(x+t==4)
            {
                flag=3;
                continue;
            }
            else if(o+t==4)
            {
                flag=4;
                continue;
            }

        }
        //Vert check
        if(flag==-1)
        {
            for(int j=0; j<4; j++)
            {
                x=0,o=0,t=0,d=0;
                for(int i=0; i<4; i++)
                {
                    if(state[i][j]=='.')
                    {
                        d++;
                        D++;

                        break;
                    }
                    else if(state[i][j]=='X')
                        x++;
                    else if(state[i][j]=='O')
                        o++;
                    else if(state[i][j]=='T')
                        t++;
                }
                if(d)
                {
                    continue;
                }
                else if(x+t==4)
                {
                    flag=3;
                    continue;
                }
                else if(o+t==4)
                {
                    flag=4;
                    continue;
                }
            }
        }
        x=0,o=0,t=0,d=0;
        //Diag check
        if(flag==-1)
        {
            for(int j=0; j<4; j++)
            {
                if(state[j][j]=='.')
                {
                    d++;
                    D++;

                    break;
                }
                else if(state[j][j]=='X')
                    x++;
                else if(state[j][j]=='O')
                    o++;
                else if(state[j][j]=='T')
                    t++;
            }
            if(d);
            else if(x+t==4)
            {
                flag=3;

            }
            else if(o+t==4)
            {
                flag=4;

            }
        }
        x=0,o=0,t=0,d=0;
        if(flag==-1)
        {
            for(int j=0; j<4; j++)
            {
                if(state[j][3-j]=='.')
                {
                    d++;
                    D++;

                    break;
                }
                else if(state[j][3-j]=='X')
                    x++;
                else if(state[j][3-j]=='O')
                    o++;
                else if(state[j][3-j]=='T')
                    t++;
            }
            if(d);
            else if(x+t==4)
            {
                flag=3;

            }
            else if(o+t==4)
            {
                flag=4;

            }
        }
        //Checks
        if(flag==-1)
        {
            if(D)flag=1;
            else flag=2;
        }
        //cout<<flag;

        switch(flag)
        {

        case 1:
            coutter<<"Case #"<<k+1<<": Game has not completed\n";
            break;
        case 2:
            coutter<<"Case #"<<k+1<<": Draw\n";
            break;
        case 3:
            coutter<<"Case #"<<k+1<<": X won\n";
            break;
        case 4:
            coutter<<"Case #"<<k+1<<": O won\n";
            break;
        }
        cinner.get();
    }
    return 0;
}
