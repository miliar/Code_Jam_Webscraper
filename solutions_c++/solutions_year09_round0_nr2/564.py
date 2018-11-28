#include <iostream>
#include <queue>
#define REP(i,n) for (i=0;i<n;++i)
#define FOR(i,a,b) for (i=a;i<=b;++i)
using namespace std;

const int MAXSIZE=100;
const int MAXVAL=1000;

int t,h,w;
int i,j,k,u,m,n,x,y,cc,ccc;
int nu,nv,c,minval,mindir;
int a[MAXSIZE+2][MAXSIZE+2],r[MAXSIZE+2][MAXSIZE+2];
int dh[]={-1,0,0,1};
int dw[]={0,-1,1,0};
queue<pair<int,int> > q,q2;

main(){
  freopen("watershed.in","r",stdin);
  freopen("watershed.out","w",stdout);
  cin>>t;
  FOR(i,1,t){
    c=96;
    cin>>h>>w;
  
    //INPUT
    FOR(j,1,w) {a[0][j]=a[h+1][j]=10000;}
    FOR(j,1,h){
      a[j][0]=a[j][w+1]=10000;
      FOR(k,1,w) cin>>a[j][k];
    }
    
    /*
    REP(j,h+2) {
      REP(k,w+2) cout<<a[j][k]<<" ";
      cout<<endl;
    }
    */
    
    memset(r,0,sizeof(r));
    
    //LOOP THROUGH
    FOR(j,1,h) FOR(k,1,w) {
      if (r[j][k]==0) {
        ++c;
        r[j][k]=c;
        q.push(make_pair(j,k));
        while (!q.empty()){
          m=q.front().first; n=q.front().second; q.pop();
          /*
          cout << m << " " << n << endl;
          */
          minval=a[m][n]; mindir=-1;
          REP(u,4){
            nu=m+dh[u]; nv=n+dw[u];
            if (a[nu][nv]<minval) {minval=a[nu][nv]; mindir=u;}
          }
          if (mindir!=-1){
            nu=m+dh[mindir]; nv=n+dw[mindir];
            /*
            cout << j << " " << k << " " << nu << " " << nv << endl;
            */
            if (r[nu][nv]==0) { 
              r[nu][nv]=c;
              q.push(make_pair(nu,nv));
            }
            else { 
              --c;
              cc=r[nu][nv];
              ccc=r[m][n];
              /*
              cout << cc << " " << ccc << endl;
              */
              q2.push(make_pair(m,n));
              while (!q2.empty()){
                x=q2.front().first; y=q2.front().second; q2.pop();
                r[x][y]=cc;
                REP(u,4){
                  nu=x+dh[u]; nv=y+dw[u];

                  if (r[nu][nv]==ccc) {
                    q2.push(make_pair(nu,nv));
                    /*
                    cout << nu << " " << nv << " " << r[nu][nv];
                    system("PAUSE");
                    */
                  }
                }
              }
            }
          }
        }
      }
    }
    cout<<"Case #"<<i<<":"<<endl;
    FOR(j,1,h){
      FOR(k,1,w) cout<<char(r[j][k])<<" ";
      cout<<endl;
    }
  }
}
