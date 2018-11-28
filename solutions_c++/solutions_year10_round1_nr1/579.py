#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = ((int)n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

vector<string> vec;
int n,k;

void rotate()
{

    vector<string> vec2(n);
    forn(i,n)
        vec2[i].resize(n);
    forn(i,n)
    forn(j,n)
    {
        vec2[i][j] = vec[n-1-j][i];
    }
    vec = vec2;
}

void gravedad()
{
    forn(j,n)
    {
        int pos = n-1;
        for(int i=n-1;i>=0;i--)
        {
            if(vec[i][j] != '.')
            {
                swap(vec[i][j],vec[pos][j]);
                pos--;
            }
        }
    }
}

bool calc(char c)
{
    for(int i=0;i<n-k+1;i++)
    forn(j,n)
    {
        bool b = true;
        forn(t,k)
        {
            if(vec[i+t][j]!=c)
            {
                b = false;
                break;
            }
        }
        if(b==true)
            return true;
    }
    for(int i=0;i<n-k+1;i++)
    forn(j,n)
    {
        bool b = true;
        forn(t,k)
        {
            if(vec[j][i+t]!=c)
            {
                b = false;
                break;
            }
        }
        if(b==true)
            return true;
    }
    for(int i=0;i<n-k+1;i++)
    for(int j=0;j<n-k+1;j++)
    {
        bool b = true;
        forn(t,k)
        {
            if(vec[i+t][j+t]!=c)
            {
                b = false;
                break;
            }
        }
        if(b==true)
            return true;
    }
    for(int i=k-1;i<n;i++)
    for(int j=0;j<n-k+1;j++)
    {
        bool b = true;
        forn(t,k)
        {
            if(vec[i-t][j+t]!=c)
            {
                b = false;
                break;
            }
        }
        if(b==true)
            return true;
    }
    return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        cin >>n >> k;
        vec.resize(n);
        forn(i,n)
            cin >> vec[i];
        rotate();
        gravedad();
        cout << "Case #" << casito+1 << ": ";
        bool blue = calc('B');
        bool red = calc('R');
        if(blue&&red)
            cout << "Both" << endl;
        if(blue&&!red)
            cout << "Blue" << endl;
        if(!blue&&red)
            cout << "Red" << endl;
        if(!blue&&!red)
            cout << "Neither" << endl;
    }
}
