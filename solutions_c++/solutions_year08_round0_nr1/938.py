#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;
int visit[101];
int main() {
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	int N, S, Q;
	int cases;
	int i;
	cin>>N;
	for(cases=0;cases<N;++cases) {
		cin>>S;
		string name;
		int id=0;
		map<string,int> dic;
		getline(cin,name);
		for (i=0; i<S; ++i) {
			getline(cin,name);
			dic[name]=id++;
		}
		cin>>Q;
		getline(cin,name);
		int ans=0;
		int count=0;
		int pre=-1;
			memset(visit,0,sizeof(visit));
		for(i=0;i<Q;++i){
		
			getline(cin,name);
			int num = dic[name];
			if(visit[num]==0){
				visit[num]=1;
				++count;
				pre=num;
			}
				if(count==id){
				++ans;
				memset(visit,0,sizeof(visit));
				visit[pre]=1;
				count=1;
			}
		}
		cout<<"Case #"<<cases+1<<": "<<ans<<endl;


	}
	return 0;
}
