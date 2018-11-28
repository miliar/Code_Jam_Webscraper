#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cstring>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

int main()
{
    int t;
    cin>>t;
    int cn=0;
    set<string> ase; string line;
    while(t--)
    {
        ase.clear();
        cn++;
        int n,m;
        cin>>n>>m;

        for(int i=0;i<n;i++)
        {
            cin>>line;
            ase.insert(line);
        }

        int rv=0;
        for(int i=0;i<m;i++)
        {
            cin>>line;
            if(ase.count(line))
            {
                continue;
            }
            bool done=false;
            while(!done)
            {
                if(line.size()==0) break;
                if(ase.count(line))
                    break;

                ase.insert(line);
                rv++;
                int x=line.size(); x--;
                //cout<<"HERE"<<endl;
                while(line[x]!='/')
                {
                    //cout<<line<<endl;
                    line.erase(line.begin()+x);
                    x--;
                }
                line.erase(line.begin()+x);
            }
        }
        printf("Case #%d: %d\n",cn,rv);

    }
    return 0;
}
