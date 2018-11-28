#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

struct node{
	bool built;
	string name;
	bool friend operator < (const node &a, const node &b){
		if(a.name == b.name)
			return a.built;
		return a.name < b.name;
	}
};
node mulu[210];
int tc, m, n, ans;

int main() {
	scanf("%d", &tc);
	int i, j;
	int len1, len2, len;
	for(int t=1; t<=tc; t++){
		scanf("%d%d", &n, &m);
		for(i=0; i<n; i++){
			cin >> mulu[i].name;
			mulu[i].built = true;
		}
		for(i=0; i<m; i++){
			cin >> mulu[n+i].name;
			mulu[n+i].built = false;
		}
		sort(mulu, mulu+(m+n));
		/*
		for(i=0; i<m+n; i++){
			cout<<mulu[i].name<<" "<<mulu[i].built<<endl;
		}
		cout<<"------------"<<endl;
		*/
		ans = 0;
		if(!mulu[0].built){
			for(i=mulu[0].name.length()-1; i>=0; i--){
				if(mulu[0].name[i] == '/')
					ans++;
			}
		}
		for(i=1; i<m+n; i++){
			if(mulu[i].built)
				continue;
			if(mulu[i].name == mulu[i-1].name) continue;
			len1 = mulu[i-1].name.length();
			len2 = mulu[i].name.length();
			if(len1 <= len2){
				for(j=0; j<len1; j++){
					if(mulu[i-1].name[j] != mulu[i].name[j]){
						break;
					}
				}
				if(mulu[i].name[j] != '/')
					ans++;
				for( ; j<len2; j++){
					if(mulu[i].name[j] == '/')
						ans++;
				}
			} else {
				for(j=0; j<len2; j++){
					if(mulu[i-1].name[j] != mulu[i].name[j]){
						break;
					}
				}
				if(mulu[i].name[j] != '/')
					ans++;
				for( ; j<len2; j++){
					if(mulu[i].name[j] == '/')
						ans++;
				}
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

