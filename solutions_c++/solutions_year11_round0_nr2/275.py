#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		bool mat[128][128]={};
		char trans[128][128]={};
		int C;cin>>C;
		for(int i=0; i<C; ++i) {
			char a,b,c;cin>>a>>b>>c;
			int x=a,y=b;
			trans[x][y]=trans[y][x]=c;
		}
		int D;cin>>D;
		for(int i=0; i<D; ++i) {
			char a,b;cin>>a>>b;
			int x=a,y=b;
			mat[x][y]=mat[y][x]=1;
		}
		int N;cin>>N;
		string s;cin>>s;
		vector<int> v;
		for(int i=0; i<N; ++i) {
			int x = s[i];
			if (!v.empty() && trans[x][v.back()])
				v.back() = trans[x][v.back()];
			else {
				bool cc=0;
				for(size_t j=0; j<v.size(); ++j)
					if (mat[v[j]][x]) v.clear(),cc=1;
				if (!cc) v.push_back(x);
			}
		}
		cout<<"Case #"<<a<<": [";
		for(size_t j=0; j<v.size(); ++j) {
			if (j>0) cout<<", ";
			cout<<(char)v[j];
		}
		cout<<"]\n";
	}
}
