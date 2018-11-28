#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;
char s[6][6];
int main()
{
    long int i,j,w,W;
    long int x,o,t,d,st;
    bool flag;
    cin>>w;
    W=w;
    while(w--)
    {
        for(i=0;i<4;i++)
        scanf("%s",s[i]);
        getchar();

        //for(i=0;i<4;i++)
        //printf("%s\n",s[i]);

        //checking rows
        flag=false;
        st=-1;

        x=t=d=o=0;
        for(i=0;i<4 && flag==false;i++)
        {
            x=o=t=0;
            for(j=0;j<4;j++)
            {
                switch(s[i][j])
                {
                    case 'X': x++;
                    break;
                    case 'O': o++;
                    break;
                    case 'T': t++;
                    break;
                    case '.': d++;
                    break;

                }
            }
            if(x+t==4)
            {
                flag=true;
                st=1;
                break;
            }
            if(o+t==4)
            {
                flag=true;
                st=2;
                break;
            }
        }

        //column
        for(i=0;i<4 && flag==false;i++)
        {
            x=o=t=0;
            for(j=0;j<4;j++)
            {
                switch(s[j][i])
                {
                    case 'X': x++;
                    break;
                    case 'O': o++;
                    break;
                    case 'T': t++;
                    break;
                    case '.': d++;
                    break;

                }
            }
            if(x+t==4)
            {
                flag=true;
                st=1;
                break;
            }
            if(o+t==4)
            {
                flag=true;
                st=2;
                break;
            }
        }
        //diagonals
        x=0;
        t=0;
        o=0;
        for(i=0;i<4 && flag==false;i++)
        {
            switch(s[i][i])
            {
                case 'X': x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                case '.': d++;
                break;

            }
        }
        if(x+t==4)
        {
            flag=true;
            st=1;
        }
        if(o+t==4)
        {
            flag=true;
            st=2;
        }

        x=0;
        t=0;
        o=0;
        for(i=3;i>=0 && flag==false;i--)
        {
            switch(s[i][3-i])
            {
                case 'X': x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                case '.': d++;
                break;

            }
        }
        if(x+t==4)
        {
            flag=true;
            st=1;
        }
        if(o+t==4)
        {
            flag=true;
            st=2;
        }

        if(st==1)
        {
            cout<<"Case #"<<W-w<<": X won\n";
            continue;
        }
        if(st==2)
        {
            cout<<"Case #"<<W-w<<": O won\n";
            continue;
        }
        if(st==-1 && d!=0)
        {
            cout<<"Case #"<<W-w<<": Game has not completed\n";
            continue;
        }
        if(st==-1 && d==0)
        {
            cout<<"Case #"<<W-w<<": Draw\n";
            continue;
        }
    }
    return 0;
}
