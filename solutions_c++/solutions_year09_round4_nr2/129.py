//============================================================================
// Name        : GCJ3.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

char arra[ 50*50 ];
char* arr = arra+100;


template< typename T, int max_size >
class queue {
public:
    T arr[max_size];
    int first, last;
    queue()
	:first(0), last(0) {

    }
    void push( const T& arg ) {
	if( first%max_size == last%max_size && last > first )
	    throw;
	arr[last%max_size] = arg;
	last++;
    }
    T& top() {
	return arr[first%max_size];
    }
    T& pop() {
	if( first == last )
	    throw;
	return arr[(first++)%max_size];
    }
    bool empty() {
	return first == last;
    }
};

char mmap[ 100*100 ];
int pitch=100;
char* map = mmap + 200;
int w=0, h=0, f=0;;

int dmap[100*100];
bool vmap[100*100];
int mind;
struct State {
    char mmap[50];
    char mmap2[50];
    bool visited[50];
    int x, y;
    int d;

    State( int d )
    : d(d) {
    }

    void init() {
	for( int i=0; i<w; i++ ) {
	    mmap[i] = map[i];
	    mmap2[i] = map[i+pitch];
	    visited[i]=false;
	}
	    x=0;
	    y=0;
	    d=0;
    }

    void read( istream& is ) {
    }

    void set( const State& a ) {
	for( int i=0; i<w; i++ )
	    mmap[i] = a.mmap[i];
	for( int i=0; i<w; i++ )
	    mmap2[i] = a.mmap2[i];
	for( int i=0; i<50; i++ )
	    visited[i] = a.visited[i];
	x=a.x;
	y=a.y;
    }

    State* move( int xd ) {
	if( x+xd < 0 || x+xd >=w )
	    return NULL;
	if( visited[x+xd] && mmap2[x+xd] == '#' )
	    return NULL;
	if( mmap[x+xd] == '#' )
	    return NULL;
	if( mmap2[x+xd] == '.' ) {
	    for( int i=1; i<=f; i++ ) {
		if( map[x + xd + (y+i+1)*pitch] == '#' ) {
		    State* ret = new State(d);
		    for( int j=0; j<w; j++ ) {
			ret->mmap2[j] = map[j+(y+i+1)*pitch];
		    }
		    if( i==1 )
			for( int j=0; j<w; j++ ) {
			    ret->mmap[j] = mmap2[j];
			}
		    else
			for( int j=0; j<w; j++ ) {
			    ret->mmap[j] = map[j+(y+i)*pitch];
			}
		    for( int j=0; j<w; j++ ) {
			ret->visited[j] = false;
		    }
		    ret->x = x + xd;
		    ret->y = y + i;
		    //ret->desc += ('0'+i);
		    return ret;
		}
	    }
	    return NULL;

	}
	State* ret = new State(d);
	ret->set( *this );
	ret->x=x+xd;
	ret->visited[x] = true;
	return ret;

    }
    State* dig( int xd ) {
	if( x+xd < 0 || x+xd >=w )
	    return NULL;
	if( mmap[x+xd] == '#' )
	    return NULL;
	if( mmap2[x+xd] == '.' )
	    return NULL;
	State* ret = new State(d+1);
	ret->set( *this );
	for( int i=0; i<w; i++ )
	    ret->visited[i]=false;

	ret->mmap2[x+xd] = '.';

	return ret;
    }
};


int main() {
    for( int i=0; i<100*100; i++ )
	mmap[i] = '#';


    std::ifstream ifs( "in.in" );
    std::ofstream out( "output.txt");
    int casecount;
    ifs >> casecount >> ws;


    for( int casenum=0; casenum<casecount; casenum++ ) {

	for( int i=0; i<100*100; i++ )
	    mmap[i] ='#';
	for( int i=0; i<100*100; i++ )
	    dmap[i] = 1000000;
	for( int i=0; i<100*100; i++ )
	    vmap[i] = false;
	ifs >> h;
	ifs >> w;
	ifs >> f;

	for( int i=0; i<h; i++ ) {
	    for( int j=0; j<w; j++ ) {
		ifs >> ws >> map[ j+i*pitch ];
	    }
	}

	/*for( int i=-1; i<h+1; i++ ) {
	    for( int j=-1; j<w+1; j++ ) {
		cout << map[j+i*pitch];
	    }
	    cout << "\n";
	}*/

	queue<State*,100000> pq;
	State* initial = new State(0);
	initial->init();
	pq.push(initial);

	mind = 1000000;
	while( !pq.empty() ) {
	    State* s = pq.pop();


	    if( s->y == h-1 ) {
		if( mind > s->d ) {
		    mind = s->d;
		}
		/*cout << "!! " << s-> x << " " << s->y << " " << s-> d << "\n";
		cout << s->desc << "\n";
		    cout << " ~~~~~~~ \n";
		}*/
		delete s;
		continue;

	    }
	    if( mind <= s->d )
		continue;
	    State* ns = s->move( -1 );
	    if( ns ) {
		//ns->desc += "l";
		pq.push(ns);
	    }
	    ns = s->move( 1 );
	    if( ns ) {
		//ns->desc += "r";
		pq.push(ns);
	    }
	    ns = s->dig( -1 );
	    if( ns ) {
		//ns->desc += "dl";
		pq.push(ns);
	    }
	    ns = s->dig( 1 );
	    if( ns ) {
		//ns->desc += "dr";
		pq.push(ns);
	    }

	    delete s;
	}

	if( mind == 1000000)
	    cout << "Case #" << (casenum+1) << ": No\n";
	else
	    cout << "Case #" << (casenum+1) << ": Yes " << mind << "\n";

    }

}
