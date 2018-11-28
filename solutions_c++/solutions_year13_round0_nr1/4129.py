#include <iostream>
#include <fstream>

using namespace std;

struct playerScore
{
    char name;
    int score;
};

int main()
{
    //playerScore score[10];
    ifstream cin("ttt.txt");
    ofstream cout("tto.txt");
    int score[10];
    int t;
    char c;
    bool dot=false;
    cin>>t;
 for (int test=1; test<=t; test++)
    {
        for(int i=0; i<10; i++)
            score[i]=0;
        dot=false;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>c;
                if(c!='.')
                {

                    score[i]+=c;
                    score[j+4]+=c;
                    if(i==j)
                        score[8]+=c;
                    if(i+j==3)
                        score[9]+=c;

                }
                else dot=true;
            }
        }

        for (int i=0; i<10; i++)
        {
            //cout<<score[i]<<" ";
            if((score[i]==4*(int)'O')||(score[i]==3*(int)'O'+(int)'T'))
            {
                cout<<"Case #"<<test<<": O won"<<'\n';
                goto READ;
            }
            if((score[i]==4*(int)'X')||(score[i]==3*(int)'X'+(int)'T'))
            {
                cout<<"Case #"<<test<<": X won"<<'\n';
                goto READ;
            }
        }
        if(dot)
            cout<<"Case #"<<test<<": Game has not completed"<<'\n';
        else
            cout<<"Case #"<<test<<": Draw"<<'\n';
READ:
        continue;
    }
    return 0;
}
