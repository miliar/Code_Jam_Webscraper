#include <iostream>
#include <vector>
using namespace std;

    char Comb[256][256];
    bool Opp[256][256];
    vector<char> list;
void null()
{
    for (int i=0; i<256; ++i )
    {
        for (int j=0; j<256; ++j )
        {
             Comb[i][j]=' ';
             Opp[i][j]=false;
        }
    }
}
bool isOpp(char c1)
{
        for (int j=0; j<list.size(); ++j)
        {
            if (Opp[c1][list[j]]) {return true;};
        }
        return false;
}

int main()
{


    char c,c1,c2,c3;
    int ri,n,m;

    cin >> n;
    for (int i=0; i<n; ++i)
    {
        null();
        list.clear();
        cin >> m;
        for (int j=0; j<m; ++j)
        {
            cin >> c1 >> c2 >> c3;
            Comb[c1][c2]=c3;
            Comb[c2][c1]=c3;
        }
         cin >> m;
            for (int j=0; j<m; ++j)
        {
            cin >> c1 >> c2;
            Opp[c1][c2]=true;
            Opp[c2][c1]=true;
        }
        cin >> m;
        for (int j=0; j<m; ++j)
        {
            cin >> c;
            if  (!list.empty())
            {
                char ic=list.back();

                if (Comb[c][ic]==' ')
                {
                    if (isOpp(c))
                    {
                        list.clear();
                    }
                    else
                    {
                    list.push_back(c);

                    }
                }
                else
                {
                    list.pop_back();
                    list.push_back(Comb[c][ic]);

                }
            }
            else
            {
                list.push_back(c);

            }
        }
    cout << "Case #" << i+1 << ": [";

    for (int j=0; j<list.size(); ++j)
        {
            cout << list[j];
            if (j!=list.size()-1) {cout << ", "; }
        }
        cout << "]";
        cout <<endl;
    }


    return 0;
}
