#include<fstream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<math.h>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

struct MyPair
{
    int x,V;
};

bool func (MyPair lhs,MyPair rhs){ return lhs.x<rhs.x; }

int main()
{
    int I,T,i,n,d,num_vendors;
    cin>>T;
    cout.setf(ios::fixed);
    cout.precision(12);
    vector<MyPair> a;
    vector<MyPair>::iterator k,m,it;
    double result,d1,d2,d3;
    for(I=1;I<=T;I++)
    {
        cin>>n>>d;
        result=0;
        a.resize(n);
        for(i=0;i<n;i++)
        {
            cin>>a[i].x>>a[i].V;
        }
        for(k=a.begin();k<a.end();k++)
        {
            for(m=k;m<a.end();m++)
            {
                num_vendors=0;
                for(it=k;it<=m;it++)
                    num_vendors+=it->V;
                d3=abs(k->x-m->x);
                d2=(num_vendors-1)*d;
                d1=(d2-d3)/2;
                if(d1>result)result=d1;
            }
        }
        cout<<"Case #"<<I<<": "<<result<<endl;
    }
}
