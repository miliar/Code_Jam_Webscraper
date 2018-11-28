#include <cstring>
#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cctype>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <utility>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

using namespace std;
#define fr(i,j,k) for (int (i) = (j); (i) < (k); (i)++)
#define frd(i,j,k) for (int (i) = (j); (i) >= (k); (i)--)
#define ms(ar,a) memset(ar, a, sizeof(ar))
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<
#define ler(a) scanf("%d", &a)
#define ler2(a,b) scanf("%d%d", &a, &b)
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
const double PI = acos(-1.0);
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
#define MAXN 100

string s[4];

int main(){

	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
    int t;
    int caso = 1;
    ler(t);
    while(t--){
        for(int i = 0;i<4;i++){
            cin >> s[i];
        }
        bool rodar = true;
        bool podex, podeo;
        string resp;
        for(int i=0;i<4 && rodar;i++){
            podex = true;
            for(int j=0; j<4;j++){
                if( !(s[i][j] == 'X' || s[i][j] == 'T') ){
                    podex = false;
                }
            }
            if(podex){
                resp = "X won";
                rodar = false;
                break;
            }
            podex = true;
            for(int j=0; j<4 ;j++){
                if( !(s[j][i] == 'X' || s[j][i] == 'T') ){
                    podex = false;
                }
            }
            if(podex){
                resp = "X won";
                rodar = false;
                break;
            }
            podeo = true;
            for(int j=0; j<4 ;j++){
                if(!(s[i][j] == 'O' || s[i][j] == 'T')){
                    podeo = false;
                }
            }
            if(podeo){
                resp = "O won";
                rodar = false;
                break;
            }
            podeo = true;
            for(int j=0; j<4 ;j++){
                if(!(s[j][i] == 'O' || s[j][i] == 'T')){
                    podeo = false;
                }
            }
            if(podeo){
                resp = "O won";
                rodar = false;
                break;
            }
        }
        if(rodar){
            podex = true;
            for(int i = 0;i<4;i++){
                if( !(s[i][i] == 'X' || s[i][i] == 'T') ){
                podex = false;
                }
            }
            if(podex){
                resp = "X won";
                rodar = false;
            }

            podeo = true;
            for(int i=0; i<4 ;i++){
                if(!(s[i][i] == 'O' || s[i][i] == 'T')){
                    podeo = false;
                }
            }
            if(podeo){
                resp = "O won";
                rodar = false;
            }

            podex = true;
            for(int i = 0;i<4;i++){
                if( !(s[3-i][i] == 'X' || s[3-i][i] == 'T') ){
                podex = false;
                }
            }
            if(podex){
                resp = "X won";
                rodar = false;
            }

            podeo = true;
            for(int i=0; i<4 ;i++){
                if(!(s[3-i][i] == 'O' || s[3-i][i] == 'T')){
                    podeo = false;
                }
            }
            if(podeo){
                resp = "O won";
                rodar = false;
            }
        }
        if(rodar){
            bool empate = true;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(s[i][j] == '.'){
                        empate = false;
                    }
                }
            }
            if(!empate){
                resp = "Game has not completed";
            }else{
                resp = "Draw";
            }
        }
        printf("Case #%d: ",caso++);
        cout << resp << endl;
    }
	return 0;
}
