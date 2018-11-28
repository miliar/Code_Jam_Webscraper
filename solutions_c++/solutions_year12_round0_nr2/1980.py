#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Node{
    int big[2];
};
int  peoval[110];
Node peos[110];
int main()
{
    freopen("x.in","r",stdin);
    freopen("x.out","w",stdout);

    int T,n,s,p,val;
    cin>>T;
    for(int i = 1;i<= T;i++){
        cin>>n>>s>>p;
        for(int j = 0;j<n;j++){
            cin>>peoval[j];
        }
        for(int j = 0;j<n;j++){
            if(peoval[j] % 3 == 0){
                peos[j].big[0] = peoval[j] / 3;
                peos[j].big[1] = peoval[j] / 3+1;
            }
            else if(peoval[j] % 3 == 1){
                peos[j].big[0] = peoval[j] / 3+1;
                peos[j].big[1] = peoval[j] / 3+1;
            }
            else if(peoval[j] % 3 == 2){
                peos[j].big[0] = peoval[j] / 3+1;
                peos[j].big[1] = peoval[j] / 3+2;
            }
        }
        int ret = 0;
        for(int j = 0;j<n;j++)
        {
            if(peos[j].big[0] >= p)
                ret++;
            else if(peos[j].big[1]>=p && peos[j].big[1]-2 >= 0 && s > 0){
                s--;
                ret++;
            }
        }
        cout<<"Case #"<<i<<": "<<ret<<endl;

    }
  //  cout << "Hello world!" << endl;
    return 0;
}
