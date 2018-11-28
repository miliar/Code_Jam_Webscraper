#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int pos[2], ans[2], con;

int getId(char ch) {
	if (ch == 'O')
	   return 0;
	else
		return 1;	
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, id, cas, iCas, preId, n, x, tmp;
	char ch;
	scanf("%d", &cas);
	for (iCas = 1; iCas <= cas; ++iCas) {
		scanf("%d", &n);
		pos[0] = pos[1] = 1;
		ans[0] = ans[1] = 0;
		con = 0;
		for (i = 1; i <= n; ++i) {
			scanf(" %c%d", &ch, &x);
			id = getId(ch);
			tmp = abs(x - pos[id]);
			if (i == 1 || preId == id) {
			   tmp++;
			   con += tmp;
			   ans[id] += tmp;
            }
			else {
               if (con >= tmp) {
                  con = 1;
		       	  ans[id] = ans[id ^ 1] + 1;
	           }
	           else {
 		          ans[id] += tmp + 1;
                  con = tmp - con + 1;
	           }
			}
			pos[id] = x;
			preId = id;
		}
		printf("Case #%d: %d\n", iCas, max(ans[0], ans[1]));

	}	
	
}