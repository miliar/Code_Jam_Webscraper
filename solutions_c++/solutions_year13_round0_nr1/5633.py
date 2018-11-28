//#includes {{{
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <complex>
#include <list>
#include <stack>
#include <queue>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;
// }}}
// #defines {{{
#define sz(a) int((a).size())
#define pb push_back

#define all(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=a; i<(int(b)); i++)
#define tr(it, container) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;

template<class T>
void splitline(const string &s, vector<T> &dest) {
    istringstream in(s);
    dest.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(dest));
}
template<class T>
inline void PRINT_ELEMENTS(const T& coll, const char* optcstr=""){
    typename T::const_iterator pos;
    std::cout<< optcstr;
    for(pos=coll.begin();pos!=coll.end();++pos){
        cout << *pos << ' ';
    }
    cout << endl;
}
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
int s2i(string str){
    stringstream ss; int n;
    ss << str; ss >> n; return n; }
string i2s(int n){
stringstream ss; string str;
ss << n; ss >> str; return str; }
// }}}

char a[4][4];
int check(int c1,int c2, int dot){
    a[c1][c2]='O';
    for(int i=0;i<4;i++) if(a[i][0]=='O'&&a[i][1]=='O'&&a[i][2]=='O'&&a[i][3]=='O') return 1;
    for(int i=0;i<4;i++) if(a[0][i]=='O'&&a[1][i]=='O'&&a[2][i]=='O'&&a[3][i]=='O') return 1;
    if(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='O') return 1;
    if(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='O') return 1;
    a[c1][c2]='X';
    for(int i=0;i<4;i++) if(a[i][0]=='X'&&a[i][1]=='X'&&a[i][2]=='X'&&a[i][3]=='X') return 2;
    for(int i=0;i<4;i++) if(a[0][i]=='X'&&a[1][i]=='X'&&a[2][i]=='X'&&a[3][i]=='X') return 2;
    if(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='X') return 2;
    if(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='X') return 2;
    a[c1][c2]='T';
    if(dot==0) return 3;
    if(dot>0) return 4;
}
int main(int argc, char*argv[]){
    //codejam
    int t;
    scanf("%d\n",&t);
    for(int z=0;z<t;z++) {
        //memset(a, '.', sizeof a);
        char ch; int dot=0; int c1,c2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) {
                scanf("%c",&ch);
                a[i][j] =ch;
                if(ch=='.') dot++;
                if(ch == 'T') {c1=i;c2=j;}
            } scanf("%c",&ch);//cout<<endl;
        } scanf("%c",&ch);
        int res = check(c1,c2,dot);
        printf("Case #%d: ",z+1);
        switch(res){
            case 1: printf("O won");
                    break;
            case 2: printf("X won");
                    break;
            case 3: printf("Draw");
                    break;
            case 4: printf("Game has not completed");
                    break;
        }
        printf("\n");
    }
}

// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread


