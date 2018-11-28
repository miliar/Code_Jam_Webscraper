#include<iostream>
#include<string>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<bitset>
#include<sstream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cctype>

#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,b) for(int a=b-1;a>=0;a--)
#define INR(a,b) (0<=a && a<b)
#define CLEAR(a,b) memset(a,b,sizeof a)

#define PB push_back
#define LLI long long
#define PII pair<int,int>
#define MKP make_pair
#define VI vector<int>
#define VS vector<string>
#define VVI vector< vector<int> >
#define VVS vector< vector< string > >
#define IT iterator

#define MAX 101

using namespace std;

int m, n;

char grid[51][51];

char sym[4] = {'/','\\','\\','/'};

bool possible(){
    FOR(i,m){
        FOR(j,n){
            if( grid[i][j] == '#'){
                if( i+1 >= m || j+1 >= n)
                    return false;
                FOR(ii,2)
                    FOR(jj,2){
                        if(grid[i+ii][j+jj]!='#')
                            return false;
                        grid[i+ii][j+jj] = sym[ii*2+jj];
                    }
            }
        }
    }

    return true;
}


int main(){

    int t;

    cin >> t;

    FOR(t_n,t){

        cin >> m >> n;
        getchar();
        FOR(i,m){
            FOR(j,n)
                grid[i][j]=getchar();
            getchar();
        }
        cout << "Case #"<<t_n+1<<":\n"; 
        if( possible() ){
            FOR(i,m){
                FOR(j,n)
                    putchar(grid[i][j]);
                putchar('\n');
            }
        }
        else{
            cout << "Impossible\n";
        }
    }
    return 0;
}
