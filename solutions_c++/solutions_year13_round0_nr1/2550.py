#include <iostream>

using namespace std;

char plansza[4][4];

int main()
{
    int n, xT=0, yT=-1;
    bool czyRemis = true;
    bool czyWygrano = false;

    cin>>n;

    for(int k=1; k<=n; ++k)
    {
        czyWygrano = false;
        czyRemis = true;
        xT=0;
        yT=-1;

        for(int i=0; i<4; ++i)
        {
            for(int j=0; j<4; ++j)
            {
                cin>>plansza[j][i];
                if(plansza[j][i]=='.') czyRemis=false;
                if(plansza[j][i]=='T') {xT=j; yT=i;}
            }
        }

        //if(czyRemis) cout<<"Case #"<<k<<": Draw\n"

//cout<<"AAAACHUJ   "<<plansza[xT][yT];
//cout<<czyRemis;


        for(int i=0; i<4; ++i)
        {
            if((plansza[i][0]!='.') && (plansza[i][0]==plansza[i][1]) && (plansza[i][0]==plansza[i][2]) && (plansza[i][0]==plansza[i][3])) {cout<<"Case #"<<k<<": "<<plansza[i][0]<<" won\n"; czyWygrano=true; break;}
            if((plansza[0][i]!='.') && (plansza[0][i]==plansza[1][i]) && (plansza[0][i]==plansza[2][i]) && (plansza[0][i]==plansza[3][i])) {cout<<"Case #"<<k<<": "<<plansza[0][i]<<" won\n"; czyWygrano=true; break;}
        }
        if(czyWygrano) continue;
        if((plansza[0][0]!='.') && (plansza[0][0]==plansza[1][1]) && (plansza[0][0]==plansza[2][2]) && (plansza[0][0]==plansza[3][3])) {cout<<"Case #"<<k<<": "<<plansza[0][0]<<" won\n"; continue;}
        if((plansza[3][0]!='.') && (plansza[3][0]==plansza[2][1]) && (plansza[3][0]==plansza[1][2]) && (plansza[3][0]==plansza[0][3])) {cout<<"Case #"<<k<<": "<<plansza[3][0]<<" won\n"; continue;}

        //czy wygraly Xy?
        plansza[xT][yT]='X';
        if((plansza[xT][0]!='.') && (plansza[xT][0]==plansza[xT][1]) && (plansza[xT][0]==plansza[xT][2]) && (plansza[xT][0]==plansza[xT][3])) {cout<<"Case #"<<k<<": X won\n"; continue;}
        if((plansza[0][yT]!='.') && (plansza[0][yT]==plansza[1][yT]) && (plansza[0][yT]==plansza[2][yT]) && (plansza[0][yT]==plansza[3][yT])) {cout<<"Case #"<<k<<": X won\n"; continue;}

            if(xT==yT)
            {

                if((plansza[0][0]!='.') && (plansza[0][0]==plansza[1][1]) && (plansza[0][0]==plansza[2][2]) && (plansza[0][0]==plansza[3][3])) {cout<<"Case #"<<k<<": X won\n"; continue;}
            }

            if(xT+yT==3)
            {
                if((plansza[3][0]!='.') && (plansza[3][0]==plansza[2][1]) && (plansza[3][0]==plansza[1][2]) && (plansza[3][0]==plansza[0][3])) {cout<<"Case #"<<k<<": X won\n"; continue;}
            }

        //czy wygraly Oa?
        plansza[xT][yT]='O';
        if((plansza[xT][0]!='.') && (plansza[xT][0]==plansza[xT][1]) && (plansza[xT][0]==plansza[xT][2]) && (plansza[xT][0]==plansza[xT][3])) {cout<<"Case #"<<k<<": O won\n"; continue;}
        if((plansza[0][yT]!='.') && (plansza[0][yT]==plansza[1][yT]) && (plansza[0][yT]==plansza[2][yT]) && (plansza[0][yT]==plansza[3][yT])) {cout<<"Case #"<<k<<": O won\n"; continue;}

            if(xT==yT)
            {

                if((plansza[0][0]!='.') && (plansza[0][0]==plansza[1][1]) && (plansza[0][0]==plansza[2][2]) && (plansza[0][0]==plansza[3][3])) {cout<<"Case #"<<k<<": O won\n"; continue;}
            }

            if(xT+yT==3)
            {
                if((plansza[3][0]!='.') &&
                   (plansza[3][0]==plansza[2][1]) &&
                   (plansza[3][0]==plansza[1][2]) &&
                   (plansza[3][0]==plansza[0][3]))
                   {cout<<"Case #"<<k<<": O won\n"; continue;}
            }

        //remis?
        if(czyRemis) {cout<<"Case #"<<k<<": Draw\n"; continue;}
        else {cout<<"Case #"<<k<<": Game has not completed\n"; continue;}

    }
    return 0;
}
