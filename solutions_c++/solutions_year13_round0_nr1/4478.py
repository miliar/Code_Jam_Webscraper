#include<iostream>
#include<fstream>
using namespace std;
int checkWinner(char arr[4][4]);
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("a-large.txt");
    int cases;
    fin>>cases;
    for(int z=1;z<=cases;z++)
    {
        char arr[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                fin>>arr[i][j];
            }
        }

        fout<<"Case #"<<z<<": ";
        int winner=checkWinner(arr);
        if(winner==1)
            fout<<"X won"<<endl;
        else if(winner==2)
            fout<<"O won"<<endl;
        else if(winner==3)
            fout<<"Draw"<<endl;
        else
            fout<<"Game has not completed"<<endl;

    }
}

int checkWinner(char arr[4][4])
{
    char a;
    int count,flag;
    bool incomplete=false;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]=='.')
                incomplete=true;
            a=arr[i][j];
            if(a=='.' || a=='T')
                continue;
            //vertical check
            count=0;flag=0;
            for(int k=0;k<4;k++)
            {
                if(arr[k][j]==a)
                    count++;
                else if(arr[k][j]=='T' && flag==0)
                {
                    flag++;
                    count++;
                }
            }
            if(count==4)
            {
                if(a=='X')
                    return 1;
                else
                    return 2;
            }
            //horizontal check
            count=0,flag=0;
            for(int k=0;k<4;k++)
            {
                if(arr[i][k]==a)
                    count++;
                else if(arr[i][k]=='T' && flag==0)
                {
                    flag++;
                    count++;
                }
            }
            if(count==4)
            {
                if(a=='X')
                    return 1;
                else
                    return 2;
            }
            //diagonal check
            if((i==0 && j==0)||(i==3 && j==3))
            {
                count=0;flag=0;
                for(int k=0;k<4;k++)
                {
                    if(arr[k][k]==a)
                    count++;
                    else if(arr[k][k]=='T' && flag==0)
                    {
                        flag++;
                        count++;
                    }
                }
                if(count==4)
                {
                    if(a=='X')
                    return 1;
                    else
                    return 2;
                }
            }
            if((i==0 && j==3)||(i==3 && j==0))
            {
                count=0;flag=0;
                for(int k=0;k<4;k++)
                {
                    if(arr[3-k][k]==a)
                    count++;
                    else if(arr[3-k][k]=='T' && flag==0)
                    {
                        flag++;
                        count++;
                    }
                }
                if(count==4)
                {
                    if(a=='X')
                    return 1;
                    else
                    return 2;
                }
            }

        }
    }
    if(incomplete)
        return 4;
    else
        return 3;
}
