#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <fstream>


using namespace std;


#define pb push_back

ifstream iff("a.in");
ofstream off("a.out");

void input(int N, int M);
void calculate();
void print_result(int cases);

set<string> s;
vector<string> ap;
vector<string> target;
int tot;

int main(void) {
    int T , N, M;

    iff>>T;
    cout<<T<<endl;

    for ( int i = 0 ; i < T ; i ++ ) {
        tot = 0;
        s.clear();
        target.clear();
        ap.clear();
        iff>>N>>M;
        cout<<N<<M<<endl;
        input(N,M);
        calculate();
        print_result(i+1);
    }

    return 0;
}

void input(int N, int M) {
    string in;
    for ( int i = 0 ; i < N ; i ++ ) {
        iff>>in;
        ap.pb(in);
    }

    for ( int j = 0 ; j < M ; j ++ ) {
        iff>>in;
        target.pb(in);
    }
}


void calculate() {

    string tmp = "";

    for ( int i = 0 ; i < ap.size() ; i ++ ) {
        tmp = "" ;
        for ( int j = 0 ; j < ap[i].size() ; j ++ ) {
            if(ap[i][j]=='/') {
                if(j!=0)
                    s.insert(tmp);
            }

            tmp += ap[i][j];
        }
        s.insert(tmp);
    }

    cerr<<s.size()<<" is"<<endl;

    tot = 0;


    for ( int i = 0 ; i < target.size() ; i ++ ) {
        tmp = "";
        for ( int j = 0 ; j < target[i].size() ; j ++ ) {
            if(target[i][j]=='/') {

                if(j!=0) {
                    if(s.count(tmp)==0) {
                        tot ++;
                        s.insert(tmp);
                        cerr<<tmp<<endl;
                    }
                }
            }

            tmp += target[i][j];

        }


        if(s.count(tmp)==0) {
            tot++;
            cerr<<tmp<<endl;
            s.insert(tmp);
        }
    }

}

void print_result(int cases) {
    off<<"Case #"<<cases<<": "<<tot<<endl;
    //off<<"Case #"<<cases<<": "<<tot<<endl;
}





