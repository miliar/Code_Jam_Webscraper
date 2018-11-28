#include <iostream>

using namespace std;

char matrix[5][5];
int x,y;

int win(char ch)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(matrix[i][j]!=ch)
                break;
        }
        if(j==4)
            return 1;
    }
    for(j=0;j<4;j++)
    {
        for(i=0;i<4;i++)
        {
            if(matrix[i][j]!=ch)
                break;
        }
        if(i==4)
            return 1;
    }
    for(i=0,j=0;i<4;i++,j++)
        if(matrix[i][j]!=ch)
            break;
    if(i==4)
        return 1;
    for(i=0,j=3;i<4;i++,j--)
        if(matrix[i][j]!=ch)
            break;
    if(i==4)
        return 1;
    return 0;
}

int xwin()
{
    matrix[x][y]='X';
    return win('X');
}

int owin()
{
    matrix[x][y]='O';
    return win('O');
}

int main()
{
    int t;
    cin>>t;
    int i,j;
    int n=1;
    char ch;
    int complete;
    while(n<=t)
    {
        complete = 1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>ch;
                if(ch=='T')
                {
                    x=i;
                    y=j;
                }
                else if(ch=='.')
                {
                    complete = 0;
                }
                matrix[i][j]=ch;
            }
        }
        cout<<"Case #"<<n<<": ";
        if(xwin())
        {
            cout<<"X won"<<endl;
        }
        else if(owin())
        {
            cout<<"O won"<<endl;
        }
        else if(complete==1)
        {
            cout<<"Draw"<<endl;
        }
        else if(complete==0)
        {
            cout<<"Game has not completed"<<endl;
        }
        n++;
    }
    return 0;
}
