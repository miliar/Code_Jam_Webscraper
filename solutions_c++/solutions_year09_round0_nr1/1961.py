#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
char buff[10000];
string tab[5001];
inline bool cmp (const string &a, const string &b) {
	int i = 0;
	while(a[i]==b[i]&&i<a.size())++i;
	return a[i]<b[i];
}
int main() {
	int L,D,N,m,res;
	bool option,p;
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;++i) {
		scanf("%s",buff);
		tab[i] = string(buff);
	}
	sort(tab,tab+D,cmp);
	for(int x=1;x<=N;++x) {
		res = 0, scanf("%s",buff);
		for(int j=0;j<D;++j) {
			p = true, m = 0, option = false;
			for(int i=0;i<L && p==true;++i) {
				while(buff[m]!=tab[j][i] && buff[m]!=')' && m < strlen(buff)) {
					if(buff[m] == '(') option = true;
					++m;
				}
				if(buff[m]!=tab[j][i]) p = false;
				if(option == true) 
					while(buff[m]!=')') ++m;
				option = false;
				if(buff[m]==')') ++m;
			}
			res += p;
		}
		printf("Case #%d: %d\n", x, res);
	}
	return 0;
}
