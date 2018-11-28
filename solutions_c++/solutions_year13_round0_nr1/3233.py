#include<iostream>
using namespace std;

int main()
{
    int t,i,j,k,count1,count2;
    char board[4][4];
    cin>>t;
    k=1;
    start:
    while(k<=t)
    {
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>board[i][j];
            }
        }

        /*
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cout<<board[i][j];
            }
            cout<<endl;
        }
        */

        for(i=0;i<4;i++)
        {
            count1=0,count2=0;
            for(j=0;j<4;j++)
            {
                if(board[i][j]=='X')
                    count1++;
                else if(board[i][j]=='T')
                    count2++;
            }

            if((count1==3 && count2==1)||(count1==4))
            {
                cout<<"Case #"<<k<<": X won\n";
                k++;
                goto start;
            }
        }


        for(i=0;i<4;i++)
        {
             count1=0,count2=0;
            for(j=0;j<4;j++)
            {
                if(board[i][j]=='O')
                    count1++;
                else if(board[i][j]=='T')
                    count2++;
            }

            if((count1==3 && count2==1)||(count1==4))
            {
                cout<<"Case #"<<k<<": O won\n";
                k++;
                goto start;
            }
        }




        for(i=0;i<4;i++)
        {
            count1=0,count2=0;
            for(j=0;j<4;j++)
            {
                if(board[j][i]=='X')
                    count1++;
                else if(board[j][i]=='T')
                    count2++;
            }

            if((count1==3 && count2==1)||(count1==4))
            {
                cout<<"Case #"<<k<<": X won\n";
                k++;
                goto start;
            }
        }


        for(i=0;i<4;i++)
        {
             count1=0,count2=0;
            for(j=0;j<4;j++)
            {
                if(board[j][i]=='O')
                    count1++;
                else if(board[j][i]=='T')
                    count2++;
            }

            if((count1==3 && count2==1)||(count1==4))
            {
                cout<<"Case #"<<k<<": O won\n";
                k++;
                goto start;
            }
        }






        count1=0;count2=0;
        for(i=0;i<4;i++)
        {

            if(board[i][i]=='X')
                count1++;
            else if(board[i][i]=='T')
                count2++;
        }
        if((count1==3 && count2==1) || (count1==4))
        {
            cout<<"Case #"<<k<<": X won\n";
            k++;
            goto start;
        }


        count1=0;count2=0;
        for(i=3;i>=0;i--)
        {


            if(board[i][3-i]=='X')
                count1++;
            else if(board[i][3-i]=='T')
                count2++;
        }
        if((count1==3 && count2==1) || (count1==4))
        {
            cout<<"Case #"<<k<<": X won\n";
            k++;
            goto start;
        }


        count1=0;count2=0;
        for(i=0;i<4;i++)
        {
            if(board[i][i]=='O')
                count1++;
            else if(board[i][i]=='T')
                count2++;
        }
        if((count1==3 && count2==1) || (count1==4))
        {
            cout<<"Case #"<<k<<": O won\n";
            k++;
            goto start;
        }

         count1=0;count2=0;

        for(i=3;i>=0;i--)
        {

            if(board[i][3-i]=='O')
                count1++;
            else if(board[i][3-i]=='T')
                count2++;
        }
        if((count1==3 && count2==1) || (count1==4))
        {
            cout<<"Case #"<<k<<": O won\n";
            k++;
            goto start;
        }

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(board[i][j]=='.')
                {
                    cout<<"Case #"<<k<<": Game has not completed\n";
                    k++;
                    goto start;
                }
            }
        }

        cout<<"Case #"<<k<<": Draw\n";
        k++;

    }
    return 0;
}
