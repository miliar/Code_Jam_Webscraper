#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

int mat[256][256];
int mat2[256][256];

void print(vector<char> &list) {
	cout<<"[";
	for (int i=0;i<list.size();i++) {
		if (i!=0) cout<<", ";
		cout<<list[i];
	}
	cout<<"]";
}

int main(){
	int casos,cc,c,d,n;
	string tmp;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		memset(mat,0,sizeof(mat));
		memset(mat2,0,sizeof(mat2));
		cin>>c;
		for (int i=0;i<c;i++) {
			cin>>tmp;
			mat[tmp[0]][tmp[1]]=tmp[2];
			mat[tmp[1]][tmp[0]]=tmp[2];
		}
		cin>>d;
		for (int i=0;i<d;i++) {
			cin>>tmp;
			mat2[tmp[0]][tmp[1]]=-1;
			mat2[tmp[1]][tmp[0]]=-1;
		}
		cin>>n;
		char elem;
		vector<char> list;
		for (int i=0;i<n;i++) {
			cin>>elem;
			int last=(int)list.size()-1;
			if (!list.empty() && mat[list[last]][elem]!=0) {
				list[last]=mat[list[last]][elem];
			} else {
				bool cleared=false;
				for (int j=0;j<=last;j++) if (mat2[list[j]][elem]==-1){
					list.clear();
					cleared=true;
					break;
				}
				if (!cleared) list.push_back(elem);
			}
		}
		
		cout<<"Case #"<<cc+1<<": ";
		print(list);
		cout<<endl;
	}
	return 0;
}
