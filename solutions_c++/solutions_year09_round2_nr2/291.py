#include <iostream>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

string solve()
{
    string a;
    cin>>a;
    a="0000"+a;
    next_permutation(a.begin(),a.end());
    while(a.size()>1 && a[0]=='0') a.erase(a.begin());
    return a;
}

int main()
{
    int t;
    cin>>t;
    fru(i,t) cout<<"Case #"<<i+1<<": "<<solve()<<endl;

#ifdef __WIN32
//    system ("pause");
#endif
return 0;
}
