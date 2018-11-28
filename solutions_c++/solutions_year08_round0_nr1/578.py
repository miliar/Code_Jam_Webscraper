/* GCJ Qualification [Saving the Universe] - SJEDDIE 2008 */
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

int S, Q;
map<string,int> eng;
string engName;

int qu [1005];
vector <bool> used (105);
int complex;
int swtch;

int main() {
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    int noOfCases;
    fin >> noOfCases;
    FORE (i, noOfCases) {
         fin >> S;
         
         eng.clear();
         used.clear();
         FORE (j,1005) qu[j] = -1;
         
         FORE (s,S+1) {
              getline (fin,engName);
              eng [engName]=s;
         }     
         fin >> Q;
         FORE (q,Q+1) {
              getline (fin,engName);
              qu [q] = eng [engName];
         }
         
         FORE (j,S+1) used [j] = 0;
         complex = 0;
         swtch = 0;
         
         //fout <<(i+1) << " " << S << " : ";
         //FOR (q,1,Q+1)fout << qu[q] << " ";
         //fout << endl;
         
         FOR (q,1,Q+1) {
            // fout << "    " << qu[q] << endl;
             if (!used [qu[q]]) {
                used [qu[q]] = 1;
                complex++;
               // fout << "    " << "COMPLEX " << complex << endl;
                if (complex == S) {
                   swtch++;   
                   FORE (j,S+1) used [j] = 0;
                   complex = 1;
                   used [qu[q]] = 1;
                   //fout << "    " << "swtch " << swtch << endl;
                }    
             } 
         }
         fout << "Case #" << (i+1) << ": " << swtch << endl;
    }
   // system("PAUSE");
    return 0;
}
