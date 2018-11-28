#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int bip(vector<vector<int> >& G) {
        int A = G.size();
        int B = G[0].size();
        vector<int> matched(A,0), match(A,0);
 
        for (int j=0;j<B;j++) {
                vector<int> seen(A,0), from(A,-1);
                queue<int> Q;
                for (int i=0;i<A;i++) if (G[i][j]) {Q.push(i); seen[i]=1;}
                int found=0;
                while (!Q.empty()) {
                        int where = Q.front(); Q.pop();
                        if (!matched[where]) {
                                found=1;
                                matched[where]=1;
                                while (1) {
                                        if (from[where]==-1) { match[where]=j; break; }
                                        match[where] = match[ from[where] ];
                                        where = from[where];
                                }
                                break;
                        }
                        int neighbor = match[where];
                        for (int i=0;i<A;i++) if (G[i][neighbor]) if (!seen[i]) {Q.push(i); seen[i]=1; from[i]=where;}
                }
 
        }
        int ret=0;
        for (int i=0;i<A;i++) { ret+=matched[i]; G[i][match[i]]=0;}
        return ret;
 
}

int m,n;

int pr(int x,int y) {
    if (y%2==0) return x*(n+1)/2+y/2;
    else return x*(n/2)+y/2;
}

int main() {
    int cases;
    cin>>cases;
    for (int tt=1;tt<=cases;tt++) {
        
        cin>>m>>n;
        vector<string> v(m,"");
        for (int i=0;i<m;i++) cin>>v[i];
        int good=0;
        vector<VI> g=vector<VI>(m*((n+1)/2)+10,VI(m*((n)/2)+10,0));

        for (int i=0;i<m;i++) for (int j=0;j<n;j++) {
            
            if (v[i][j]=='.') {
                good++;
                if (i!=0&&j!=0&&v[i-1][j-1]=='.') {
                    if (j%2==0) g[pr(i,j)][pr(i-1,j-1)]=1;
                    else g[pr(i-1,j-1)][pr(i,j)]=1;
                }
                 if (i!=0&&j!=n-1&&v[i-1][j+1]=='.') {
                    if (j%2==0) g[pr(i,j)][pr(i-1,j+1)]=1;
                    else g[pr(i-1,j+1)][pr(i,j)]=1;
                }
                  if (j!=0&&v[i][j-1]=='.') {
                    if (j%2==0) g[pr(i,j)][pr(i,j-1)]=1;
                    else g[pr(i,j-1)][pr(i,j)]=1;
                }
                   if (j!=n-1&&v[i][j+1]=='.') {
                    if (j%2==0) g[pr(i,j)][pr(i,j+1)]=1;
                    else g[pr(i,j+1)][pr(i,j)]=1;
                }
           }
            
        }
        cout<<"Case #"<<tt<<": "<<good-bip(g)<<endl;


    }
}
