#include<fstream>
using namespace std;
ifstream in("tic.in");
ofstream out("tic.out");
char a[10][10];
int n;
void readAndSolve(int caz)
{
    int status=0;
    //0 nu s-a terminat
    //1 castiga x
    //2 castiga y
    //3 egal
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
            in>>a[i][j];
    }
    //verif linie;
    for(int i=1;i<=4;i++)
    {
        bool exVictorieLinie=true;
        bool exVictoriColoana=true;
        for(int j=2;j<=4;j++)
        {
            if(a[i][j]!=a[i][j-1] && a[i][j]!='T')
                exVictorieLinie=false;
            if(a[j][i]!=a[j-1][i] && a[i][j]!='T')
                exVictoriColoana=false;
        }
        if(exVictorieLinie==true)
        {
            int j=1;
            while(a[i][j]=='T')
                j++;
            if(a[i][j]=='X')
            {
                if(status==2)
                    status=3;
                else
                    status=1;
            }
            if(a[i][j]=='O')
            {
                if(status==1)
                    status=3;
                else
                    status=2;
            }
        }
        if(exVictoriColoana==true)
        {
            int j=1;
            while(a[j][i]=='T')
                j++;
            if(a[j][i]=='X')
            {
                if(status==2)
                    status=3;
                else
                    status=1;
            }
            if(a[j][i]=='O')
            {
                if(status==1)
                    status=3;
                else
                    status=2;
            }
        }
    }
    bool exPr=true;
    bool exSc=true;
    for(int i=2;i<=4;i++)
    {
        if(a[i][i]!=a[i-1][i-1] &&a[i][i]!='T')
            exPr=false;
        if(a[i][4-i+1]!=a[i-1][4-i+2] && a[i][4-i+1]!='T')
            exSc=false;
    }
    if(exPr==true)
    {
        int j=1;
        while(a[j][j]=='T')
            j++;
        if(a[j][j]=='X')
        {
            if(status==2)
                status=3;
            else
                status=1;
        }
        if(a[j][j]=='O')
        {
            if(status==1)
                status=3;
            else
                status=2;
        }
    }
    if(exSc==true)
    {
        int j=1;
        while(a[j][4-j+1]=='T')
            j++;
        if(a[j][4-j+1]=='X')
        {
            if(status==2)
                status=3;
            else
                status=1;
        }
        if(a[j][4-j+1]=='O')
        {
            if(status==1)
                status=3;
            else
                status=2;
        }
    }
    out<<"Case #"<<caz<<": ";
    if(status==0)
    {
        bool exPunct=false;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(a[i][j]=='.')
                    exPunct=true;
        if(exPunct==false)
                out<<"Draw"<<"\n";
        else
        out<<"Game has not completed"<<"\n";
    }
    if(status==1)
    {
        out<<"X won"<<"\n";
    }
    if(status==2)
    {
        out<<"O won"<<"\n";
    }
    if(status==3)
    {
        out<<"Game has not completed"<<"\n";

    }
    //diagonale
}
int main()
{
    in>>n>>ws;
    for(int i=1;i<=n;i++)
    {
        readAndSolve(i);
        in>>ws;
    }
}
