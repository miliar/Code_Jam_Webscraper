#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<map>
#include<algorithm>

#define pb push_back
#define mp make_pair
#define fr first
#define se second
#define sc scanf
#define pr printf

const double eps = 1e-12;
const double PI = 3.1415926535898;
const int alphabet = 256;
const int MN = 100010;
const long long inf = (1LL<<60);

using namespace std;
struct pt{
    double x, y;
};
inline double sqr(double X){
    return (X*X);
}
inline double dist(pt a, pt b){
    return sqrt( sqr(a.x-b.x) + sqr(a.y-b.y) + eps);
}
inline double vector_m(pt a, pt b, pt c){
    return (b.x-a.x)*(c.y-a.y) - (c.x-a.x)*(b.y-a.y);
}
inline double scalar_m(pt a, pt b, pt c){
    return (b.x-a.x)*(c.x-a.x) + (b.y-a.y)*(c.y-a.y);
}
pt IntersectionOfLines(double A1, double B1, double C1, double A2, double B2, double C2){
    double D = A2*B1 - A1*B2;
    pt ans;
    if(fabs(D)<eps){
        ans.x = -inf;
        ans.y = -inf;
    }
    else{
        ans.x = (C1*B2 - C2*B1)/D;
        ans.y = (A1*C2 - A2*C1)/D;
    }
    return ans;
}
inline bool intersect(double a, double b, double c, double d){
    if(a>b)swap(a, b);
    if(c>d)swap(c, d);
    return (max(a, c)-min(b, d))<eps;
}
inline bool cmp (pt a, pt b) {
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

int t;
string s[5];
void Init(){
    int k;
    for(cin>>t, k=1; k<=t; k++){
        cout<<"Case #"<<k<<": ";
        bool emp = false, ans = false;
        for(int i=0; i<4; i++){
            cin>>s[i];
            for(int j=0; j<4; j++){
                if(s[i][j] == '.'){
                    emp = true;
                }
            }
        }
        for(int i=0; i<4; i++){
            bool FlagO = true, FlagX = true;
            for(int j=0; j<4; j++){
                if(s[i][j] != 'T' && s[i][j] != 'O'){
                    FlagO = false;
                }
                if(s[i][j] != 'T' && s[i][j] != 'X'){
                    FlagX = false;
                }
            }
            if(FlagO){
                cout<<"O won"<<endl;
                ans = true;
                break;
            }
            if(FlagX){
                cout<<"X won"<<endl;
                ans = true;
                break;
            }
        }
        if(!ans){
            for(int i=0; i<4; i++){
                bool FlagO = true, FlagX = true;
                for(int j=0; j<4; j++){
                    if(s[j][i] != 'T' && s[j][i] != 'O'){
                        FlagO = false;
                    }
                    if(s[j][i] != 'T' && s[j][i] != 'X'){
                        FlagX = false;
                    }
                }
                if(FlagO){
                    cout<<"O won"<<endl;
                    ans = true;
                    break;
                }
                if(FlagX){
                    cout<<"X won"<<endl;
                    ans = true;
                    break;
                }
            }
        }
        if(!ans){
            bool FlagO = true, FlagX = true;
            for(int i=0; i<4; i++){
                if(s[i][i] != 'T' && s[i][i] != 'O'){
                    FlagO = false;
                }
                if(s[i][i] != 'T' && s[i][i] != 'X'){
                    FlagX = false;
                }
            }
            if(FlagO){
                cout<<"O won"<<endl;
                ans = true;
            }
            if(FlagX){
                cout<<"X won"<<endl;
                ans = true;
            }
        }
        if(!ans){
            bool FlagO = true, FlagX = true;
            for(int i=0; i<4; i++){
                if(s[i][3-i] != 'T' && s[i][3-i] != 'O'){
                    FlagO = false;
                }
                if(s[i][3-i] != 'T' && s[i][3-i] != 'X'){
                    FlagX = false;
                }
            }
            if(FlagO){
                cout<<"O won"<<endl;
                ans = true;
            }
            if(FlagX){
                cout<<"X won"<<endl;
                ans = true;
            }
        }
        if(!ans){
            if(!emp){
                cout<<"Draw"<<endl;
            }
            else{
                cout<<"Game has not completed"<<endl;
            }
        }
    }
}

main(){
	freopen("input.txt", "r", stdin);	freopen("output.txt", "w", stdout);
	//freopen("paint.in", "r", stdin);	freopen("paint.out", "w", stdout);
    Init();
	return 0;
}
