#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

typedef pair<int,int> pii;
char s[110];

int zam[600];
int del[50][2];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int gi=1; gi<=cases; ++gi){
		int c, d, n;
		scanf("%d", &c);
		memset(zam, -1, sizeof(zam));
		for(int i=0; i<c; ++i){
			scanf("%s", s);
			int a = s[0]-'A';
			int b = s[1]-'A';
			int c = s[2]-'A';
			zam[26*a + b] = zam[26*b + a] = c;
		}
		scanf("%d", &d);
		for(int i=0; i<d; ++i){
			scanf("%s", s);
			del[i][0] = s[0]-'A';
			del[i][1] = s[1]-'A';
		}
		
		printf("Case #%d: [", gi);
		vector<int> v;
		scanf("%d", &n);
		scanf("%s", s);
		for(int i=0; i<n; ++i){
			int a = s[i]-'A';
			if(v.empty()){ v.push_back(a); continue; }
			int b = v.back();
			if(zam[26*a+b] != -1){ v.pop_back(); v.push_back(zam[26*a+b]); }
			else v.push_back(a);
			for(int i=0; i+1<v.size(); ++i){
				int c = v[i];
				for(int dl=0; dl<d && !v.empty(); ++dl){
					if(del[dl][0] == v.back() && del[dl][1] == c) v.clear();
					else if(del[dl][1] == v.back() && del[dl][0] == c) v.clear();
				}
			}
		}
		for(int i=0; i<v.size(); ++i){
			if(i > 0) printf(", ");
			printf("%c", (char)(v[i] + 'A'));
		}
		printf("]\n");
	}
	return 0;
}
