#include <iostream>
#include <string>
#include <utility>
using namespace std;
int n,m;
string w[10000];
struct word{
	string s;
	int score;
	int ref;
	bool flag;
};
bool operator<(const word& w1,const word& w2){
	if (w1.s!=w2.s)
		return w1.s<w2.s;
	return w1.flag && !w2.flag;
}
bool comp(const word& w1,const word& w2){
	if (w1.score!=w2.score)
		return w1.score>w2.score;
	return w1.ref<w2.ref;
}
word W[10000];
int main(){
	int tnum,tcou=0;cin>>tnum;
	while (tnum--){
		cin>>n>>m;
		for (int i=0;i<n;++i)
			cin>>w[i];
		cout<<"Case #"<<++tcou<<":";
		while (m--){
			string l;cin>>l;
			for (int i=0;i<n;++i){
				W[i].s=w[i];
				W[i].score=0;
				W[i].ref=i;
				W[i].flag=0;
			}
			for (int i=l.size()-1;i>=0;--i){
				for (int j=0;j<n;++j){
					W[j].flag=false;
					for (int k=0;k<W[j].s.size();++k)
						if (W[j].s[k]==l[i]){
							W[j].s[k]='-';
							W[j].flag=true;
						}
				}
				sort(W,W+n);
				for (int j=0;j<n;){
					int k;
					for (k=j;k<n && W[k].s==W[j].s;++k)
						if (W[j].flag && !W[k].flag){
							++W[k].score;
						}
					j=k;
				}
			}
			sort(W,W+n,comp);
			cout<<" "<<w[W[0].ref];
		}
		cout<<endl;
	}
	return 0;
}
