#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("AL.in");
ofstream fout("Aout.txt");
char buff[4][5];
int N;

int main()
{
    fin >> N;
    for(int i=0;i<N;i++)
    {
            for(int j=0;j<4;j++)
                    fin >> buff[j];
            bool end = false;
            char Won = 0;
            char P=0;
            for(int j=0;j<4;j++)
            {
                    P=0;
                    bool fail = false;
                    for(int k=0;k<4;k++)
                    {
                            if(buff[j][k]=='.'){fail = true;break;}
                            else if(buff[j][k]=='T')continue;
                            else if(P==0)P=buff[j][k];
                            else if(buff[j][k]!=P){fail = true;break;}
                    }
                    if(fail==false){end=true;Won=P;}
            }
            for(int j=0;j<4;j++)
            {
                    P=0;
                    bool fail = false;
                    for(int k=0;k<4;k++)
                    {
                            if(buff[k][j]=='.'){fail = true;break;}
                            else if(buff[k][j]=='T')continue;
                            else if(P==0)P=buff[k][j];
                            else if(buff[k][j]!=P){fail = true;break;} 
                    }
                    if(fail==false){end=true;Won=P;}
            }
            P=0;
            bool fail = false;
            for(int j=0;j<4;j++)
            {
                    if(buff[j][j]=='.'){fail = true;break;}
                    else if(buff[j][j]=='T')continue;
                    else if(P==0)P=buff[j][j];
                    else if(buff[j][j]!=P){fail = true;break;}
            }
            if(fail==false){end=true;Won=P;}
            P=0;
            fail = false;
            for(int j=0;j<4;j++)
            {
                    if(buff[j][3-j]=='.'){fail = true;break;}
                    else if(buff[j][3-j]=='T')continue;
                    else if(P==0)P=buff[j][3-j];
                    else if(buff[j][3-j]!=P){fail = true;break;}
            }
            if(fail==false){end=true;Won=P;}
            bool notcomplete = false;
            for(int j=0;j<4;j++)
            {
                    for(int k=0;k<4;k++)
                            if(buff[j][k]=='.')notcomplete = true;
                            }
            fout <<"Case #" << i+1 << ": ";
            if(end)fout <<  Won << " won"<<endl;
            else if(notcomplete) fout << "Game has not completed" <<endl;
            else fout <<  "Draw"<<endl;
    }
    system("pause");
}
