#include <iostream>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

class SavingTheUniverse
{
public:
	SavingTheUniverse()
	{
		cin>>test;
		for (int testcase=0;testcase<test;testcase++){
			cin>>n;
			getchar();
			m.clear();
			for (int i=0;i<n;i++){
				string name;
				getline(cin,name);
				m[name]=i+1;
			}
			cin>>q;
			getchar();
			memset(d,0,sizeof(d));
			int cnt=0,res=0;
			for (int i=0;i<q;i++){
				string strq;
				getline(cin,strq);
				if (d[m[strq]]==0){
					cnt++;
				}
				if (cnt==n){
					res++;
					memset(d,0,sizeof(d));
					cnt=1;
				}
				d[m[strq]]=1;
			}
			cout<<"Case #"<<testcase+1<<": "<<res<<endl;
		}
	}
private:
	int n,q,test;
	map<string,int> m;
	int d[101];
};

int main()
{
	SavingTheUniverse a;
	return 0;
}