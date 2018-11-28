#include<cstdio>
#include<cstring>
#include<stack>
#include<vector>

using namespace std;
int n;
char merge[30][30];
vector<char> del[30];
int inside[30];
int tc,c,d;
char ch1,ch2,ch3;

int main(){
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		stack<char> stak;
		char ch;
		scanf("%d",&c);
		memset(del,false,sizeof(bool));
		memset(inside,0,sizeof(inside));
		for (int i = 0; i < 30; i++) {
			del[i].clear();
			for (int j = 0; j < 30; j++) {
				merge[i][j] = '\0';
			}
		}
		for (int i = 0; i < c; i++) {
			scanf(" %c%c%c",&ch1,&ch2,&ch3);
			merge[ch1-'A'][ch2-'A'] = ch3;
			merge[ch2-'A'][ch1-'A'] = ch3;
		}
		scanf("%d",&d);
		for (int i = 0; i < d; i++) {
			scanf(" %c%c",&ch1,&ch2);
			del[ch1-'A'].push_back(ch2);
			del[ch2-'A'].push_back(ch1);
		}
		
		scanf("%d",&n);  scanf("%c",&ch);
		for (int i = 0; i < n; i++) {
			scanf("%c",&ch1);
			stak.push(ch1);
			inside[ch1-'A']++;
			while (stak.size()>= 2) {
				char ch2 = stak.top();
				inside[ch2-'A']--;
				stak.pop();
				char ch1 = stak.top();

				if (merge[ch1-'A'][ch2-'A'] != '\0') {
					inside[ch1-'A']--;
					stak.pop();
					stak.push(merge[ch1-'A'][ch2-'A']);
					inside[merge[ch1-'A'][ch2-'A']-'A']++;
				} else  {
					stak.push(ch2);
					inside[ch2-'A']++;				
					bool tr = false;
					for (int j = 0; j < del[ch2-'A'].size(); j++) {
						if (inside[del[ch2-'A'][j]-'A'] != 0) tr = true;
					}

					if (tr) {
						while (!stak.empty()) {
							inside[stak.top()-'A']--;
							stak.pop();
						}
					} else  {
						break;
					}
				}
			}

		}
		scanf("\n");
		vector<char> res;
		while(!stak.empty()) {
			res.push_back(stak.top());
			stak.pop();
		}
		printf("Case #%d: [",ti);
		for (int i = res.size()-1; i >= 0; i--) {
			printf("%c",res[i]);
			if (i != 0) printf(", ");
		}
		printf("]\n");
	}
}