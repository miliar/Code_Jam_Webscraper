#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <string>
#include <cassert>
#include <iostream>
using namespace std;

map <string, int> name2Id;
vector<int> s; // search stream
map <int, map<int, int> > m;
vector<int> bindex;

void clear(){
    bindex.clear();
    name2Id.clear();
    s.clear();
    m.clear();
}

int parseCase(ifstream & f){
    clear();
    // read a line to get engine number
    int eCount;
    f>>eCount;
    cout<<"this case has "<<eCount<<"search engines.\n";
    char buf[1024];
    f.getline(buf, 1024);
    for (int i=1; i<=eCount; ++i){
        string ename;
        getline(f, ename);
        cout<<i<<":  "<<ename<<endl;
        name2Id[ename] = i;
    }
    f>>eCount;
    f.getline(buf,1024);
    // read in the stream
    string lastName;
    for (int i=0; i<eCount; ++i){
        string ename;
        getline(f, ename);
        if (ename==lastName) continue;
        lastName = ename;
        assert(name2Id[ename]);
        s.push_back(name2Id[ename]);
    }

    return s.size()-1;
}
int run(int a, int b){
    //[a,b]
    if (m.count(a) && m[a].count(b)){
        return m[a][b];
    }
    if (a==b){
        m[a][b]=0;
        return 0;
    }

    set <int> v;
    for (int i=a; i<=b; i++){
        // check if 0
        v.insert(s[i]);
    }
    if (v.size()<name2Id.size()){
        m[a][b]=0;
        return 0;
    }
    set<int> visited;
    // dp
    int result = 10000000;
	// no need to visit in order!
	int m1 = (a+b)/2;
	visited.clear();
    for (int i=a; i<b; ++i){
        visited.insert(s[i]);
        if (run(a,i) + run(i+1,b)<result){
            result = run(a,i)+run(i+1,b)+1;
        }
	    if (visited.size()>=name2Id.size()){
            assert(result<10000000);
            m[a][b]=result;
            return result;
        } 
    }
    assert(result<10000000);
	m[a][b] = result;
	return result;
}

int main(){
    ifstream f ("input.file");
    ofstream fout ("output");
    int numCases =0;
    f>>numCases;
    cout<<"get "<<numCases<<"\n";
    for (int i=1; i<=numCases; i++){
        fout<<"Case #"<<i<<": "<<run(0, parseCase(f))<<endl;
    }
    return 0;
}
