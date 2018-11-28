#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctype.h>  // isdigit(), isalnum(), isalpha()
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
using namespace std;

#define MAX_LINE 10000

bool dbg = false;

#define DBG if( dbg )
#define LOOP(var,f,t) for( var=f; var<t; var++ )
#define loop(var,n)   LOOP(var,0,n)
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

// "3 4 5" ->  { 3, 4, 5 }
// returns the array size
// size should be big enough
template <class T>
int line2arr( char* line, T* arr, int max_size )
{
    int n = 0;
    if ( line != NULL ) {
        istringstream s(line);
        T v;
        while ( s >> v ) {
            arr[n++] = v;
        }
    }
    return n;
}

void chomp( char *line ) {
    if ( line != 0 )
        while ( strlen(line) > 0 && line[strlen(line)-1] == '\n' )
            line[strlen(line)-1] = 0;
}

class node
{
    public:
    node* parent;
    string name;
    vector<node*> children;
    int index;
    void print( int indent = 0 );
};

void node::print( int indent )
{
    int i;
    if( !dbg ) return;

    REP( i, indent ) { cout << " "; }
    cout << "'" << name << "'" << endl;
    vector<node*>::iterator it;
    for( it = children.begin(); it != children.end(); it++ )
        (*it)->print( indent + 1 );
}

vector<node> dir;

void doAll( int caseno )
{
    int i, j, k;
    /*
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin); chomp(line);
    */

    node* root = new node;
    root->parent = 0;
    root->name = "";

    int existe, noexiste;
    scanf("%d%d", &existe, &noexiste);
    DBG cout << "Existe " << existe << " No existe " << noexiste << "\n";

    string line;
    getline( cin, line );
    REP(i,existe) {
        getline(cin,line);
        DBG cout << "Existe '" << line << "'  length: " << line.length() << "\n";
        string path;
        REP(j,line.length()) {
            if( line[j] == '/' )
                path += " ";
            else
                path += line[j];
        }
        // DBG cout << "path " << path << "\n";
        istringstream d(path);
        string dir;
        node* p = root;
        while( d >> dir ) {
            // DBG cout << "dir = " << dir << "\n";
            vector<node*>::iterator it;
            bool found = false;
            for( it = p->children.begin(); it != p->children.end(); it++ )
            {
                if( (*it)->name == dir )
                {
                    found = true;
                    p = (*it);
                    break;
                }
            }
            if( !found )
            {
                // DBG cout << "not found adding dir: " << dir << "\n";
                node* n = new node;
                n->name = dir;
                n->parent = p;
                p->children.push_back(n);
                p= n;
            }
        }
    }

    DBG cout << "------------------\n";
    DBG cout << "starting dirs: \n";
    root->print();
    DBG cout << "------------------\n";

    int cuenta = 0;
    REP(i,noexiste) {
        getline(cin,line);
        DBG cout << "== Trying '" << line << "'\n";

        string path;
        REP(j,line.length()) {
            if( line[j] == '/' )
                path += " ";
            else
                path += line[j];
        }
        DBG cout << "path " << path << "\n";
        istringstream d(path);
        string dir;
        node* p = root;
                p->print();

        while( d >> dir ) {
            DBG cout << " dir = " << dir << " -> " ;
            vector<node*>::iterator it;
            bool found = false;
            for( it = p->children.begin(); it != p->children.end(); it++ )
            {
                if( (*it)->name == dir )
                {
                    found = true;
                    p = (*it);
                    DBG cout << " existe\n";
                    break;
                }
            }
            if( !found )
            {
                cuenta++;
                DBG cout << " not found adding dir: " << p->name << "/" << dir << "  cuenta: " << cuenta << "\n";
                node* n = new node;
                n->name = dir;
                n->parent = p;
                // DBG cout << "Adding to parent dir: " << p->name << "  cuenta: " << cuenta << "\n";
                p->children.push_back(n);
                p = n;
            }
        }
    }

    /*
    int arr[10];
    int n = line2arr( line, arr, 10 );
    DBG cout <<( "Array has " << n "elements\n";
    */

    // Answer for this case
    cout << "Case #" << caseno << ": ";
    cout << cuenta;
    cout << "\n";
}

int main( int argc, char* argv[] ) {
    // freopen("sample.txt","r",stdin);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    // freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if ( argc != 1 ) dbg = true;

    int ncases,i;
    string line;

    scanf("%d",&ncases);
    getline( cin, line );
    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) doAll(i+1);

    return 0;
}

