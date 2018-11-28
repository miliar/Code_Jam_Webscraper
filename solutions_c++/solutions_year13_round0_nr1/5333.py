#include <iostream>
#include <vector>
using namespace std;

void DoOnce(const char * mat, int ndx, int & nX, int & nO, int & nT)
{
    nX = nO = nT = 0;
    if(ndx < 4)
    {
        int irow = ndx;
        for(int j = 0; j < 4; j++)
        {
            if(mat[irow*4+j] == 'X') nX++;
            else if(mat[irow*4+j] == 'O') nO++;
            else if(mat[irow*4+j] == 'T') nT++;
        }
    }
    else if(ndx < 8)
    {
        int jcol = ndx-4;
        for(int i = 0; i < 4; i++)
        {
            if(mat[i*4+jcol] == 'X') nX++;
            else if(mat[i*4+jcol] == 'O') nO++;
            else if(mat[i*4+jcol] == 'T') nT++;
        }
    }
    else
    {
        vector<int> v;
        if(ndx==8)
        {
            v.push_back(0);
            v.push_back(5);
            v.push_back(10);
            v.push_back(15);
        }
        else
        {
            v.push_back(3);
            v.push_back(6);
            v.push_back(9);
            v.push_back(12);
        }
        for(vector<int>::const_iterator iter = v.begin(); iter != v.end(); iter++)
        {
            if(mat[*iter] == 'X') nX++;
            else if(mat[*iter] == 'O') nO++;
            else if(mat[*iter] == 'T') nT++;
        }
    }
}

int main()
{
    char mat[16];
    int T;
    cin >> T;
    for(int k = 0; k < T; k++)
    {
        int ntot = 0;
        for(int i = 0; i < 16; i++)
        {
            cin >> mat[i];
            if(mat[i] != '.') ntot++;
        }
        int nX, nO, nT;
        bool det = false;
        for(int ndx = 0; ndx < 10; ndx++)
        {
            DoOnce(mat, ndx, nX, nO, nT);
            if(nX==4 || (nX==3&&nT==1))
            {
                det = true;
                cout << "Case #" << k+1 << ": X won" << endl;
                break;
            }
            if(nO==4 || (nO==3&&nT==1))
            {
                det = true;
                cout << "Case #" << k+1 << ": O won" << endl;
                break;
            }
        }
        if(!det)
        {
            if(ntot==16)
                cout << "Case #" << k+1 << ": Draw" << endl;
            else
                cout << "Case #" << k+1 << ": Game has not completed" << endl;
        }
    }
    return 0;
}
