#include<iostream>
using namespace std;
#define F(i,m,n) for(int i = m; i<=n; i++)

int grid[4][4];
int tx,ty;
bool hasDot = false;

void inputGrid()
{
    tx=-1;
    ty=-1;
    hasDot = false;

    F(a,0,3)
        {
            F(b,0,3)
            {
                char c;
                cin>>c;
                grid[a][b] = c;
                if (c == 'T')
                {
                    tx=a;
                    ty=b;
                    grid[a][b] = 'O';
                }
                if(c == '.')
                {
                    hasDot = true;
                }
            }

        }
}

void outputGrid()
{
    F(a,0,3)
        {
            F(b,0,3)
            {
                cout<<(char)grid[a][b];
            }
            cout<<'\n';
        }
}

bool checkResult(int res)
{
     if (res == 4*'O') {
                cout<<"O won";
                return true;
            }
            else if (res == 4*'X')
            {
                cout<<"X won";
                return true;
            }
    return false;
}

bool checkRow(int i)
{
    int res = 0;
    F(k,0,3)
    {
        res += grid[i][k];
    }

    return checkResult(res);
}

bool checkCol(int i)
{
    int res = 0;
    F(k,0,3)
    {
        res += grid[k][i];
    }

    return checkResult(res);
}

bool checkDiag1()
{
    int res = 0;
    F(i,0,3)
    {
        res += grid[i][i];
    }
    return checkResult(res);
}

bool checkDiag2()
{
     int res = 0;
    F(i,0,3)
    {
        res += grid[3-i][i];
    }
    return checkResult(res);
}

void checkGrid()
{
     F(p,0,3)
        {
           if(checkRow(p) || checkCol(p)) return;
        }
    if(checkDiag1() || checkDiag2()) return;


    if(tx >= 0)
    {
        grid[tx][ty] = 'X';

        if(checkRow(tx) || checkCol (ty)) return;

        if(tx == ty || tx == 3-ty)
        {
            if(checkDiag1() || checkDiag2()) return;
        }
    }

    if(hasDot) cout<<"Game has not completed";

    else cout<<"Draw";
}




int main()
{

    int t;
    cin>>t;



    F(i,1,t)
    {

        inputGrid();

        cout<<"Case #"<<i<<": ";

        checkGrid();

        cout<<endl;
        //outputGrid();
    }

    return 0;
}
