#include <iostream>

using namespace std;

const char *x_w="X won",*draw="Draw",*y_w="O won",*not_c="Game has not completed";
void check();
int main()
{
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++)
    {
        cout<<"Case #"<<i<<": ";
        check();
    }
}

void check()
{
    char *line[4];
    line[0]=new char[4];
    line[1]=new char[4];
    line[2]=new char[4];
    line[3]=new char[4];
    cin>>line[0]>>line[1]>>line[2]>>line[3];
    bool empties=false;
    int x_count=0,y_count=0;
    for(int i=0;i<4;i++)
    {
        x_count=0,y_count=0;
        for(int j=0;j<4;j++)
        {
            switch(line[i][j])
            {
                case 'X':x_count++;break;
                case 'O':y_count++;break;
                case 'T':x_count++;y_count++;break;
                case '.':empties=true;
            }
            if(x_count==4)
            {
                cout<<x_w<<'\n';
                return;
            }
            if(y_count==4)
            {
                cout<<y_w<<'\n';
                return;
            }
        }
    }

    for(int i=0;i<4;i++)
    {
        x_count=0,y_count=0;
        for(int j=0;j<4;j++)
        {
            switch(line[j][i])
            {
                case 'X':x_count++;break;
                case 'O':y_count++;break;
                case 'T':x_count++;y_count++;break;
                case '.':empties=true;
            }
            if(x_count==4)
            {
                cout<<x_w<<'\n';
                return;
            }
            if(y_count==4)
            {
                cout<<y_w<<'\n';
                return;
            }
        }
    }

    x_count=0,y_count=0;

    for(int i=0;i<4;i++)
    {
      switch(line[i][i])
            {
                case 'X':x_count++;break;
                case 'O':y_count++;break;
                case 'T':x_count++;y_count++;break;
                case '.':empties=true;
            }
            if(x_count==4)
            {
                cout<<x_w<<'\n';
                return;
            }
            if(y_count==4)
            {
                cout<<y_w<<'\n';
                return;
            }
    }
    x_count=0,y_count=0;

    for(int i=0;i<4;i++)
    {
      switch(line[3-i][i])
            {
                case 'X':x_count++;break;
                case 'O':y_count++;break;
                case 'T':x_count++;y_count++;break;
                case '.':empties=true;
            }
            if(x_count==4)
            {
                cout<<x_w<<'\n';
                return;
            }
            if(y_count==4)
            {
                cout<<y_w<<'\n';
                return;
            }
    }
    if(empties)
        cout<<not_c<<'\n';
    else
        cout<<draw<<'\n';
    return;
}
