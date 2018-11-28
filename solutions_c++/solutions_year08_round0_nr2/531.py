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
#include <fstream>
#include <assert.h>
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define RFOR(i,a,b) for(int i = (a); i > (b);i--)
#define FORSZ(i,a,b) FOR(i,0,(b).size())
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort(ALL(a))
#define FSI(a) FORSZ(i, 0, (a))
#define FSJ(a) FORSZ(j, 0, (a))
#define FSK(a) FORSZ(k, 0, (a))
#define shift(n) (1<<(n))
#define shiftL(n) ((ll)(1<<(n)))
#define SQR(a) ((a)*(a))

using namespace std;

ifstream fin;
ofstream fout;

struct Trip
{
    int start;
    int end;
    Trip(int s, int e) : start(s), end(e) { }
    bool operator<(const Trip &t) const { 
        if(start == t.start) return end < t.end;
        return start < t.start ? true : false; 
    }
};

int timeFromString(string s)
{
    assert(s.length() == 5);
    int hr = atoi(s.substr(0, 2).c_str());
    int mi = atoi(s.substr(3).c_str());
    return hr * 60 + mi;
}

void solve(int delay, vector<Trip> &abTrips, vector<Trip> &baTrips, int &retA, int &retB)
{
    retA = 0;
    retB = 0;
    SORT(abTrips); 
    SORT(baTrips);
    
    bool A;
    int t = -1;

    while(!abTrips.empty() || !baTrips.empty()){
        if(!abTrips.empty() && (baTrips.empty() || abTrips[0] < baTrips[0])){
            retA++;
            A = 0;
            t = abTrips[0].end + delay;
            abTrips.erase(abTrips.begin());
        }
        else if (!baTrips.empty()) {
            retB++;
            A = 1;
            t = baTrips[0].end + delay;
            baTrips.erase(baTrips.begin());
        }
            
        while(!abTrips.empty() || !baTrips.empty()){
            bool keepGoing = false;
            if(A){
                FOR(i,0,abTrips.size()){
                    if(abTrips[i].start >= t){
                        A = 0;
                        t = abTrips[i].end + delay;
                        abTrips.erase(abTrips.begin() + i);
                        keepGoing = 1;
                        break;
                    }
                }
            }
            else{
                FOR(i,0,baTrips.size()){

                    if(baTrips[i].start >= t){
                        A = 1;
                        t = baTrips[i].end + delay;
                        baTrips.erase(baTrips.begin() + i);
                        keepGoing = 1;
                        break;
                    }
                }
            }
            if(!keepGoing) break;
        }
    }
}

void solveProblem()
{
    int nCases; fin >> nCases;
    FOR(tcase, 0, nCases){ 

        int delay, NAB, NBA;
        fin >> delay >> NAB >> NBA;
        fin.get();

        vector<Trip> abTrips, baTrips;

        FOR(i,0,NAB){
            char s[1000];
            fin.getline(s, 1000);            
            string L = ((string) s).substr(0, 5);
            string A = ((string) s).substr(6);
            int tL = timeFromString(L);
            int tA = timeFromString(A);
            abTrips.push_back(Trip(tL, tA));
        }
        FOR(i,0,NBA){
            char s[1000];
            fin.getline(s, 1000);            
            string L = ((string) s).substr(0, 5);
            string A = ((string) s).substr(6);
            int tL = timeFromString(L);
            int tA = timeFromString(A);
            baTrips.push_back(Trip(tL, tA));
        }

        int retA, retB;
        solve(delay, abTrips, baTrips, retA, retB);

        int ret = 0;
        cout << "Case #" << tcase+1 << ": " << retA << " " << retB << endl;
        fout << "Case #" << tcase+1 << ": " << retA << " " << retB << endl;

    }    
}




int main()
{
    fin.open("C:\\Users\\t-gregpa\\Documents\\Visual Studio 2008\\Projects\\GCJ\\in.txt");
    fout.open("C:\\Users\\t-gregpa\\Documents\\Visual Studio 2008\\Projects\\GCJ\\out.txt");
    solveProblem();  
    cout << "done" << endl;
    while(1);
}






















