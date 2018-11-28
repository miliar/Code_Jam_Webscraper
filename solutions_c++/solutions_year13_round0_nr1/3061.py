#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

int main ()
{
    char grid[4][5];
    unsigned int T, flag;
    cin>>T;
    for (int i=0;i<T;i++)
    {
        for (int j=0;j<4;j++)
            cin>>grid[j];
        int x, o, dot;
        x = o = dot = 0;
        for (int j=0;j<4;j++)
        {
            flag=1;
            for (int k=0;k<4;k++)
            {
                if (grid[j][k]=='.')
                {
                    dot++;
                    flag=0;
                    break;
                }
                else if (grid[j][k]=='X')
                {
                    x++;
                    if (o>0)
                    {
                        flag=0;
                        break;
                    }
                }
                else if (grid[j][k]=='O')
                {
                    o++;
                    if (x>0)
                    {
                        flag=0;
                        break;
                    }
                }
            }
            if (x>=3 && flag)
            {
                cout<<"Case #"<<i+1<<": X won\n";break;
            }
            else if (o>=3 && flag)
            {
                cout<<"Case #"<<i+1<<": O won\n";break;
            }
            else
                x=o=0;
        }
        if (x == 0 && o == 0)
        {
            for (int j=0;j<4;j++)
            {
                flag=1;
                for (int k=0;k<4;k++)
                {
                    if (grid[k][j]=='.')
                    {
                        dot++;
                        flag=0;
                        break;
                    }
                    else if (grid[k][j]=='X')
                    {
                        x++;
                        if (o>0)
                        {
                            flag=0;
                            break;
                        }
                    }
                    else if (grid[k][j]=='O')
                    {
                        o++;
                        if (x>0)
                        {
                            flag=0;
                            break;
                        }
                    }
                }
                if (x>=3 && flag)
                {
                    cout<<"Case #"<<i+1<<": X won\n";break;
                }
                else if (o>=3 && flag)
                {
                    cout<<"Case #"<<i+1<<": O won\n";break;
                }
                else
                    x=o=0;
            }
            flag=1;
            if (x==0 && o==0)
            {
                for (int j=0;j<4;j++)
                {
                        if (grid[j][j]=='.')
                        {
                            dot++;
                            flag=0;
                            break;
                        }
                        else if (grid[j][j]=='X')
                        {
                            x++;
                            if (o>0)
                            {
                                flag=0;
                                break;
                            }
                        }
                        else if (grid[j][j]=='O')
                        {
                            o++;
                            if (x>0)
                            {
                                flag=0;
                                break;
                            }
                        }
                }
                if (x>=3 && flag)
                {
                    cout<<"Case #"<<i+1<<": X won\n";
                }
                else if (o>=3 && flag)
                {
                    cout<<"Case #"<<i+1<<": O won\n";
                }
                else
                {
                   x=o=0;
                   flag=1;
                    for (int j=0;j<4;j++)
                    {
                            if (grid[j][3-j]=='.')
                            {
                                dot++;
                                flag=0;
                                break;
                            }
                            else if (grid[j][3-j]=='X')
                            {
                                x++;
                                if (o>0)
                                {
                                    flag=0;
                                    break;
                                }
                            }
                            else if (grid[j][3-j]=='O')
                            {
                                o++;
                                if (x>0)
                                {
                                    flag=0;
                                    break;
                                }
                            }
                    }
                    if (x>=3 && flag)
                    {
                        cout<<"Case #"<<i+1<<": X won\n";
                    }
                    else if (o>=3 && flag)
                    {
                        cout<<"Case #"<<i+1<<": O won\n";
                    }
                    else if (dot>0)
                    {
                        cout<<"Case #"<<i+1<<": Game has not completed\n";
                    }
                    else
                    {
                        cout<<"Case #"<<i+1<<": Draw\n";
                    }
                }
            }
        }
    }       
    return 0;
}
