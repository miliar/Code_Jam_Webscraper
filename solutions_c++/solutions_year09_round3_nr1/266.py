#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
int main(){

	int nt;
	cin>>nt;
	for(int g=1;g<=nt;g++){
		string str;
		cin>>str;
		map<char,int> ma;
		vi v;
		v.pb(1);int val=0;
		ma[str[0]]=1;int maxVal=1;
		for(int i=1;i<sz(str);i++){
			if(ma.find(str[i])==ma.end()){
				ma[str[i]] = val; 
				v.pb(val);
				val++;
				if(val==1)
					val=2;
			}
			else{
				v.pb(ma[str[i]]);
			}
		}
		for(int i=0;i<sz(v);i++)
			if(maxVal<v[i])
				maxVal = v[i];
		maxVal+=1;
		long long ans =0;
		cout<<"Case #"<<g<<": ";
		for(int i=0;i<sz(v);i++)
			ans=ans*maxVal+v[i];
		cout<<ans<<endl;
	}
return EXIT_SUCCESS;

}
