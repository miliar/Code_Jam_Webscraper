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
#include <map>
#include <iomanip>
#include <sstream>
using namespace std;

struct Node {
    bool children;
    std::string attr;
    double p;
    Node* a;
    Node* b;

};

Node* ReadNode( std::ifstream& ifs) {
    Node* ret = new Node;
    ifs >> ws;
    assert( ifs.peek() == '(' );
    ifs.get();

    ifs >> ret->p;
    ifs >> ws;

    if( ifs.peek() == ')' ) {
	ret->children=false;
    }
    else {
	ret->children = true;
	ifs >> ret->attr;
	ret->a = ReadNode( ifs );
	ret->b = ReadNode( ifs );
    }

    ifs >> ws;
    assert( ifs.get() == ')' );
    return ret;
}

void PrintNode( Node* n ) {
    cout << "( " << n->p << " ";
    if( n->children ) {
	cout << n->attr << " ";
	PrintNode( n->a );
	cout << " ";
	PrintNode( n->b );
    }
    cout << " )";
}

double CalcP( Node* n, map<string, bool> traits ) {
    if( n->children == false )
	return n->p;
    else if( traits[n->attr] == true ) {
	return n->p * CalcP( n->a, traits );
    }
    else
	return n->p * CalcP( n->b, traits );
}

int main() {

    std::ifstream ifs( "input.in" );
    std::ofstream out( "output.txt");
    int casecount;
    ifs >> casecount >> ws;



    for( int i=0; i<casecount; i++ ) {
	int d;
	ifs >> d >> ws;

	Node* n;
	n = ReadNode( ifs );
	//PrintNode( n );

	int animalcount;
	ifs >> animalcount;

	out << "Case #" << (i+1) << ":\n";

	for( int j=0; j<animalcount; j++ ) {
	    map< string, bool > traits;

	    string animalname;
	    ifs >> animalname;

	    int traitcount;
	    ifs >> traitcount;

	    string trait;
	    for( int k=0; k<traitcount; k++ ) {
		ifs >> trait;
		traits[trait] = true;
	    }

	    double p = CalcP( n, traits );
	    out << setiosflags(ios::fixed) << setprecision(7) << p << "\n";
	}

	// << ": " << ans << " " << n << "\n";
    }

}
