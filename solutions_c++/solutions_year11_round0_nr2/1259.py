#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

struct Node{
	char str[5];
}hc[1000], hd[1000];
char list[100000];
char inp[100000];
int c, d, n;
bool judge(int id){
	int i;
	char a = list[id];
	char b = list[id-1];
	char p, q;
	for(i = c-1; i >= 0; i --){
	//for(i = 0; i < c; i ++){
		p = hc[i].str[0];
		q = hc[i].str[1];
		if( (a == p && b == q) ||  (a == q && b == p) )
		{
			list[id-1] = hc[i].str[2]; return true;
		}
	}
	return false;
}
bool kils(int id){
	int i, j;
	char a = list[id], b;
	char p, q;
	//for(i = id-1; i >= 0; i --){
	for(i = 0; i < id; i ++){
		b = list[i];
		for(j = 0; j < d; j ++){
			p = hd[j].str[0];
			q = hd[j].str[1];
			if( (a == p && b == q) ||  (a == q && b == p) )
			{
				return true;
			}
		}
	}
	return false;
}
void solve(int cas){
	int  i, cnt = 0;
	cin >> c;
	for(i = 0; i < c; i ++)
		cin >> hc[i].str;
		
	cin >> d;
	for(i = 0; i < d; i ++)
		cin>> hd[i].str;
	cin >> n;
	cin >> inp;
	cnt = 0;

	for(i = 0; i < n;i ++){
		if(cnt == 0){
			list[cnt] = inp[i]; cnt ++;
		}else{
			list[cnt] = inp[i];
			if(judge(cnt)){
				continue;
			}
			else if(kils(cnt)){
				cnt = 0; continue;
			}
			cnt ++;
		}
	}
	printf ("Case #%d: [",cas);
	for(i = 0; i < cnt; i ++){
		if(i > 0) printf (", ");
		printf ("%c", list[i]);
	}
	printf ("]\n");

}
int main()
{
	int T, i;
	freopen("B-large.in","r", stdin);
	freopen("B-large.out","w", stdout);
	scanf ("%d", &T);
	for(i = 1; i <= T; i ++){
		solve(i);
	}
	return 0;
}