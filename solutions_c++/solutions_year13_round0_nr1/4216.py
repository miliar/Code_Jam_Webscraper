#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    string s[4],t1;
    ifstream fin;
    ofstream fout;
    fin.open("cji1.txt");
    fout.open("cjo1.txt");
    int t,i,j,flag=0;
    fin>>t;
    getline(fin,s[0]);
    for(i=0;i<t;i++)
    {
        flag=0;
        for(j=0;j<4;j++)
        {
            getline(fin, s[j]);
            if(s[j][0]=='.' || s[j][1]=='.' || s[j][2]=='.' || s[j][3]=='.')
                flag=1;
        }
        getline(fin,t1);
        for(j=0;j<4;j++)
        {


            if(s[j][0]=='T' || s[j][1]=='T' || (s[j][0]==s[j][1] && s[j][0]!='.'))
            {
                if(s[j][0]=='T')
                {
                    if(s[j][1]==s[j][2] && s[j][2]==s[j][3] && s[j][1]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[j][1]<<" won"<<endl;
                        break;
                    }
                }
                else if(s[j][1]=='T')
                {
                    if(s[j][0]==s[j][2] && s[j][0]==s[j][3] && s[j][0]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[j][0]<<" won"<<endl;
                        break;
                    }
                }
                else
                {

                    if(s[j][2]=='T')
                    {
                        if(s[j][1]==s[j][0] && s[j][0]==s[j][3] && s[j][1]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[j][1]<<" won"<<endl;
                            break;
                        }
                    }
                    else if(s[j][3]=='T')
                    {
                        if(s[j][1]==s[j][2] && s[j][0]==s[j][1] && s[j][0]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[j][0]<<" won"<<endl;
                            break;
                        }
                    }
                    else
                    {
                        if(s[j][1]==s[j][2] && s[j][0]==s[j][1] && s[j][1]==s[j][3] &&s[j][0]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[j][0]<<" won"<<endl;
                            break;
                        }
                    }
                }

            }
        }

        if(flag==2)
        {
            continue;
        }
        for(j=0;j<4;j++)
        {
            if(s[0][j]=='T' || s[1][j]=='T' || (s[0][j]==s[1][j] && s[0][j]!='.'))
            {
                if(s[0][j]=='T')
                {
                    if(s[1][j]==s[2][j] && s[2][j]==s[3][j] && s[1][j]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[1][j]<<" won"<<endl;
                        break;
                    }
                }
                else if(s[1][j]=='T')
                {
                    if(s[0][j]==s[2][j] && s[0][j]==s[3][j] && s[0][j]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[0][j]<<" won"<<endl;
                        break;
                    }
                }
                else
                {

                    if(s[2][j]=='T')
                    {
                        if(s[1][j]==s[0][j] && s[0][j]==s[3][j] && s[1][j]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[1][j]<<" won"<<endl;
                            break;
                        }
                    }
                    else if(s[3][j]=='T')
                    {

                        if(s[1][j]==s[2][j] && s[0][j]==s[1][j] && s[0][j]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[0][j]<<" won"<<endl;
                            break;
                        }
                    }
                    else
                    {
                        if(s[1][j]==s[2][j] && s[0][j]==s[1][j] && s[1][j]==s[3][j] &&s[0][j]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[0][j]<<" won"<<endl;
                            break;
                        }
                    }
                }

            }
        }
        if(flag==2)
        {
            continue;
        }
        if(s[0][0]=='T' || s[1][1]=='T' || (s[0][0]==s[1][1] && s[0][0]!='.'))
        {
            if(s[0][0]=='T')
            {
                if(s[1][1]==s[2][2] && s[2][2]==s[3][3] && s[1][1]!='.')
                {
                    flag=2;
                    fout<<"Case #"<<i+1<<": "<<s[1][1]<<" won"<<endl;

                }
            }
            else if(s[1][1]=='T')
            {
                if(s[0][0]==s[2][2] && s[0][0]==s[3][3] && s[0][0]!='.')
                {
                    flag=2;
                    fout<<"Case #"<<i+1<<": "<<s[0][0]<<" won"<<endl;

                }
            }
            else
            {

                if(s[2][2]=='T')
                {
                    if(s[1][1]==s[0][0] && s[0][0]==s[3][3] && s[1][1]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[1][1]<<" won"<<endl;

                    }
                }
                else if(s[3][3]=='T')
                {

                    if(s[1][1]==s[2][2] && s[0][0]==s[1][1] && s[0][0]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[0][0]<<" won"<<endl;

                    }
                }
                else
                {
                    if(s[1][1]==s[2][2] && s[0][0]==s[1][1] && s[1][1]==s[3][3] &&s[0][0]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[0][0]<<" won"<<endl;

                    }
                }
            }

        }
        if(flag==2)
        {
            continue;
        }

        if(s[0][3]=='T' || s[1][2]=='T' || (s[0][3]==s[1][2] && s[0][3]!='.'))
            {
                if(s[0][3]=='T')
                {
                    if(s[1][2]==s[2][1] && s[2][1]==s[3][0] && s[1][2]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[1][2]<<" won"<<endl;

                    }
                }
                else if(s[1][2]=='T')
                {
                    if(s[0][3]==s[2][1] && s[0][3]==s[3][0] && s[0][3]!='.')
                    {
                        flag=2;
                        fout<<"Case #"<<i+1<<": "<<s[0][3]<<" won"<<endl;

                    }
                }
                else
                {

                    if(s[2][1]=='T')
                    {
                        if(s[1][2]==s[0][3] && s[0][3]==s[3][0] && s[1][2]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[1][2]<<" won"<<endl;

                        }
                    }
                    else if(s[3][0]=='T')
                    {

                        if(s[1][2]==s[2][1] && s[0][3]==s[1][2] && s[0][3]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[0][3]<<" won"<<endl;

                        }
                    }
                    else
                    {
                        if(s[1][2]==s[2][1] && s[0][3]==s[1][2] && s[1][2]==s[3][0] &&s[0][3]!='.')
                        {
                            flag=2;
                            fout<<"Case #"<<i+1<<": "<<s[0][3]<<" won"<<endl;

                        }
                    }
                }

            }
            if(flag==2)
                continue;

            if(flag==1)
                fout<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
            else
                fout<<"Case #"<<i+1<<": "<<"Draw"<<endl;




    }
    fout.close();

}
