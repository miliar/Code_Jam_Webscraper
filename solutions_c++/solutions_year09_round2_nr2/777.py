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
#include<utility>
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
    while(t--)
    {
	cn++;
	string n;
	cin>>n;
	reverse(all(n));
	n=n+"0";
	vector<int> v;	
	for(int i=0;i<sz(n);i++) v.push_back(n[i]-'0');
	reverse(all(v));
	next_permutation(all(v));
	while(sz(v)>=0 && v[0]==0) v.erase(v.begin());
	cout<<"Case #"<<cn<<": ";
	for(int i=0;i<sz(v);i++) cout<<v[i];
	cout<<endl;
//	cout<<res<<endl;

    }
}
