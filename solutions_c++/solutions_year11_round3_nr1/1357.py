#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<map>

using namespace std;

bool out(int r, int c, int i, int j)
{
    if (i<0 || i >=r) return true;
    if (j<0 || j >=c) return true;
    return false;
}

int main()
{
    int t, count;
    cin >> t;
    count=0;
    int r, c;
    int sum;
    bool T;
    vector<vector<char> > map; 
    while (count<t)
    {
        count++;
        sum=0;
        cin >> r >> c;
        map.clear();
        vector<char> temp;
        temp.assign(c, ' ');
        map.assign(r, temp);
        T=true;
        for (int i=0; i<r; i++)
            for (int j=0; j<c; j++)
                cin >> map[i][j];

        for (int i=0; i<r; i++)
            for (int j=0; j<c; j++)
            {
                if (map[i][j]=='#')
                {
                    map[i][j]='/'; sum++;       
                    if (!out(r,c,i,j+1)&&map[i][j+1]=='#') { map[i][j+1]='\\'; sum++;}
                    else T=false;
                    if (!out(r,c,i+1,j)&&map[i+1][j]=='#') { map[i+1][j]='\\'; sum++;}
                    else T=false;
                    if (!out(r,c,i+1,j+1)&&map[i+1][j+1]=='#') { map[i+1][j+1]='/'; sum++;}                
                    else T=false;
                }
            }
            
        cout << "Case #" << count << ":" <<endl;
        if (sum%4!=0 || !T)
            cout << "Impossible" << endl;
        else
        {
            for (int i=0; i<r; i++)
            {
                for (int j=0; j<c; j++)
                    cout << map[i][j];
                cout << endl;
            }
        }

    }
    
}
