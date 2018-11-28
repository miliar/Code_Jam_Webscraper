#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int loop;
    cin>>loop;
    rep(j,loop){
        int tillnow_o=0,tillnow_b=0,flag,t_o,t_b,now_o=1,now_b=1,p;
        char c;
        int tot=0;
        int n;
        cin>>n;
        rep(i,n){
            cin>>c;cin>>p;
            if(i==0){ if(c=='O') flag=0; if(c=='B') flag=1;}
            if(c=='O'){
                t_o=abs(p-now_o)+1;
                if(flag==1){
                    if(tillnow_b>=t_o){
                        tot++;
                        tillnow_o=1;
                    }
                    else{tot+=t_o-tillnow_b; tillnow_o=t_o-tillnow_b;}}
                else{
                    tot+=t_o;
                    tillnow_o+=t_o;
                }
                flag=0;now_o=p;
            }
            else if(c=='B'){
                t_b=abs(p-now_b)+1;
                if(flag==0){
                    if(tillnow_o>=t_b){
                        tot++; tillnow_b=1;
                    }
                    else{ tot+=t_b-tillnow_o; tillnow_b=t_b-tillnow_o;}
                }
                else {
                    tot+=t_b;tillnow_b+=t_b;}
                flag=1;now_b=p;
            }
        }
        cout<<"Case #"<<j+1<<": "<<tot<<endl;
    }
	return 0;
}