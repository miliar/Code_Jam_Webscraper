//	ID : pallab81
// 	PROG : A
// 	LANG : C++
// 	2011-05-22-14.59.55 Sunday
//
// 	"I have not failed, I have just found 10000 ways that won't work.
//


#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <bitset>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>

using namespace std;

#define  CI( x ) scanf( "%d", &x )

#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VC vector<char>
#define VVC vector<VC >
#define VB vector<bool>
#define VVB vector<VB >
#define PAIR pair<int,int>
#define VP vector<PAIR >
#define fo(i,st,ed) for(int i = st; i < ed ; ++i)
#define foE(i,st,ed) for(int i = st; i <= ed ; ++i)
#define foit(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define bip system("pause")
#define mk make_pair
#define f first
#define s second
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()
#define ll long long
#define IO ifstream cin(".in") ; ofstream cout(".out");

VVC mat;
int R,C;
bool possible;
inline void read(){
    cin>>R>>C;
    mat.assign(R, VC(C,'.'));
    fo(i,0,R){
        fo(j,0,C){
            cin>>mat[i][j];
        }
    }
}

int move[4][2]={ {0,0},{0,1},{1,0},{1,1} };
char cc[4]={'/','\\','\\','/'};

inline void colorIt(){
    possible=true;
    fo(i,0,R){
        fo(j,0,C){
            if(mat[i][j]=='#'){
                int total=0;
                fo(k,0,4){
                    int tr = i+move[k][0];
                    int tc = j+move[k][1];
                    if(tr<0 || tc<0 || tr>=R || tc>=C)continue;
                    if(mat[tr][tc]=='#'){
                        total++;
                        mat[tr][tc]= cc[k];
                    }
                }
                //cout<<i<<" "<<j<<total<<"\n";bip;
                if(total!=4){
                    possible=false;
                    return ;
                }
            }
        }
    }
}

inline void proc(int case_){
    printf("Case #%d:\n",case_);
    if(possible==false){
        printf("Impossible\n");
    }
    else{
        fo(i,0,R){
            fo(j,0,C){
                cout<<mat[i][j];
            }
            cout<<"\n";
        }
    }
}

int main(){
    int case_;
    cin>>case_;
    foE(i,1,case_){
        read();
        colorIt();
        proc(i);
    }
return 0;
}

