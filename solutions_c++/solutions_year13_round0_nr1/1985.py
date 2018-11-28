#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;


char M[10][10];

bool venceu (char c){
    f (i, 0, 4){
        int cnt = 0;
        f (j, 0, 4) if (M[i][j] == c || M[i][j] == 'T') cnt++;
        if (cnt == 4) return 1;
    }
    f (j, 0, 4){
        int cnt = 0;
        f (i, 0, 4) if (M[i][j] == c || M[i][j] == 'T') cnt++;
        if (cnt == 4) return 1;
    }
    int cnt = 0;
    for (int i = 0, j = 0; i < 4; i++, j++){
        if (M[i][j] == c || M[i][j] == 'T') cnt++;
    }
    if (cnt == 4) return 1;
    cnt = 0;
    for (int i = 0, j = 3; i < 4; i++, j--){
        if (M[i][j] == c || M[i][j] == 'T') cnt++;
    }
    if (cnt == 4) return 1;
    return 0;
}


int main (){
    int t;
    cin >> t;
    f (tt, 1, t+1){
        f (i, 0, 4) scanf(" %s", M[i]);
        //f (i, 0, 4) printf("%s\n", M[i]); printf("\n");
        int a= venceu('X');
        int b = venceu('O');
        int tem = 0;
        f (i, 0, 4) f (j, 0, 4) if (M[i][j] == '.') tem = 1;
        printf("Case #%d: ", tt);
        if (a) printf("X won\n");
        else if (b) printf("O won\n");
        else if (tem) printf("Game has not completed\n");
        else printf("Draw\n");
            
    }
    return 0;
}
