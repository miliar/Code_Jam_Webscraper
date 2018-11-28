#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


void solve(istream& in, ostream& out)
{
    int n;
    vector<int> d(n+1), l(n+1), max(n+1,-1);
    in>>n;
    for(int i=0;i<n; i++)
    {
        in>>d[i]>>l[i];
    }
    in>>d[n]; l[n]=1000000001;

    max[0]=d[0];
    for(int i=1; i<=n; i++) {
        int mx=0;
        for(int j=i-1; j>=0; j--) { //j-rõl i-re
            //if(d[i]-d[j]>l[j]) continue;
            if(d[j]+max[j]>=d[i]) { mx=d[i]-d[j];}

        }
        max[i]=(mx<l[i] ? mx : l[i]);
    }

    /*for(int i=0; i<=n; i++) {
        cout<<max[i]<<endl;
    }*/

    if(max[n]>0) out<<"YES";
    else out<<"NO";
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("swing.out");
    int cases;
    in>>cases;
    for(int i=0;i<cases;i++)
    {
        out<<"Case #"<<(i+1)<<": ";
        solve(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
