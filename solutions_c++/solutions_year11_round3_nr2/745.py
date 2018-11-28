#include <iostream>

using namespace std;
typedef long long LL;
const int MAXN = 30000;
LL A[MAXN];
LL T[MAXN];
LL P[MAXN];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    //scanf("%d",&T);
    int Tt;
    cin>>Tt;
    for(int tc=1;tc<=Tt;tc++) {
        LL L,t,N,C;
        cout<<"Case #"<<tc<<": ";
        //scanf("%d %d %d %d",&L,&t,&N,&C);
        cin>>L>>t>>N>>C;
        for(int i = 0; i < C; i++) {
           // scanf("%d",&P[i]);
            cin>>P[i];
        }

        for(int i = 0; i < N; i++) {
            T[i+1]=P[i%C];
        }

        if(L==0) {
            LL sum = 0;
            for(int i = 1; i <= N; i++) {
                sum+=T[i]*2LL;
            }
            cout<<sum<<endl;
        }
        else {
            if(L==1) {
                LL ret = -1;
                for(int i = 0; i <= N-1; i++) {
                    //place L at i
                    LL req = 0;
                    for(int j = 0; j <= N-1; j++) {
                        if(req>=t) {
                            if(j==i) {
                                req+=T[j+1];
                            }
                            else {
                                req+=T[j+1]*2LL;
                            }
                            continue;
                        }
                        if(req+T[j+1]*2LL>=t) {
                            if(j==i) {
                            LL need = (t - req)/2LL;
                            if(req+need*2LL>=t) {
                                req+=need*2LL;
                                req+=T[j+1]-need;
                            }
                            else {
                                need++;
                                req+=need*2LL;
                                req+=T[j+1]-need;

                            }
                            }
                            else {
                                req+=T[j+1]*2LL;
                            }
                            continue;
                        }
                        req+=T[j+1]*2LL;

                    }
                    if(ret==-1)ret=req;
                    else ret = min(ret,req);
                //    cout<<req<<endl;
                }
                cout<<ret<<endl;
            }
            else {
                LL ret = -1;
                for(int i = 0; i <= N-1; i++) {
                    for(int k= i + 1; k <= N -1; k++) {
                                    LL req = 0;
                    for(int j = 0; j <= N-1; j++) {
                        if(req>=t) {
                            if(j==i||j==k) {
                                req+=T[j+1];
                            }
                            else {
                                req+=T[j+1]*2LL;
                            }
                            continue;
                        }
                        if(req+T[j+1]*2LL>=t) {
                            if(j==i||j==k) {
                            LL need = (t - req)/2LL;
                            if(req+need*2LL>=t) {
                                req+=need*2LL;
                                req+=T[j+1]-need;
                            }
                            else {
                                need++;
                                req+=need*2LL;
                                req+=T[j+1]-need;

                            }
                            }
                            else {
                                req+=T[j+1]*2LL;
                            }
                            continue;
                        }
                        req+=T[j+1]*2LL;

                    }
                    if(ret==-1)ret=req;
                    else ret = min(ret,req);

                    }
                }

                cout<<ret<<endl;
            }

        }



    }
    return 0;
}
