/* GCJ Qualification [Train Timetable] - SJEDDIE 2008 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <list>
#include <sstream>

using namespace std;

#define uint unsigned int
#define llong long long
#define ullong unsigned long long
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define FORE(i,a) FOR(i,0,a)
#define PB push_back
#define MP make_pair

#define DAY 1440

struct slot {
       int ABs, ABe, BAs, BAe;
};

vector < slot > tim;
int push, na, nb;
int a,b,c,d,st,et;

int A,B,minA,minB;

int main() {
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    int noOfCases;
    fin >> noOfCases; 
    FORE (nn,noOfCases) {
         
    tim.clear();
    FORE (i,DAY) tim.PB ((slot) {0,0,0,0});
             
        fin >> push >> na >> nb;
        fin.get(); //eol
        FORE (nna,na) {
        a = fin.get()-'0';
        b = fin.get()-'0';
        fin.get (); // :
        c = fin.get()-'0';
        d = fin.get()-'0';
        st = (a*10+b)*60 + (c*10+d);
        
        fin.get (); // _
        
        a = fin.get()-'0';
        b = fin.get()-'0';
        fin.get (); // :
        c = fin.get()-'0';
        d = fin.get()-'0';
        
        et = (a*10+b)*60 + (c*10+d);
        
        tim [st].ABs ++;
        if (et+push < DAY)
        tim [et+push].ABe ++;
        fin.get(); //eol
        }
        
        FORE (nna,nb) {
        a = fin.get()-'0';
        b = fin.get()-'0';
        fin.get (); // :
        c = fin.get()-'0';
        d = fin.get()-'0';
        
        st = (a*10+b)*60 + (c*10+d);
        
        fin.get (); // _
        
        a = fin.get()-'0';
        b = fin.get()-'0';
        fin.get (); // :
        c = fin.get()-'0';
        d = fin.get()-'0';
        
        et = (a*10+b)*60 + (c*10+d);
        
        tim [st].BAs ++;
        if (et+push < DAY)
        tim [et+push].BAe ++;
        fin.get(); //eol
        }
        
        minA = minB = 99999;
        A = B = 0;
        
        FORE (i,DAY) {
             A -= tim[i].ABs;
             A += tim[i].BAe;
             B -= tim[i].BAs;
             B += tim[i].ABe;
             if (A < minA) minA = A;
             if (B < minB) minB = B;
            // if (i == ) cout << B << endl;
        }
        if (minA > 0) minA = 0;
        if (minB > 0) minB = 0;
        fout << "Case #" << (nn+1) << ": " << (-minA) << " " << (-minB) << endl;  // omg nn+1 costed me a turn :(
    }

    //system("PAUSE");
    return 0;
}
