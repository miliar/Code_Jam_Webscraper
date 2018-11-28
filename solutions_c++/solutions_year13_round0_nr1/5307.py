/* 
 * File:   main.cpp
 * Author: Tivi
 *
 * Created on 13. huhtikuuta 2013, 22:56
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream in("A-large.in");
    //ostream& out = cout;
    ofstream out("out.txt");
    
    int cases;
    in>>cases;
    
    char map[4][4];
    
    string a;
    for( int ca=1; ca<=cases; ca++ ) {
        getline(in, a); //blanko
        for( int j=0; j<4; j++ ) {
            getline(in,a);
            for( int i=0;i<4; i++ ) {
                map[i][j] = a[i];
            }
        }
        
        bool xwon=false;
        bool owon=false;
        bool draw=false;
        
        for( int j=0; j<4; j++ ) {
            int xs=0, os=0, ds=0, ts=0;
            for( int i=0; i<4; i++ ) {
                char c=map[i][j];
                if( c=='O' ) os++;
                else if( c=='X' ) xs++;
                else if( c=='T' ) ts++;
                else if( c=='.' ) ds++;
            }
            if( ds==0 && os==0 ) xwon=true;
            if( ds==0 && xs==0 ) owon=true;
        }
        for( int i=0; i<4; i++ ) {
            int xs=0, os=0, ds=0, ts=0;
            for( int j=0; j<4; j++ ) {
                char c=map[i][j];
                if( c=='O' ) os++;
                else if( c=='X' ) xs++;
                else if( c=='T' ) ts++;
                else if( c=='.' ) ds++;
            }
            if( ds==0 && os==0 ) xwon=true;
            if( ds==0 && xs==0 ) owon=true;
        }{
            int xs=0, os=0, ds=0, ts=0;
            for( int j=0; j<4; j++ ) {
                char c=map[j][j];
                if( c=='O' ) os++;
                else if( c=='X' ) xs++;
                else if( c=='T' ) ts++;
                else if( c=='.' ) ds++;
            }
            if( ds==0 && os==0 ) xwon=true;
            if( ds==0 && xs==0 ) owon=true;
        }{
            int xs=0, os=0, ds=0, ts=0;
            for( int j=0; j<4; j++ ) {
                char c=map[3-j][j];
                if( c=='O' ) os++;
                else if( c=='X' ) xs++;
                else if( c=='T' ) ts++;
                else if( c=='.' ) ds++;
            }
            if( ds==0 && os==0 ) xwon=true;
            if( ds==0 && xs==0 ) owon=true;
        }
        draw=true;
        
        for( int i=0; i<4; i++ )
            for( int j=0; j<4; j++ )
                if( map[i][j] == '.' )
                    draw=false;
            
        out << "Case #" << ca << ": ";
        if( xwon ) out << "X won";
        else if( owon ) out << "O won";
        else if( draw ) out << "Draw";
        else out << "Game has not completed";
        out << endl;
        
        /*for( int j=0; j<4; j++ ) {
            for( int i=0;i<4; i++ )
                cout << map[i][j];
            cout << endl;
        }*/
    }
    //for( int i=0; )
    return 0;
}

