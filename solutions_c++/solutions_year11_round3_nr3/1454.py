#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

FILE *fin = freopen("C-small-attempt3.in","r",stdin);
FILE *fout = freopen("probB1.out","w",stdout);


int gcd(int a,int b) {
    int r;
    while(b) {
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}

int main() {

    int T;
    cin>>T;
    for(int t=0;t<T;t++) {
        int N,L,H;
        cin>>N>>L>>H;
        int i;
        vector<int> v;
        for(i=0;i<N;i++) {
            int x;
            cin>>x;
            v.push_back(x);
        }
        make_heap(v.begin(),v.end());
        sort_heap(v.begin(),v.end());

        int h=0;

        cout<<"Case #"<<(t+1)<<": ";
        for(i=L;i<=H;i++) {
            int ok=1;
            for(int j=0;j<N && ok;j++)
                if(v[j]%i!=0 && i%v[j]!=0)
                    ok=0;
            if(ok) {
                cout<<i<<"\n";
                h=1;
                break;
            }
        }
        if(!h)
            cout<<"NO"<<"\n";
    }
    return 0;
}
