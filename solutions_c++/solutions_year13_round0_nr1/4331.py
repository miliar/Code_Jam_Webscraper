#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstdio>
using namespace std;

int main()
{
    int kase=1,i,T;
    string s1[5];

    freopen("ALarge.in","r",stdin);
    freopen("ALarge.out","w",stdout);

    cin>>T;

    while(T--)
    {

        cin>>s1[0]>>s1[1]>>s1[2]>>s1[3];

        int winO=0,winX=0;

        //for O
        int ansO=4*('O');
        int ans2=3*('O')+'T';
        int ansX=4*('X');
        int ans3=3*('X')+'T';

        int diag=0;
        int reversediag=0,rd=3;

        for(i=0;i<4;i++)
        {   int value=0;

            diag+=s1[i][i];
            reversediag+=s1[i][rd];

            for(int j=0;j<4;j++)
            {
                value+=(s1[i][j]);
            }

            if(value== ansO || value==ans2)
            {
                winO=1;
            }
            if(value==ansX || value==ans3)
            {
                winX=1;
            }

            value=0;

            for(int j=0;j<4;j++)
            {
                value+=s1[j][i];
            }
            if(value== ansO || value==ans2)
            {
                winO=1;
            }

            if(value==ansX || value==ans3)
            {
                winX=1;
            }
            rd--;
        }

        if(diag==ansO || diag==ans2)
        {
            winO=1;
        }
        if(reversediag==ansO || reversediag==ans2)
        {
            winO=1;
        }
        //for X
        if(diag==ansX || diag==ans3)
        {
            winX=1;
        }
        if(reversediag==ansX || reversediag==ans3)
        {
            winX=1;
        }

        if(winX==0 && winO==0)
        {
            int c=0;
            for(i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    if(s1[i][j]=='.')
                        {
                            c=1;
                            break;
                        }
                }
                if(c==1)break;
            }

            if(c==1)
            {
                printf("Case #%d: Game has not completed\n",kase);
            }

            else if(c==0)
            {
               printf("Case #%d: Draw\n",kase);
            }
        }
        else if(winX==1)
        {
            printf("Case #%d: X won\n",kase);
        }
        else if(winO==1)
        {
            printf("Case #%d: O won\n",kase);
        }
        kase++;
    }

    return 0;
}

