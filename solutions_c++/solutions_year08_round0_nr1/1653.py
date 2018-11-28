#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip> 
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define INF 0xFFFF
 
using namespace std;

int main()
{
//    freopen("A-small.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("salida.out","w",stdout);
    int casos;
    cin>>casos;    
    FOR (cases,casos)
    {
        int m,n;
        cin>>m;
        vector<string> cadenas(m);
        string cadena;
        getline(cin,cadena);
        FOR (i,m)
            getline(cin,cadenas[i]);
        cin>>n;
        vector<string> quer(n);
        getline(cin,cadena);
        FOR (i,n)
            getline(cin,quer[i]);
        int resp=INF;     
        if (n==0)
           resp=0;
        else{
        vector< vector<int> > matrix(n,vector<int>(m,INF));
        

        FOR (j,m)
            if (quer[0]!=cadenas[j])
               matrix[0][j]=0;

        FORI (i,1,n)
            FOR (j,m)
            {
                if (quer[i]==cadenas[j])
                   continue;
                FOR (k,m)
                    matrix[i][j]=min(matrix[i][j],matrix[i-1][k]+!(k==j));
            }
        FOR (i,m)
            resp=min(resp,matrix[n-1][i]);}
        cout<<"Case #"<<cases+1<<": "<<resp<<endl;
    }
    return 0;
}
