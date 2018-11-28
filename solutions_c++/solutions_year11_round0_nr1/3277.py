#include<iostream>
#include<vector>
#include<cstdio>

#define sz(c) (int)c.size()

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t = 0; t < T; t++)
    {
        int N;
        cin>>N;
        vector<int> val(N,0), bval, oval;
        vector<char> c(N);
        for(int i = 0; i < N; i++)
        {
            cin>>c[i]>>val[i];
            if(c[i] == 'B') bval.push_back(val[i]);
            else oval.push_back(val[i]);
        }
        int ans = 0;
        int i = 0, bi = 0, oi = 0, blue = 1, orange = 1;
        while(i < sz(val))
        {
            bool bmoved = false, omoved = false;
            if(c[i] == 'B' && blue == val[i])
            {
                i++;
                bi++;
                bmoved = true;
            }
            else if(c[i] == 'O' && orange == val[i])
            {
                i++;
                oi++;
                omoved = true;
            }
            if(!omoved && (oi < sz(oval)))
            {
                if(orange < oval[oi])
                    orange++;
                else if(orange > oval[oi])
                    orange--;
            }
            if(!bmoved && (bi < sz(bval)))
            {
                if(blue < bval[bi])
                    blue++;
                else if(blue > bval[bi])
                    blue--;
            }
            ans++;
        }
        cout<<"Case #"<<(t+1)<<": "<<ans<<endl;
    }
}

