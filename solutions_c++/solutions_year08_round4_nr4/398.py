#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
#define MAXV 1000000

int main(){
	int t,ret=0,tmp,k;
	string s,ts;

	vector <int> vi;
	cin>>t;
	//scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		cin>>k>>s;
		ts=s;
		ret=MAXV;
		vi.clear();
		for(int i=0;i<k;i++)vi.push_back(i);
		do{
			for(int i=0;i<s.size();i+=k){
				for(int j=0;j<k;j++)
					ts[i+j]=s[i+vi[j]];
			}
			//cout<<ts<<endl;
			tmp=1;
			for(int i=1;i<s.size();i++)
			if(ts[i]!=ts[i-1])tmp++;
			if(tmp<ret)ret=tmp;
		}while(next_permutation(vi.begin(),vi.end()));
		//printf("Case #%d: %d\n",tc,res);
		cout<<"Case #"<<tc<<": "<<ret<<endl;
	}
	return 0;
}


