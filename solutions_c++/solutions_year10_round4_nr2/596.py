#include <iostream>
using namespace std;
typedef long long LL;
const int MAXN = 5000;
const LL INF = 500000010LL;
int M[MAXN];
LL price[MAXN];
LL dp[MAXN][20];
int mark[MAXN];
int main()
{
    //freopen("test.in","r",stdin);
   // freopen("B-small-attempt2.in","r",stdin);
 //   freopen("B-small-attempt2.out","w",stdout);
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
    int T;cin>>T;


    for(int tc=1;tc<=T;tc++) {
        memset(mark,0,sizeof(mark));
        for(int i=0;i<MAXN;i++) for(int j=0;j<20;j++) dp[i][j]=INF;
        int P;
        cin>>P;
        int shift = (1<<P)-1;
        for(int i=1;i<=(1<<P);i++) {
            cin>>M[shift+i];
            M[shift+i]=P-M[shift+i];
        }

        for(int i=P-1;i>=0;i--) {
            int v;
            for(int j=1;j<=(1<<i);j++) {
                cin>>price[(1<<i)-1+j];
            }
        }
        for(int i=shift+1;i<shift+1+(1<<P);i+=2) {
            int parent = i/2;
            dp[parent][max(M[i],M[i+1])] = 0;
            //cout<<parent<<" "<<max(M[i],M[i+1])<<endl;
        }

        for(int level = P-1;level>=1;level--) {
            int start = (1<<level)-1;
            for(int j=1;j<=(1<<level);j+=2) {
                for(int p1=0;p1<=P;p1++) {
                    for(int p2=0;p2<=P;p2++) {
                        int node = start+j;

//                        if(p1+p2>P) continue;

                        if(dp[node][p1]<INF&&dp[node+1][p2]<INF) {
                            LL cost = dp[node][p1]+dp[node+1][p2];
                            //both pays
                            if(p1>0&&p2>0) {
                                LL ncost = price[node]+price[node+1]+cost;
                                int parent = node/2;

                                LL &ret = dp[parent][max(p1-1,p2-1)];
                                ret = min(ret,ncost);
                            }
                            if(p1>0) {
                                LL ncost = price[node]+cost;
                                int parent = node/2;
                                LL &ret = dp[parent][max(p1-1,p2)];
                                ret = min(ret,ncost);
                            }
                            if(p2>0) {
                                LL ncost = price[node+1]+cost;
                                int parent = node/2;

                                LL &ret = dp[parent][max(p1,p2-1)];

                                ret = min(ret,ncost);

                            }
                            LL ncost = cost;
                            int parent = node/2;
                            LL &ret = dp[parent][max(p1,p2)];
                            ret=min(ret,cost);


                        }
                    }
                }
            }
        }

        LL ret = dp[1][0];
        if(dp[1][1]<INF) {
            //cout<<ret<<endl;
            ret = min(ret,dp[1][1]+price[1]);
        }


        cout<<"Case #"<<tc<<": "<<ret<<endl;


    }
    return 0;
}
