#include <iostream>
#include <cmath>

using namespace std;
int n;

int cur[2];


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,ti;
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        cin>>n;
        cur[0]=1;
        cur[1]=1;
        int dest;
        char c;
        int ptur=-1;
        int ctur;
        int res=0;
        int pres=0;
        int t1;

        for(int i=0;i<n;i++)
        {
            cin>>c>>dest;
            if(c=='O') ctur=0;
            else if(c=='B') ctur=1;

            t1= abs(cur[ctur]-dest);
            if(ptur==ctur);
            else
            {
                 t1=t1-pres;
                 if(t1<0) t1=0;
                 pres=0;
            }
            t1++;
            //cout<<"::"<<t1<<"xx";
            res+=t1;
            pres+=t1;
            cur[ctur]=dest;
            ptur=ctur;
        }
        cout<<"Case #"<<ti<<": "<<res<<endl;
    }
    return 0;
}




