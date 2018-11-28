#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>

using namespace std;

char Cs[1000];
int Ds[30][30];
char seen[30];
char buf[400];
vector<char> ret;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	gets(buf);
	int T,C,D,N;
	string s;
	sscanf(buf,"%d",&T);
	for(int t=1; t<=T; t++){
		memset(seen,0,sizeof(seen));
		memset(Cs,0,sizeof(Cs));
		memset(Ds,0,sizeof(Ds));
		ret.clear();
		gets(buf);
		stringstream ss(*new string(buf));
		ss>>C;
		for(int i=0; i<C; i++) {
			ss>>s;
			if(s[0]>s[1]) swap(s[0],s[1]);
			Cs[(s[0]-'A')*26 + s[1]-'A']=s[2];
		}
		ss>>D;
		for(int i=0; i<D; i++) {
			ss>>s;
			if(s[0]>s[1]) swap(s[0],s[1]);
			Ds[s[0]-'A'][s[1]-'A']=1;
			Ds[s[1]-'A'][s[0]-'A']=1;
		}
		ss>>N;
		ss>>s;
		ret.clear();
		ret.pb(s[0]);
		seen[s[0]-'A']++;
		int n;
		char c;
		for(int i=1; i<N; i++){
			ret.pb(s[i]);
			n = ret.size();
			c = 0;
			if(n>1)	c = Cs[(min(ret[n-1],ret[n-2])-'A')*26+(max(ret[n-1],ret[n-2])-'A')];
			if(c!=0){
				ret.pop_back();
				seen[ret.back()-'A']--;
				ret.back()=c;
				seen[c-'A']++;
			} else {
				for(int j=0; j<26; j++){
					if(Ds[s[i]-'A'][j]&&seen[j]){
						ret.clear();
						memset(seen,0,sizeof(seen));
						break;
					}
				}
				if(ret.size()){
					seen[s[i]-'A']++;
				}
			}
		}
		printf("Case #%d: [",t);
		for(int i=0; i<ret.size(); i++){
			printf("%c", ret[i]);
			if(i<ret.size()-1) printf(", ");
		}
		printf("]\n");
	}
	//system("pause");
	return 0;
}
