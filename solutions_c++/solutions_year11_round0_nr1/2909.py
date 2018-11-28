#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
struct node{
	int tag;
	int p;	
	node(int _tag = 0, int _p = 0): tag(_tag), p(_p){}
}st[105];
int n;
int n_case = 0;
void run(int tag, int&d1, int &d2, int l){
	if(tag == 0) {d2 += l; d1 = 0;}
	if(tag == 1) {d1 += l; d2 = 0;}
}
int find(int cnt, int tag){
	for(int i = cnt-1; i >= 0; i--){
		if(st[i].tag == tag) return i;
	}	
	return -1;
}
void solve0(){
	int d1 = 0, d2 = 0;
	int res = 0,pre;
	for(int i = 0; i < n; i++){
		int k = find(i,st[i].tag);
		int l;
		if(k == -1){
			l = abs(st[i].p-1)+1;
		} else {
			l = abs(st[i].p - st[k].p)+1;
		}
		int tmp;
		if(st[i].tag == 0) res += max(1, l-d1),tmp = max(1, l-d1);
		else res += max(1, l-d2), tmp = max(1, l-d2);
		printf("tag = %d d1 = %d d2 = %d l = %d tmp = %d\n", st[i].tag, d1, d2, l, tmp);
		run(st[i].tag, d1, d2, l);
		//printf(" i = %d k = %d l = %d d1 = %d d2 = %d time = %d\n", i ,k , l, d1, d2, res - pre);
	}
	for(int i = 0; i < n; i++){
		printf("%c %d\n", st[i].tag == 0?'O':'B', st[i].p);
	}
	printf("Case #%d: %d\n", ++n_case, res);
}
void find_p(int begin,int &p1,int &p2){
	p1 = -1, p2 = -1;
	for(int i = begin; i < n; i++){
		if(st[i].tag == 0){
			p1 = st[i].p; break;
		}
	}
	for(int i = begin; i< n; i++){
		if(st[i].tag == 1){
			p2 = st[i].p;break;	
		}	
	}
}
void solve(){
	int cnt = 0;
	int pos1 = 1, pos2 = 1;
	int t = 0, pre;
	for(;cnt < n;t++){
		pre = t;
		//printf("t = %d %d %d cnt = %d\n", t, pos1, pos2, cnt);
		int nxt1,nxt2;
		find_p(cnt,nxt1,nxt2);
		int now_tag = st[cnt].tag;
		int now_pos = st[cnt].p;
		if(now_tag == 0){
			if(now_pos == pos1){
				cnt++;
			}else if(now_pos > pos1){
				pos1++;
			}else if(now_pos < pos1){
				pos1--;
			}
			if(nxt2 != -1){
				if(nxt2 > pos2){
					pos2++;
				} 
				if(nxt2 < pos2){
					pos2--;
				}
			}
		} else {
			if(now_pos == pos2){
				cnt++;
			}else if(now_pos > pos2){
				pos2++;
			}else if(now_pos < pos2){
				pos2--;
			}
			if(nxt1 != -1){
				if(nxt1 > pos1){
					pos1++;
				} 
				if(nxt1 < pos1){
					pos1--;
				}
			}
		}
	}
	printf("Case #%d: %d\n", ++n_case, t);
}
void input(){
	scanf("%d",	&n);
	int p;
	char str[2];
	for(int i = 0; i < n; i++){
		scanf("%s%d", str, &p);
		if(str[0]=='O') st[i] = node(0, p);
		else st[i] = node(1, p);
	}
	/*for(int i = 0; i < n; i++){
		printf("%d %d\n", st[i].tag, st[i].p);
	}*/
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int C;
	scanf("%d", &C);
	for(int i = 1; i <= C; i++){
		input();
		solve();	
	}
}
