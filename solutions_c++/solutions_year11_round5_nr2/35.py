#include <iostream>
#include <vector>
using namespace std;
int num[1000];
int cou;
vector<int> seq[1000];
void add(int v){
	int the_one=-1;
	for (int i=0;i<cou;++i)
		if (seq[i].back()==v-1){
			if (the_one==-1 || seq[the_one].size()>seq[i].size())
				the_one=i;
		}
	if (the_one==-1){
		seq[cou].clear();
		seq[cou++].push_back(v);
	}
	else
		seq[the_one].push_back(v);
}
int main(){
	int tnum,tcou=0;
	cin>>tnum;
	while (tnum--){
		int n;cin>>n;
		for (int i=0;i<n;++i)
			cin>>num[i];
		sort(num,num+n);
		cou=0;
		for (int i=0;i<n;++i)
			add(num[i]);
		int ans=0;
		for (int i=0;i<cou;++i){
			if (ans==0)
				ans=seq[i].size();
			else
				ans=min(ans,(int)seq[i].size());
		}
		cout<<"Case #"<<++tcou<<": "<<ans<<endl;
	}
	return 0;
}
