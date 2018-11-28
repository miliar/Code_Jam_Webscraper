#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
struct DIC
{
	string wo;
}dic[5010];
struct ST
{
	string w;
	int nn;
	int p;
};
int cmp (const DIC a, const DIC b)
{
	return a.wo.compare(b.wo) > 0;
}

char word[10000];
int len, l, d, n;
queue<ST>que;
bool check(ST a)
{
	int low = 0;
	int hig = d;
	int mid;
	while (low <= hig){
		mid = (low + hig) / 2;
		int idx = a.w.compare(dic[mid].wo);
		if (idx == 0)
			return true;
		else if (idx < 0)
			low = mid + 1;
		else
			hig = mid - 1;
	}
	return false;
}
int BFS()
{
	int cnt = 0, ap;
	int i, j;
	while (!que.empty())
		que.pop();
	ST now, next;
	now.w = "";
	now.nn = 0;
	now.p = 0;
	que.push(now);
	while (!que.empty()){
		now = que.front();
		que.pop();
		if (now.w.size() == l){
			if(check(now))
				cnt ++;
			continue;
		}
		if (word[now.p] == '('){
			for (j = now.p + 1; word[j] && word[j] != ')'; j ++);
			if (!word[j])
				j --;
			ap = j + 1;
			for (j = now.p + 1; word[j] && word[j] != ')'; j ++){
				for (int k = 0; k < d; k ++){
					if (word[j] == dic[k].wo[now.nn]){
						if(now.nn > 0){
							if (now.w[now.nn - 1] != dic[k].wo[now.nn - 1])
								continue;
						}
						next = now;
						next.w += word[j];
						next.p = ap;
						next.nn ++;
						que.push(next); 
						break;
					}
				}
			}
		}
		else{
			for (int k = 0; k < d; k ++){
				if (word[now.p] == dic[k].wo[now.nn]){
					next = now;
					next.w += word[now.p];
					next.p = now.p + 1;
					next.nn ++;
					que.push(next);
					break;
				}
			}
		}
	}
	return cnt;
}
int main ()
{
	
	int cas, ans;
	char ch[20];
	int i;
	freopen ("A-small-attempt1.in", "r", stdin);
	freopen ("A-small-attempt1.out", "w", stdout);
	scanf ("%d %d %d", &l, &d, &n);
	cas = 1;
	for (i = 0; i < d; i ++){
		scanf ("%s", ch);
		dic[i].wo = ch;
	}
	sort(dic, dic + d, cmp);
	for (i = 0; i < n; i ++){
		scanf ("%s", word);
		len = strlen(word);
		ans = BFS();
		printf ("Case #%d: %d\n", cas ++, ans);
	}
	return 0;
}