#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int l[50];
char str[50];

void change(int f, int t)
{
	int temp = l[t];
	int i;
	for(i=t; i>f; i--) {
		l[i] = l[i-1];
	}
	l[f] = temp;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen("input.txt", "r", stdin);

	int i, j, cas, now, n, pos, sol;
	scanf("%d\n",&cas);

	for(now = 1; now <= cas; now++) {
		printf("Case #%d: ",now);
		sol = 0;

		scanf("%d\n",&n);
		
		for(i=0; i<n; i++) {
			pos = -1;
			cin.getline(str, 50);
			for(j=0; j<n; j++) {
				if(str[j] == '1') pos = j;
			}
			l[i] = pos;
		}
		
		for(i=0; i<n; i++) {
			if(l[i] > i) {
				for(j=i+1; j<n; j++) {
					if(l[j] <= i) {
						change(i, j);
						sol += (j-i);
						break;
					}
				}
			}
		}

		printf("%d\n",sol);
	}

	return 0;
}