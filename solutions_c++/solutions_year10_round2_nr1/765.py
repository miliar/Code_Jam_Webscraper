#include<iostream>
#include<map>
#include<cstdio>
#include<string.h>
#include<string>

using namespace std;

int T, N, M, id, cas;
struct node{
	string st;
	int ft;
}dir[100000];

void input()
{
	int i, j, k, l;
	char s[200];
	string ss;
//	tr.clear();
	scanf("%d%d", &N, &M);
	
	id = 0;
	dir[0].ft = 0;
	dir[0].st = "/";
	for (i=0;i<N;i++){
		memset(s, 0, sizeof(s));
		scanf("%s", s);
		s[strlen(s)] = '/';
		ss = "";
		k = 0;
		for (j=1;s[j];j++)
			if (s[j] == '/'){
				
				for (l=1;l<=id;l++)
					if (dir[l].st == ss && dir[l].ft == k){
						k = l;
						ss = "";
						break;
					}
				if (l > id){
					id++;
					dir[id].st = ss;
					dir[id].ft = k;
				//	printf("id = %d, st = %s, ft = %d\n", id, dir[id].st.c_str(), dir[id].ft);
					k = id;
					ss = "";
				}
			}else ss+=s[j];
	}
}

int work()
{
	int i, j, k, l, ret = 0;
	char s[200];
	string ss;
	
	for (i=0; i<M; i++){
		memset(s, 0, sizeof(s));
		scanf("%s", s);
		s[strlen(s)] = '/';
		ss = "";
		k = 0;
		for (j=1;s[j];j++)
			if (s[j] == '/'){
				
				for (l=1;l<=id;l++)
					if (dir[l].ft == k && dir[l].st == ss){
						k = l; 
						ss = "";
						break;
				}
				
				if (l > id) {
					id++;
					dir[id].st = ss;
					dir[id].ft = k;
			//		printf("insert: id = %d, st = %s, ft = %d\n", id, dir[id].st.c_str(), dir[id].ft);
					k = id;
					ret ++;
					ss = "";
				}
			}else ss+=s[j];
	}
	return ret;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int res;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++){
		input();
		res = work();
		printf("Case #%d: %d\n", cas, res);
	}
}
