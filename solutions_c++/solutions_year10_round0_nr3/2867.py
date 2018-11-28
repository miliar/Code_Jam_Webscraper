#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
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
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;
vector<int> v,temp;

int main()
{
    int t;
    long long r,k,n;
    cin>>t;
    int cn=0;
    while(t--)
    {
	cn++;
	printf("Case #%d: ",cn);
	cin>>r>>k>>n;
	v.resize(n);
	for(int i=0;i<n;i++) cin>>v[i];
	lli rep=0, sum=0;
	int ind=0; bool done=false;
	map<int,lli> mp;
	long long spsum=0;
	for(int i=0;i<v.size();i++) spsum+=v[i];
	if(spsum<=k)
	{
	    done=true;
	    cout<<r*spsum<<endl;
	}

	while(true && !done)
	{
	    
	    lli cursum=0;
	    while(cursum+v[ind]<=k)
	    {
		cursum+=v[ind];
		ind++;
		ind%=n;
	    }

	    temp.clear();
	    while(temp.size()<v.size()) 
	    {
		temp.push_back(v[ind++]);
		ind%=n;

	    }

	    rep++; sum+=cursum;
	    mp[rep]=sum;
	    if(rep==r)
	    {
		cout<<sum<<endl;
		done=true;
		break;
	    }
	    if(temp==v)
	    {
		break;
	    }
	  //  cerr<<"     "<<rep<<"   "<<sum<<"    "<<cursum<<endl;
	    


	}
	if(done) continue;
	long long int ans=0;
	ans=(r/rep)*sum+mp[r%rep];
	cout<<ans<<endl;




    }


}
