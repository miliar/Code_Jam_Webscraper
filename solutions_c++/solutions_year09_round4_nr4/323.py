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
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

double posx[3];
double posy[3];
double radio[3];

double dist(int i, int j)
{
    return sqrt((posx[i]-posx[j])*(posx[i]-posx[j])+(posy[i]-posy[j])*(posy[i]-posy[j]));
}

int main()
{
    ifstream fin("D-small.in");
    ofstream fout("D-small.out");
	int casos;
	fin >> casos;
	forn(casito,casos)
	{
	    double res;
	    int n;
	    fin >> n;
	    forn(i,n)
	    {
	        fin >> posx[i] >> posy[i] >> radio[i];
	    }
	    if(n==1)
	        res = radio[0];
	    if(n==2)
            res = max(radio[0],radio[1]);
        if(n==3)
        {
            res = max(radio[0],dist(1,2)+radio[1]+radio[2]);
            res <?= max(radio[1],dist(0,2)+radio[0]+radio[2]);
            res <?= max(radio[2],dist(1,0)+radio[1]+radio[0]);
            res /= 2;
        }
        fout << "Case #" << casito+1 << ": " << res << endl;
	}
}
