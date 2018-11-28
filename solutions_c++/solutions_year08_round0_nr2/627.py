#include <iostream>
#include <sstream>
#include <string>
#include <set>
using namespace std;
multiset<pair<int,int> > a,b;
int main()
{freopen("d:\\B-large.in.txt","r",stdin);
freopen("d:\\out.txt","w",stdout);
    int i,j,k,n,tt,t,na,nb,ansa,ansb;
    string s;
    char c;
    cin>>n;
    for (tt=1;tt<=n;tt++)
    {
        cin>>t>>na>>nb;
        a.clear();
        b.clear();
        for (i=0;i<na;i++)
        {
            cin>>s;
            istringstream i1(s);
            i1>>j>>c>>k;
            k=k+j*60;
            a.insert(pair<int,int>(k,1));
            cin>>s;
            istringstream is(s);
            is>>j>>c>>k;
            k=k+j*60+t;
            b.insert(pair<int,int>(k,0));
        }
        for (i=0;i<nb;i++)
        {
            cin>>s;
            istringstream i2(s);
            i2>>j>>c>>k;
            k=k+j*60;
            b.insert(pair<int,int>(k,1));
            cin>>s;
            istringstream it(s);
            it>>j>>c>>k;
            k=k+j*60+t;
            a.insert(pair<int,int>(k,0));
        }
        k=0;
        ansa=0;
        multiset<pair<int,int> >::iterator p;
        for (p=a.begin();p!=a.end();p++)
        {
            if (p->second==0)
            {
                k++;
            }
            else
            {
                if (k)
                    k--;
                else
                    ansa++;
            }
        }
        ansb=0;
        k=0;
        for (p=b.begin();p!=b.end();p++)
        {
            if (p->second==0)
            {
                k++;
            }
            else
            {
                if (k)
                    k--;
                else
                    ansb++;
            }
        }
        cout<<"Case #"<<tt<<": "<<ansa<<" "<<ansb<<endl;
    }
    return 0;
}