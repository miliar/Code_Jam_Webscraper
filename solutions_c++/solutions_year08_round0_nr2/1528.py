#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

static const int N = 101;
char ibuffer[N];
typedef map<string, int> mapt;

void fill(ifstream &in, int n, list<int> &dep, list<int> &arr){

    for(int i=0; i < n; i++) {
        in.getline(ibuffer, N);
        string line(ibuffer);
        int si = line.find(' ');

        string d = line.substr(0,si),
               a = line.substr(si+1);

        dep.push_front(atoi(d.substr(0,2).c_str()) * 60 + 
                                                   atoi(d.substr(3,2).c_str()));
        arr.push_front(atoi(a.substr(0,2).c_str()) * 60 +
                                                   atoi(a.substr(3,2).c_str()));
    }

    dep.sort();
    arr.sort();

}

int count(int t, list<int> dep, list<int> arr){
    int c = 0;
    for( list<int>::iterator i = arr.begin();  i!=arr.end(); i++){
        int ready = t + *i;
        for( list<int>::iterator j = dep.begin(); j!=dep.end(); j++){
            cout << ready << " ss " << *j  << " &&&\n";
            if( ready <= *j ) { 
                c++;
                dep.erase(j);
                break;
            }
        }
    }
    return c;
}

void process_case(ifstream &in, int &na, int &nb){
    in.getline(ibuffer, N);
    int tournament = atoi(ibuffer);

    in.getline(ibuffer, N);
    string line(ibuffer); int si = line.find(' ');
    na = atoi(line.substr(0,si).c_str());
    nb = atoi(line.substr(si).c_str());
    cout << na << " *** " << nb << endl;

    list<int> da, aa, db, ab;
    fill(in, na, da, aa);
    fill(in, nb, db, ab);

    na -= count(tournament, da, ab);
    nb -= count(tournament, db, aa);
}

int main (int argc, char **argv) {
    
    ofstream out;
    ifstream in;
    if(argc < 2) {
        cerr << "Usage: " << argv[0] << " <input filename> [output filename]\n";
        return -1;
    } else {
        in.open(argv[1]);
    }
    
    if(argc > 2){
        out.open(argv[1]);
    } else {
        out.open("out.dat");
    }

    in.getline(ibuffer, N);
    int ncases = atoi(ibuffer);

    for(int i = 0; i < ncases; i++){
        int na, nb;
        process_case(in, na, nb); 
        out << "Case #" << (i+1) << ": " << na << " " << nb << endl;
    }

    out.close();
}

