#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char board[4][4];

string eval()
{
    bool f = true;
    bool xD1 = true;
    bool xD2 = true;
    bool oD1 = true;
    bool oD2 = true;
    for(int a=0;a<4;a++)
    {
        bool xR = true;
        bool xC = true;
        bool oR = true;
        bool oC = true;
        for(int b=0;b<4;b++)
        {
            char cR = board[a][b];
            xR = xR && (cR == 'X' || cR == 'T');
            oR = oR && (cR == 'O' || cR == 'T');
            char cC = board[b][a];
            xC = xC && (cC == 'X' || cC == 'T');
            oC = oC && (cC == 'O' || cC == 'T');
            if(cR == '.') f = false;
        }
        if(xR || xC) return "X won";
        if(oR || oC) return "O won";
        char cD1 = board[a][a];
        xD1 = xD1 && (cD1 == 'X' || cD1 == 'T');
        oD1 = oD1 && (cD1 == 'O' || cD1 == 'T');
        char cD2 = board[a][3-a];
        xD2 = xD2 && (cD2 == 'X' || cD2 == 'T');
        oD2 = oD2 && (cD2 == 'O' || cD2 == 'T');
    }
    if(xD1 || xD2) return "X won";
    if(oD1 || oD2) return "O won";
    return f ? "Draw" : "Game has not completed";
}

int main(int argc, char* argv[])
{
    ifstream in("A-large.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
        for(int j=0;j<4;j++) in>>board[j];
        out<<"Case #"<<i+1<<": "<<eval()<<endl;
    }
    in.close();
    out.close();
	return 0;
}
