#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(){
	int t;
	cin >> t;
	for (int z=1;z<=t;++z){
		int s, q;
		cin >> s;
		string eng[s+1];
		getline(cin,eng[0]);
		for (int i=0;i<s;++i)
			getline(cin,eng[i]);
		cin >> q;
		string que[q+1];
		getline(cin,que[0]);
		for (int i=0;i<q;++i)
			getline(cin,que[i]);
		bool die[s];
		memset(die,false,sizeof(die));
		int done = 0, ans=0, died=0;
		while (done < q){
			for (int i=0;i<s;++i)
				if (que[done] == eng[i] && !die[i]) {
					++died;
					if (died==s) ++ans,memset(die,false,sizeof(die)),died=1;
					die[i] = true;
				}
			++done;
		}
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}
