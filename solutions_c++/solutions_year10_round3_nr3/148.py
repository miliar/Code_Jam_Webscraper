#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

const int maxn = 1000;
int T,M,N;
int c[maxn][maxn];

bool cut(int x,int y,int s)
{
    int i,j,k;
    bool ok=false;
    int f=0,t=0;
    
    if(c[x][y]==0)f=0;
    else f=1;

    for(i=x;i<x+s;i++)
    {
        //if( f==0 )t=1;//101010
        //else t=0;//010101

        t=f;
        for(j=y;j<y+s;j++)
        {
            if( c[i][j]==-1 || c[i][j] !=t )return false;
            t=1-t;            
        }

        f=1-f;
    }

    for(i=x;i<x+s;i++)
    {
        for(j=y;j<y+s;j++)c[i][j]=-1;
    }

    return true;
}

int main(){    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j,k;
    char str[1000];
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>M>>N;
        memset(c,0,sizeof(c));
        for(i=0;i<M;i++){
            cin>>str;
            for(j=0;j<N/4;j++)
            {
                int tmp;
                if( isdigit(str[j]) )tmp = str[j]-'0';
                else tmp = str[j]-'A' + 10;

                for(k=0;k<4;k++)
                {
                    c[i][ j*4 + (3-k) ] = tmp%2;
                    tmp/=2;
                }
            }
        }

        //for(i=0;i<M;i++)
        //{
        //    for(j=0;j<N;j++)cout<<c[i][j];
        //    cout<<endl;
        //}

        vector< pair<int,int> >ans;
        for(k=max(M,N);k>=1;k--)
        {
            bool ok = false;
            for(i=0;i<M-k+1;i++)
                for(j=0;j<N-k+1;j++)
                 {
                    if( cut(i,j,k) ){ // 
                        
                        if( !ok )
                        {
                            ans.push_back( make_pair(k,1) );
                        }
                        else {
                            ans[ ans.size() - 1 ].second ++;
                        }
                        ok=true;
                    }
                 }
        }

        printf("Case #%d: %d\n",ca,ans.size());
        for(i=0;i<ans.size();i++)
        {
            cout<<ans[i].first<<" "<<ans[i].second<<endl;
        }
        
    }
}

