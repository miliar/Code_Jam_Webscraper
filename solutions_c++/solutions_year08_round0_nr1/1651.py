#include <vector>
#include <iostream>
#include<string>
#include <stdio.h>

using namespace std;

int n,s,q;

int main() {
		freopen("A.in","r",stdin);
		freopen("A.out","w",stdout);
		scanf("%i", &n);
		for (int t = 0; t<n; t++) {
			scanf("%i\n", &s);
			vector <string> eng;
			for (int i = 0; i<s; i++) {
				string st;
				char ss[100];
				st = gets(ss);
				eng.push_back(st);
			}
			vector <int> last(s);
			for (int i = 0; i<s; i++) 
				last[i] = 0;
			scanf("%i\n", &q);
			for (int i = 0; i<q; i++) {
				string st;
				char ss[100];
				st = gets(ss);
				vector <int> dp;
				for (int j = 0; j<s; j++) {
					if (st == eng[j])
						dp.push_back(-1);
					else {
						int temp = 1000000;
						if (last[j]!=-1)
							temp = last[j];
						for (int k = 0; k<s; k++) 
							if (k != j && last[k] != -1) {
								if (last[k]+1<temp)
									temp = last[k]+1;							
							}
						dp.push_back(temp);
					}
				}
				last = dp;
			}
			int res = 1000000;
			for (int i = 0; i<s;  i++) {
				if (last[i] != -1 && last[i]<res)
					res = last[i];
			}
			printf("Case #%i: %i\n", t+1, res);
		}
}