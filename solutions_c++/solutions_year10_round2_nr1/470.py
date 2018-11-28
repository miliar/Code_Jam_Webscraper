#include <iostream>
#include <map>
#include <string>
using namespace std;

char c[205];
string s;

int main(){
	int t;
	scanf("%d\n",&t);
	for(int f=1;f<=t;f++){
		map<string,int> mmm;
		int n,m;
		scanf("%d%d\n",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%s\n",c);
			int len = strlen(c);
			for(int j=1;j<=len;j++){
				if(c[j] == '/' || c[j] =='\0'){
					c[j] = '\0';
					mmm[string(c)] = 1;
					c[j] = '/';
				}
			}
		}
		int cnt= 0;
		for(int i =0;i<m;i++){
			scanf("%s\n",c);
			int len = strlen(c);
			for(int j=1;j<=len ;j++){
				if(c[j] == '/' || c[j] =='\0'){
					c[j] = '\0';
					s = string(c);
					if(mmm[s] !=1) {cnt++;
						//cout << s << endl;
						}
					mmm[s] = 1;
					c[j] = '/';
				}
			}
		}

		printf("Case #%d: %d\n",f,cnt);
	}
	return 0;
}
