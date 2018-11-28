

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{

	int n;
	cin>>n;
	for(int i=1;i<=n;++i){
		cout<<"Case #"<<i<<": ";
		string xstr;
		int k;
		cin>>k>>xstr;
		const string org(xstr);
		vector<int> perm(k);
		for(int i=0;i<k;++i)
			perm[i] = i;
		unsigned int ans = -1;
		int _x = 0;
		do{
			++_x;
			const int part = org.size()/k;
			string now;
			for(int i=0;i<part;++i){
				for(int j=0;j<k;++j)
					now += org[ i*k + perm[j] ];
			}
			unsigned int cc = distance(now.begin(),unique(now.begin(),now.end()));
			if(ans>cc)
				ans = cc;
		}while(next_permutation(perm.begin(),perm.end()));
		cout<<ans<<endl;
	}
}
