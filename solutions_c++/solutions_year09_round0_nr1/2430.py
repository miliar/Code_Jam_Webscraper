#include <cstdio>
#include <map>
#include <string.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

vector<char> v[20];
int c;

void read(){
	char s[1000];
	gets(s);
	int len = strlen(s);
	int i=0;
	while (i<len){
		if (s[i] == '('){
			int oi = i+1;
			while (s[i] != ')') i++;
			int ei = i-1;
			for (int j=oi; j<=ei; j++)
				v[c].push_back(s[j]);
			c++;
		}else
			v[c++].push_back(s[i]);
		i++;
	}

}

char a[5010][20];
int sol;
int l, d, n;

void run(){
	for (int i=0; i<d; i++){
		bool err = false;
		for (int j=0; j<l; j++){
			bool find = false;
			int size = v[j].size();
			for (int k=0; k<size; k++)
				if (v[j][k] == a[i][j]){
					find = true;
					break;
				}
			if (!find){
				err = true;
				break;
			}
		}
		if (!err) sol++;
	}
}

int main(){
	char s[1000];
	scanf("%d%d%d", &l, &d, &n);
	gets(s);
	for (int i=0; i<d; i++){
		gets(a[i]);
	}
	for (int i=0; i<n; i++){
		for (int j=0; j<20; j++) v[j].clear();
		sol = c = 0;
		read();
		run();
		printf("Case #%d: %d\n", i+1, sol);
	}
	return 0;
}
