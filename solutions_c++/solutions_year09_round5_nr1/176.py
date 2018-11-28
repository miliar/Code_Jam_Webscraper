#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
#define INF 10
using namespace std;

typedef long double ld;
typedef long long ll;


int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};


typedef vector<string> labr;

labr lab; // check for positions of walls
int rows,cols;
// x moves next rows, y moves next cols
int nboxes;

int gx[5],gy[5];

struct sta
{    
    int nx[5],ny[5];
    int moves;
    bool stable;
    
    void print()
    {
        cout << "fsf " << endl;
        FR(i,nboxes) cout << nx[i] << " " << ny[i] << endl;
        cout << moves << endl;
        cout << "fsf " << endl;
    }
    
    /*
    bool operator < ( const sta & state) const
    {           
        
        double est1=0,est2=0;
        FR(j,nboxes)
        {
            double a=100000;
            FR(i,nboxes)
            {
                a=min(a,fabs(gx[j]-this->nx[i])+fabs(gy[j]-this->ny[i]));
            }
            est1+=a;
        }
        
        FR(j,nboxes)
        {
            double a=100000;
            FR(i,nboxes)
            {
                a=min(a,fabs(gx[j]-state.nx[i])+fabs(gy[j]-state.ny[i]));
            }
            est2+=a;
        }                
        return (  (double)this-> moves +  est1  >
        (double)state.moves> +  est2);
    }*/
    
    
    bool operator < ( const sta & state) const
    {    
        return this->moves > state.moves;   
    }
};


priority_queue<sta> As;    
set<string> seen;
sta next;

string hsh(const sta& ss)
{
    stringstream ss2;
    FR(i,nboxes) ss2<<ss.nx[i]<<ss.ny[i];
    string res;
    ss2 >> res;
    return res;
}

bool finish()
{
    FR(i,nboxes)
    {
        bool b=false;
        FR(j,nboxes)
        {
            if(gx[j]==next.nx[i]&&gy[j]==next.ny[i])
            {
                b=true;break;
            }
        }
        if(!b) return false;
    }
    return true;
}

bool ok(int x, int y)
{
    return (x>-1&&y>-1&&x<rows&&y<cols&&lab[x][y]!='#');
}


sta nxt;

bool stb()
{
    if(nboxes==1) return true;
    FR(i,nboxes) // for each box
    {
        bool ok=false;
        FR(j,nboxes) // check if it is a neighbour to this box
        {        
            if(i==j) continue;
            FR(k,4)
            {
                int bx=nxt.nx[i]+dx[k];
                int by=nxt.ny[i]+dy[k];
                if(bx==nxt.nx[j]&&by==nxt.ny[j])
                {
                    ok=true;break;
                }
            }
            if(ok) break;
        }
        if(!ok) return false;
    }            
    return true;
}


void move()
{
    // if it is stable, the thing is valid
    // if it is not stable, it had to be stable before
        FR(i,nboxes) // for all boxes
        {
            FR(j,4) // for all movements
            {
                int bx=next.nx[i]+dx[j];
                int by=next.ny[i]+dy[j];
                if(!ok(bx,by)) continue;
                string s;
                FR(k,nboxes) // check that there is no box there
                {
                    if(next.nx[k]==bx&&next.ny[k]==by) goto CNT;
                }
                
                int bx2=next.nx[i]-dx[j];
                int by2=next.ny[i]-dy[j];
                if(!ok(bx2,by2)) continue;
                FR(k,nboxes) // check that there is no box there
                {
                    if(next.nx[k]==bx2&&next.ny[k]==by2) goto CNT;
                }
                
                
                
                
                
                FR(k,nboxes) // fill new boxes
                {
                    if(k!=i) nxt.nx[k]=next.nx[k];
                    else nxt.nx[k]=bx;
                    if(k!=i) nxt.ny[k]=next.ny[k];
                    else nxt.ny[k]=by;
                }
                nxt.moves=next.moves+1;
                nxt.stable=stb();
//                cout << "nxt " << endl;
//                nxt.print();
//                cout << "nxt " << endl;

                if(!nxt.stable&&!next.stable) continue;
                s= hsh(nxt);
                if(seen.find(s)==seen.end())
                {   
                    As.push(nxt);
                    seen.insert(s);
                }
            CNT:;
            }
        }        
}

// need additional check for some movements

int main()
{
    int n;
    scanf("%d",&n);
    FR(i,n)
    {
        while(!As.empty()) As.pop();
        lab.clear();
        seen.clear();
        int r,c;
        scanf("%d %d",&r,&c);
        FR(i,r)
        {
            string s;
            cin >> s;
            lab.PB(s);
        }
        rows=r;
        cols=c;
        nboxes=0;
        int ngoals=0;
        
        
        sta cur;
        FR(i,r)
            FR(j,c)
            if(lab[i][j]=='w')
            {
                gx[ngoals]=i;
                gy[ngoals++]=j;
                cur.nx[nboxes]=i;
                cur.ny[nboxes++]=j;
            }
            else if(lab[i][j]=='x')
            {
               gx[ngoals]=i;
               gy[ngoals++]=j;
            }        
            else if(lab[i][j]=='o')
            {
               cur.nx[nboxes]=i;
               cur.ny[nboxes++]=j;
            }
               
        cur.moves=0;
        
        nxt=cur;
        // check if the initial thing is stable
        bool con=stb();
        
        cur.stable=con;
        As.push(cur);
        while(!As.empty())
        {
            next=As.top();
  //          cout << "popped " << endl;
  //          next.print();
            if(finish())
            {
                cout << "Case #" << i+1 <<": " << next.moves << endl;
                goto AS;
            }
            As.pop();
            move();
        }
        cout << "Case #" << i+1 <<": " << -1 << endl;
    AS:;
    }
}