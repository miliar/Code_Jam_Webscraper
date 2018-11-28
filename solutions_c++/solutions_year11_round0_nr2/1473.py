#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

int tabla1[9][9];
int tabla2[9][9];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int casos;
	cin >> casos;
	string letras = "QWERASDF";
	map<char,int> mapa;
	forn(i,28)
        mapa[i+'A'] = 8;
	forn(i,8)
        mapa[letras[i]] = i;
    string st;
	for(int casito = 1; casito <= casos; casito++)
	{
	    forn(i,9)
	    forn(j,9)
	    {
            tabla1[i][j] = -1;
            tabla2[i][j] = -1;
	    }
	    int c, d, n;
	    cin >> c;
	    forn(i,c)
	    {
	        cin >> st;
	        tabla1[mapa[st[0]]][mapa[st[1]]] = st[2]-'A';
	        tabla1[mapa[st[1]]][mapa[st[0]]] = st[2]-'A';
	    }
	    cin >> d;
	    forn(i,d)
	    {
	        cin >> st;
	        tabla2[mapa[st[0]]][mapa[st[1]]] = -2;
	        tabla2[mapa[st[1]]][mapa[st[0]]] = -2;
	    }
	    cin >> n >> st;
	    string res = "";
	    forn(i,n)
	    {
	        res+=st[i];
	        if(res.size()>1&&tabla1[mapa[res[res.size()-1]]][mapa[res[res.size()-2]]]>=0)
	        {
	            res[res.size()-2] = 'A'+tabla1[mapa[res[res.size()-1]]][mapa[res[res.size()-2]]];
	            res.resize(res.size()-1);
	        }
	        forn(j,res.size()-1)
	        {
	            if(tabla2[mapa[res[res.size()-1]]][mapa[res[j]]]==-2)
                    res.clear();
	        }
	    }
	    cout << "Case #"<<casito<<": [";
	    forn(i,res.size()-1)
            cout << res[i] << ", ";
        if(res.size()>0)
            cout << res[res.size()-1];
        cout << "]"<< endl;
	}
}
