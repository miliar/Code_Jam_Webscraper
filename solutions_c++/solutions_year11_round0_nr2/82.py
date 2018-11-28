#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
map<string,string> tr;map<string,int> re;
int main()
{
	int i,j,k,n,t;string s;cin>>t;
	for(j=0;j<t;j++){
		tr.clear();re.clear();
		cin>>n;string ret="";
		for(i=0;i<n;i++){
			cin>>s;tr[s.substr(0,2)]=s.substr(2,1);
			reverse(s.begin(),s.end());tr[s.substr(1,2)]=s.substr(0,1);
		}
		cin>>n;
		for(i=0;i<n;i++){
			cin>>s;re[s]=1;reverse(s.begin(),s.end());re[s]=1;
		}
		cin>>n>>s;
		for(i=0;i<n;i++){
			ret+=s[i];int m=ret.size();
			if(m>1){
				if(tr[ret.substr(m-2,2)].size()>0){
					ret=ret.substr(0,m-2)+tr[ret.substr(m-2,2)];
				}
				else{
					int f=0;
					for(k=0;k<m-1;k++){
						string st=ret.substr(k,1);st+=ret.substr(m-1,1);
						//cout<<'a'<<st<<endl;
						if(re[st]>0) f=1;
					}
					if(f>0) ret="";
				}
			}
//			cout<<ret<<endl;
		}
		printf("Case #%d: [",j+1);
		for(i=0;i<ret.size();i++){
			cout<<ret[i];if(i<ret.size()-1) printf(", ");//else printf("]\n");
		}
		printf("]\n");
	}
	return 0;
}
