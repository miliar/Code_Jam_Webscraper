#include<iostream>
#include<cstdio>
#include<string>
#include<vector>

using namespace std;

int T,N,K;
int O[55];

int main()
{
    cin>>T;

    for(int CASO=1;CASO<=T;CASO++)
    {
        cin>>N>>K;

        vector<string> M(N);

        for(int i=0;i<N;i++)
            cin>>M[i];

        for(int i=0;i<N;i++)
        {
            int last=N-1;

            for(int j=N-1;j>=0;j--)
            {
                if(M[i][j]!='.')
                {
                    M[i][last]=M[i][j];

                    if(last!=j)
                        M[i][j]='.';

                    last--;
                }
            }
        }

        bool bluewon=false,redwon=false;

        // rows
        for(int i=0;i<N;i++)
        {
            int bluek=0,redk=0;

            for(int j=0;j<N;j++)
            {
                if(M[i][j]=='.')
                {
                    bluek=redk=0;
                }
                else if(M[i][j]=='R')
                {
                    bluek=0;
                    redk++;

                    if(redk>=K)
                        redwon=true;
                }
                else
                {
                    redk=0;
                    bluek++;

                    if(bluek>=K)
                        bluewon=true;
                }
            }
        }

        // cols
        for(int j=0;j<N;j++)
        {
            int bluek=0,redk=0;

            for(int i=0;i<N;i++)
            {
                if(M[i][j]=='.')
                {
                    bluek=redk=0;
                }
                else if(M[i][j]=='R')
                {
                    bluek=0;
                    redk++;

                    if(redk>=K)
                        redwon=true;
                }
                else
                {
                    redk=0;
                    bluek++;

                    if(bluek>=K)
                        bluewon=true;
                }
            }
        }

        // diag
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                int x=i,y=j;
                int bluek=0,redk=0;

                do
                {
                    if(M[x][y]=='.')
                    {
                        bluek=redk=0;
                    }
                    else if(M[x][y]=='R')
                    {
                        bluek=0;
                        redk++;

                        if(redk>=K)
                            redwon=true;
                    }
                    else
                    {
                        redk=0;
                        bluek++;

                        if(bluek>=K)
                            bluewon=true;
                    }

                    x++;
                    y++;
                }
                while(x<N&&y<N);

                x=i;
                y=j;
                bluek=0,redk=0;

                do
                {
                    if(M[x][y]=='.')
                    {
                        bluek=redk=0;
                    }
                    else if(M[x][y]=='R')
                    {
                        bluek=0;
                        redk++;

                        if(redk>=K)
                            redwon=true;
                    }
                    else
                    {
                        redk=0;
                        bluek++;

                        if(bluek>=K)
                            bluewon=true;
                    }

                    x++;
                    y--;
                }
                while(x<N&&y>=0);
            }
        }

        string result;

        if(bluewon&&redwon)
            result="Both";
        else if(bluewon)
            result="Blue";
        else if(redwon)
            result="Red";
        else
            result="Neither";

        printf("Case #%d: %s\n", CASO, result.c_str());
    }
}
