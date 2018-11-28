#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int i = 0; i<t; ++i)
    {
        bool oWin = false;
        bool xWin = false;
        bool noWin = true;
        vector<int> xV(4,0);
        vector<int> xH(4,0);
        vector<int> oV(4,0);
        vector<int> oH(4,0);
        int cont = 0;
        int xDiagL = 0;
        int xDiagR = 0;
        int oDiagL = 0;
        int oDiagR = 0;
        for(int j = 0; j<4; ++j)
        {
            for(int k = 0; k<4; ++k)
            {
                char l;
                cin>>l;
                if(l == 'X' || l == 'T')
                {
                    xV[j]++;
                    xH[k]++;
                    if(xV[j] == 4 || xH[k] == 4) {
                        xWin = true;
                        noWin = false;
                    }
                    if(k == j)
                    {
                        xDiagL++;
                    }
                    if(3-k == j)
                    {
                        xDiagR++;
                    }
                    cont++;
                }
                if(l == 'O' || l == 'T')
                {
                    oV[j]++;
                    oH[k]++;
                    if(oV[j] == 4 || oH[k] == 4) {
                        oWin = true;
                        noWin = false;
                    }
                    if(k == j)
                    {
                        oDiagL++;
                    }
                    if(3-k == j)
                    {
                        oDiagR++;
                    }
                    if(l != 'T')
                        cont++;
                }
            }
        }

        if(xDiagL == 4 || xDiagR == 4)
        {
            xWin = true;
            noWin = false;
        }
        if(oDiagL == 4 || oDiagR == 4)
        {
            oWin = true;
            noWin = false;
        }

        if(cont != 16 && noWin)
        {
            cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
        }
        if(noWin && cont == 16)
        {
            cout<<"Case #"<<i+1<<": Draw"<<endl;
        }
        else
        {
            if(oWin)
            {
                cout<<"Case #"<<i+1<<": O won"<<endl;
            }
            if(xWin)
            {
                cout<<"Case #"<<i+1<<": X won"<<endl;
            }
        }
    }
    return 0;
}
