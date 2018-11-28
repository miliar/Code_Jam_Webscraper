#include <iostream>
#include <vector>
using namespace std;

class commd
{
private:
    int color, button;
public:
    commd(int c,int b)
    {
        color = c;
        button = b;
    }
    int col()
    {
        return color;
    }
    int but()
    {
        return button;
    }
};

int solve ( vector <commd> P)
{
    int bluetime = 0;
    int bluebut = 1;
    int ortime = 0;
    int orbut = 1;
    for (int i=0; i<P.size();i++)
    {
        if (P[i].col()==1) 
        {
            ortime = ortime+abs(orbut-P[i].but())+1;
            ortime = (ortime <=bluetime?bluetime+1:ortime);
            orbut = P[i].but();
        } else
        {
            bluetime = bluetime+abs(bluebut-P[i].but())+1;
            bluetime = (bluetime <=ortime?ortime+1:bluetime);
            bluebut = P[i].but();
        } 
    }
    return (bluetime>ortime?bluetime:ortime);
}

void printline(int i,int T)
{
    cout << "Case #" << i+1 << ": " << T << endl;
}

int main()
{
    int T,N;
    int b,ti;
    char c;
    cin >> T;
    vector <commd> P;
    for (int i=0; i< T;i++)
    {
        cin >> N;
        P.clear();
        for (int j=0; j<N; j++)
        {
            cin >> c >> b;
            commd a(c=='B'?2:1,b);
            P.push_back(a);
        }
        ti = solve( P);    
        printline(i,ti);
    }
    return 0;
}
