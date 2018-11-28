#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <cstring>
using namespace std;

int ppl[100];
int n,l,h;

int harmoney()
{
	int res=-1;
	for(int i=l;i<=h;i++){
		bool f=true;
		for(int j=0;j<n;j++){
			if(i%ppl[j]!=0 && ppl[j]%i!=0){
				f=false;
				break;
			}
		}
		if(f==true)return i;
	}
	return res;

}

int main()
{
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	//freopen("large.in","r",stdin);
	//freopen("large.out","w",stdout);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		cin>>n>>l>>h;
		for(int i=0;i<n;i++){
			int x;
			cin>>x;
			ppl[i]=x;
		}
		if(harmoney()==-1)cout<<"Case #"<<test<<": NO\n";
		else cout<<"Case #"<<test<<": "<<harmoney()<<endl;;
	}
	return 0;
}
