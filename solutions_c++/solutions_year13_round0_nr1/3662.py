#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
#define ll long long
const long long LINF = ~(((long long)0x1)<<63)/2;
const int INF=0X3F3F3F3F;
const double eps=1e-7;
char a[5][5];
int main()
{
    int T;
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        for(int i=0;i<4;i++)
            cin>>a[i];
        bool flag=false;
        for(int i=0;i<4;i++)
        {
            flag=true;
            for(int j=0;j<4;j++)
                if(a[i][j]=='.'||a[i][j]=='O')
                    flag=false;
            if(flag) break;
            flag=true;
            for(int j=0;j<4;j++)
                if(a[j][i]=='.'||a[j][i]=='O')
                    flag=false;
            if(flag) break;
        }
        if(flag){ cout<<"X won"<<endl; continue;}
        flag=true;
        for(int i=0;i<4;i++) if(a[i][i]=='.'||a[i][i]=='O') flag=false;
        if(flag){cout<<"X won"<<endl; continue;}
        flag=true;
        for(int i=0;i<4;i++) if(a[i][3-i]=='.'||a[i][3-i]=='O') flag=false;
        if(flag){cout<<"X won"<<endl; continue;}
        
        
        flag=false;
        for(int i=0;i<4;i++)
        {
            flag=true;
            for(int j=0;j<4;j++)
                if(a[i][j]=='.'||a[i][j]=='X')
                    flag=false;
            if(flag) break;
            flag=true;
            for(int j=0;j<4;j++)
                if(a[j][i]=='.'||a[j][i]=='X')
                    flag=false;
            if(flag) break;
        }
        if(flag){ cout<<"O won"<<endl; continue;}
        flag=true;
        for(int i=0;i<4;i++) if(a[i][i]=='.'||a[i][i]=='X') flag=false;
        if(flag){cout<<"O won"<<endl; continue;}
        flag=true;
        for(int i=0;i<4;i++) if(a[i][3-i]=='.'||a[i][3-i]=='X') flag=false;
        if(flag){cout<<"O won"<<endl; continue;}
        
        flag=true;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(a[i][j]=='.') flag=false;
        
        if(!flag){
            cout<<"Game has not completed"<<endl;
        }
        else
            cout<<"Draw"<<endl;
        
    }
    return 0;
    
}






