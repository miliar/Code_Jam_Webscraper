#include <iostream>
#include <fstream>
using namespace std;

char board[4][4];

#define p(a,x,y) if (board[x][y]!='T') { if (a==0) a=board[x][y]; else {if (a!=board[x][y]) a=-1;}}

string izr()
{
    bool gotovo=true;
    for (int i=0;i<4;i++)
    {
        char prvi=0,drugi=0,treci=0,cetvrti=0;
        for (int j=0;j<4;j++)
        {
            if (board[j][i]=='.') gotovo=false;
            p(prvi,i,j);
            p(drugi,j,i);
            p(treci,j,j);
            p(cetvrti,3-j,j);
        }
        if (prvi>'.') return prvi+string(" won");
        if (drugi>'.') return drugi+string(" won");
        if (treci>'.') return treci+string(" won");
        if (cetvrti>'.') return cetvrti+string(" won");
    }
    if (gotovo) return "Draw"; else return "Game has not completed";
}

int main()
{
    ofstream out("izlaz.txt");
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<4;j++)
            cin >> board[j];
        out << "Case #" << i+1 << ": " << izr() << endl;
    }
    out.close();
    return 0;
}
