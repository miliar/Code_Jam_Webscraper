#include<stdio.h>
#include<vector>
using namespace std;


typedef long long ll;
typedef struct {ll x;ll y;} point;
int N;

vector<point> V;
int main()
{
    scanf("%d", &N);
    int TC = 1;
    while(N--){
        V.clear();
        int n,A,B,C,D,x0,y0,M;
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        
        int X, Y;
        X = x0;
        Y = y0;
        point temp;
        temp.x = x0;
        temp.y = y0;
        V.push_back(temp);
        for(int i=1;i<n;i++){
            X = (ll(A)*X + B) % M;
            Y = (ll(C)*Y + D) % M;
            temp.x = X;
            temp.y = Y;
            V.push_back(temp);
        }
        
        int sum = 0;
        for(int a = 0;a<V.size();a++)
        for(int b=a+1;b<V.size();b++)
        for(int c=b+1;c<V.size();c++){
            if(a!=b && a!=c && b!=c){
                ll sx, sy;
                sx = V[a].x + V[b].x + V[c].x;
                sy = V[a].y + V[b].y + V[c].y;
                if(((sx%3)==0) && ((sy%3)==0))sum++;
            }
        }
        printf("Case #%d: %d\n",TC++, sum);
    }
    
    return 0;
}