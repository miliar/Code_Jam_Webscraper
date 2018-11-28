//
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define ita(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define itd(i_,f_,t_) for(int i_=f_;i_>t_;--i_)

int cs[1000];
int css[1000];
int main()
{
    int T;
    cin>>T;
    ita(t,0,T)
    {
        int L,N,C;
        long long h;
        cin>>L>>h>>N>>C;
        int ac = 0;
        ita(i,0,C)
        {
            int a;
            cin>>a;
            cs[i]=a;
            ac+=a*2;
        }

        int of = h % ac;

        int aa = 0;
        int n0=0;
        ita(i,0,C)
        {
            aa+=cs[i]*2;
            if (aa>of)
            {
                aa = aa - of;
                n0=i+1;
                break;
            }
        }

        aa /= 2;
        long long n = N - (h / ac)*C - n0;
        copy(cs,cs+C,css);
        
        vector<pair<long long,int>> vs;
        
        int l = L;
        int ta=0;
        long long dif = 0;
        if (n>0)
        {
            int n1 = (int)n/C;
            ita(i,0,C)
            {
                vs.push_back(pair<long long,int>(cs[i],n1));
                
            }

            int n2 = (int)n % C;
            int la = (min)(C-n0,n2);
            ita(i,0,la)
            {
                vs.push_back(pair<long long,int>(cs[i+n0],1));
            }

            ita(i,0,n2-la)
            {
                vs.push_back(pair<long long,int>(cs[i],1));
            }

            sort(vs.begin(),vs.end());

            for(int i = vs.size()-1; l>0 && i>=0;--i)
            {
                if (vs[i].first<=aa && !ta)
                {
                    ta =1; --l;
                    dif += aa;
                }

                int m = (min)(l,vs[i].second);

                dif += (long long)vs[i].first * m;
                l-=m;
            }

        }
        if (n==0)
            dif=aa;

        long long r = long long(N/C) * ac;
        long long rc = N % C;
        ita(i,0,rc)
        {
            r += cs[i]*2;
        }
        r -= dif;    

        cout<<"Case #"<<(t+1)<<": "<<r<<endl;
    }
    return 0;
}