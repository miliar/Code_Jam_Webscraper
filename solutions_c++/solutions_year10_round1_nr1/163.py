#include <iostream>
#include <vector>
using namespace std;
#define read(a) scanf("%d",&a)
#define For(i,a,b) for(int i =(a);i<(b);++i)
typedef pair<int, int> pii;
typedef vector<int> vi;

#define isValid(x,y) (((x)>=0)&&((x)<n)&&(((y)>=0)&&((y)<n)))
#define check(x,y,dx,dy){\
    int count=0;char last ='X';\
    for(int curX=(x),curY=(y); isValid(curX,curY); curX+=dx,curY+=dy){\
        if(grid[curY][curX] != last)\
            last = grid[curY][curX],count=0; \
        ++count;\
        if(count>=k)wins[last]=true;\
    }\
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int total;read(total);
    char*solutions[] = {"Neither","Red","Blue","Both"};

    for(int times=1;times<=total;++times){
        int n,k;read(n);read(k);
        string grid[n];
        For(i,0,n){
            cin>>grid[i];

            for(int j = n,lastGood=n; j-- > 0; ){
                char cur = grid[i][j];
                grid[i][j]='.';
                if(cur!='.')
                    grid[i][--lastGood]=cur;
            }
           // cout<<grid[i]<<endl;
        }
        bool wins[256];wins['B']=wins['R']=false;
        For(i,0,n){
            check(i,0,0,1);
            check(0,i,1,0);
            check(i,0,1,1);
            check(i,0,-1,1);
            check(0,i,1,1);
            check((n-1),i,-1,1);
        }
        int type = (wins['B']?2:0)+(wins['R']?1:0);

        printf("Case #%d: %s\n",times,solutions[type]);
    }
    return 0;
}
