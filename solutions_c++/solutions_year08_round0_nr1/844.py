#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int n, test = 1, s, q, i,j;
	int start, index, exit, switches, en, prev;
	cin >> n;
	char a[105][105], b[1005][105];
	while(n--) {
		cin >> s;
		for(i=0;i<s;i++)
			scanf(" %[^\n]", a[i]);
		cin >> q;
		for(i=0;i<q;i++)
			scanf(" %[^\n]", b[i]);
		start = 0;
		switches = 0;
		prev = -1;
		while(1) {
			index = start-1;
			exit = 0;
			for(i=0;i<s;i++) {
				for(j=start;j<q;j++) {
					if(strcmp(a[i],b[j])==0) {
						if(j>index && i!=prev) {
							index = j;
							en = i;
						}
						break;
					}
				}
				if(j==q && i!=prev) {
					index = j;
					en = i;
				}
			}
			if(exit)
				break;
			prev = en;
			start = index+1;
			if(start>q)
				break;
			switches++;
		}
		cout << "Case #" << (test++) << ": " << switches << endl;
	}
	return 0;
}
