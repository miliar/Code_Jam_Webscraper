#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <algorithm>
#include <map>
#include <iomanip>
using namespace std;

int n,m;
const int prime = 59509;

vector< string >  getpath(){
    string tmp;
    getline(cin,tmp);

    vector< string > ret;

    string w = "";
    for( int i = 0; i < tmp.size(); ++i ){
        if( tmp[i] == '/' ){
            if( w.length() > 0 ) ret.push_back(w);
            w = "";
        }else w = w + tmp[i];
    }
    if( w.length() > 0 ) ret.push_back(w);

    return ret;
}

struct trie{
    vector< string > names;
    vector< trie* > poks;

    int has( string q ){
        for( int i = 0; i < names.size(); ++i )
            if( names[i] == q ) return i;
            return -1;
    }

    void kill(){
        for( int i = 0; i < poks.size(); ++i ) poks[i]->kill();
        names.clear();
        poks.clear();
    }

};

trie dad;

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);

    int tests;
    scanf("%d",&tests);

    int t = 1;

    for( ; tests; --tests ){
        scanf("%d%d\n",&n,&m);

        dad.kill();

        for( int i = 0; i < n; ++i ){
            vector< string > h = getpath();

            trie *p = &dad;
            for( int i = 0; i < h.size(); ++i ){
                int v = p->has( h[i] );

                if( v == -1 ){
                    v = p->names.size();
                    p->names.push_back( h[i] );
                    p->poks.push_back( new trie );
                }

                p = p->poks[v];
            }
        }
        int sol = 0;

        for( int i = 0; i < m; ++i ){
            vector< string > h = getpath();
            trie *p = &dad;

            for( int i = 0; i < h.size(); ++i ){
                int v = p->has( h[i] );

                if( v == -1 ){
                    sol ++;
                    v = p->names.size();
                    p->names.push_back( h[i] );
                    p->poks.push_back( new trie );
                }

                p = p->poks[v];
            }
        }
        printf("Case #%d: %d\n",t,sol);
        t++;



    }

    return 0;
}
