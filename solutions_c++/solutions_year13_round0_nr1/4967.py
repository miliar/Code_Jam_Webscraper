#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void megold(istream& in, ostream& out)
{
    string game[4];
    string temp;
    for(int i=0; i<4; i++)
    {
        getline(in, game[i]);
    }
    getline(in, temp);

    //sorok
    for(int i=0; i<4; i++)
    {
        bool nyert=true;
        for(int j=0; j<4; j++) nyert=nyert && (game[i][j]=='X' || game[i][j]=='T');
        if(nyert) { out<<"X won"; return; }

        nyert=true;
        for(int j=0; j<4; j++) nyert=nyert && (game[i][j]=='O' || game[i][j]=='T');
        if(nyert) { out<<"O won"; return; }
    }

    //oszlopok
    for(int i=0; i<4; i++)
    {
        bool nyert=true;
        for(int j=0; j<4; j++) nyert=nyert && (game[j][i]=='X' || game[j][i]=='T');
        if(nyert) { out<<"X won"; return; }

        nyert=true;
        for(int j=0; j<4; j++) nyert=nyert && (game[j][i]=='O' || game[j][i]=='T');
        if(nyert) { out<<"O won"; return; }
    }

    //fõátló
    bool nyert=true;
    for(int i=0; i<4; i++)
    {
        nyert=nyert && (game[i][i]=='X' || game[i][i]=='T');
    }
    if(nyert) { out<<"X won"; return; }

    nyert=true;
    for(int i=0; i<4; i++)
    {
        nyert=nyert && (game[i][i]=='O' || game[i][i]=='T');
    }
    if(nyert) { out<<"O won"; return; }

    //mellékátló
    nyert=true;
    for(int i=0; i<4; i++)
    {
        nyert=nyert && (game[i][3-i]=='X' || game[i][3-i]=='T');
    }
    if(nyert) { out<<"X won"; return; }

     nyert=true;
    for(int i=0; i<4; i++)
    {
        nyert=nyert && (game[i][3-i]=='O' || game[i][3-i]=='T');
    }
    if(nyert) { out<<"O won"; return; }

    bool dontetlen=true;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            dontetlen=dontetlen && (game[i][j]!='.');
        }
    }

    if(dontetlen) out<<"Draw";
    else out<<"Game has not completed";
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("tictactoe.out");
    int n;
    in>>n;
    string temp;
    getline(in, temp);
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();

    return 0;
}
