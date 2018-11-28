#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>
#include <locale>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main(void)
{
    ofstream cout ("A-small-attempt0.out");
    ifstream cin ("A-small-attempt0.in");
    int T;
    int Tno;
    int h,i,j;
    //int Txpos,Typos;
    bool start,stat,complete;
    char tempchar;
    string tictactoe[4];
    string ans;
    cin>>T;
    for(j=1;j<=T;j++)
    {
        complete=true;
        ans="";
        for(i=0;i<4;i++)    cin>>tictactoe[i];

        for(h=0;h<4;h++)
        {
            stat=false;
            start=true;
            Tno=0;
            for(i=0;i<4;i++)
            {
                if(tictactoe[h][i]=='.')
                {
                    complete=false;
                    stat=true;
                    break;
                }
                else if(tictactoe[h][i]=='T')
                {
                    Tno++;
                    if(Tno>1)
                    {
                        stat=true;
                        break;
                    }
                }
                else
                {
                    if(start)
                    {
                        tempchar=tictactoe[h][i];
                        start=false;
                    }
                    else
                    {
                        if(tictactoe[h][i]!=tempchar)
                        {
                            stat=true;
                            break;
                        }
                    }
                }
            }
            if(!stat)
            {
                ans+=tempchar;
                ans+=" won";
                break;
            }
        }
        if(stat)
        {
            for(i=0;i<4;i++)
            {
                stat=false;
                start=true;
                Tno=0;
                for(h=0;h<4;h++)
                {
                    if(tictactoe[h][i]=='.')
                    {
                        stat=true;
                        complete=false;
                        break;
                    }
                    else if(tictactoe[h][i]=='T')
                    {
                        Tno++;
                        if(Tno>1)
                        {
                            stat=true;
                            break;
                        }
                    }
                    else
                    {
                        if(start)
                        {
                            tempchar=tictactoe[h][i];
                            start=false;
                        }
                        else
                        {
                            if(tictactoe[h][i]!=tempchar)
                            {
                                stat=true;
                                break;
                            }
                        }
                    }
                }
                if(!stat)
                {
                    ans+=tempchar;
                    ans+=" won";
                    break;
                }
            }

            if(stat)
            {
                //cout<<"de\n";
                stat=false;
                start=true;
                Tno=0;
                for(i=0;i<4;i++)
                {
                    if(tictactoe[i][i]=='.')
                    {
                        stat=true;
                        break;
                    }
                    else if(tictactoe[i][i]=='T')
                    {
                        Tno++;
                        if(Tno>1)
                        {
                            stat=true;
                            break;
                        }
                    }
                    else
                    {
                        if(start)
                        {
                            tempchar=tictactoe[i][i];
                            start=false;
                        }
                        else
                        {
                            if(tictactoe[i][i]!=tempchar)
                            {
                                stat=true;
                                break;
                            }
                        }
                    }
                }
                if(!stat)
                {
                    //cout<<"de\n";
                    ans+=tempchar;
                    ans+=" won";
                    //cout<<ans;
                    //break;
                }
                else
                {
                    stat=false;
                    start=true;
                    Tno=0;
                    for(i=0;i<4;i++)
                    {
                        if(tictactoe[i][3-i]=='.')
                        {
                            stat=true;
                            break;
                        }
                        else if(tictactoe[i][3-i]=='T')
                        {
                            Tno++;
                            if(Tno>1)
                            {
                                stat=true;
                                break;
                            }
                        }
                        else
                        {
                            if(start)
                            {
                                tempchar=tictactoe[i][3-i];
                                start=false;
                            }
                            else
                            {
                                if(tictactoe[i][3-i]!=tempchar)
                                {
                                    stat=true;
                                    break;
                                }
                            }
                        }
                    }
                    if(!stat)
                    {
                        ans+=tempchar;
                        ans+=" won";
                        //break;
                    }
                    else
                    {
                        if(complete)    ans="Draw";
                        else            ans="Game has not completed";
                    }
                }
            }
        }

        cout<<"Case #"<<j<<": "<<ans<<"\n";
    }

    return 0;
}
