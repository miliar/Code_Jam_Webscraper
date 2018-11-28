#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime>  
 
using namespace std;
 
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long LL; 
typedef pair<int,int> PII; 
typedef pair<string,string> PSS; 
 
#define pb push_back 
#define all(a) a.begin(), a.end() 
 
#define ss stringstream 
 
#define F(a,b,i) for(int i=a; i<b; ++i)   
#define FE(it,s) for (__typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)  
#define R(a,b,i) for(int i=b-1; i>=a; --i) 
  
/*  debug  */ 
#define D(x) cout << #x << " = "<< x <<endl; 
#define PV(label,x) cout<<label<<"=[ "; FE(it,x) cout<<*it<<" "; cout<<"]"<<endl; 
#define PM(label,x) cout<<label<<endl; FE(it,x){cout<<label<<"["<<it->first<<"]="<<it->second<<endl;}

int main(){
    int t,h,w;
    cin>>t;
    for(int nc=0;nc<t;nc++){
        cin>>h>>w;
        VI v(w,0);
        vector< VI > m(h,v);
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                cin>>m[i][j];
            }
        }
        string vs(w,' ');
        VS vr(h,vs);
        int di[4]={-1, 0, 0,+1};
        int dj[4]={ 0,-1, 1, 0};
        char f='a';
        
        for(int x=0;x<h;x++)
        {
            for(int y=0;y<w;y++)
            {
                if(vr[x][y]==' ')
                {
                    int pos=x*w+y;
                    queue<int> Q;
                    Q.push(pos);
                    VI v; v.push_back(pos);
                    char f2=' ';
                    while( !Q.empty() ){
                        int u=Q.front();
                        Q.pop();
                        v.push_back(u);
                        int ui=u/w; int uj=u%w;
                        
                        int mn=1000000;
                        int post=-1;
                        for(int a=0;a<4;a++){
                            int vi=ui+di[a];
                            int vj=uj+dj[a];
                            
                            if(0<=vi&&vi<h &&  0<=vj&&vj<w ){
                                if( m[vi][vj] < mn ){
                                    post=vi*w+vj;
                                    mn=m[vi][vj];
                                }
                            }
                        }
                        if(post!=-1 && mn< m[ui][uj] ){
                            int ri=post/w;
                            int rj=post%w;
                            if( vr[ri][rj]==' '){
                                Q.push(post);
                                v.push_back(post);
                            }
                            else{
                                f2=vr[ri][rj];
                                goto next;
                            }
                        }
                    }
                    next:
                    if(f2!=' '){
                        for(int z=0;z<v.size();z++){
                            vr[v[z]/w][v[z]%w]=f2;
                        }
                    }
                    else{
                        for(int z=0;z<v.size();z++){
                            vr[v[z]/w][v[z]%w]=f;
                        }                        
                        f++;
                    }
                }
            }                
        }
        cout<<"Case #"<<nc+1<<":"<<endl;
        for(int x=0;x<h;x++)
        {
            for(int y=0;y<w;y++){
                cout<<vr[x][y];
                if(y!=w-1) cout<<" ";
            }
            cout<<endl;
        }
        
    }
}

