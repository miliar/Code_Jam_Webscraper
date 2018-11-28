#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int T;
int magic[255][255], op[255][255];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		int n;
		string s;

		memset(magic,0,sizeof(magic));
		memset(op,0,sizeof(op));

		cin >> n;
		for(int i=0;i<n;i++){
			cin >> s;
			magic[s[1]][s[0]] = magic[s[0]][s[1]] = s[2];
		}
		cin >> n;
		for(int i=0;i<n;i++){
			cin >> s;
			op[s[1]][s[0]] = op[s[0]][s[1]] = 1;
		}
		string ans;
		cin >> n >> s;
		for(int i=0;i<n;i++){
			ans = ans + s[i];
			while(1){
				if(ans.length() > 1 && magic[ ans[ans.length() - 2] ] [ ans[ans.length() - 1] ] != 0){
					ans[ans.length() - 2] = magic[ ans[ans.length() - 2] ] [ ans[ans.length() - 1] ];
					ans.resize(ans.length()-1);
					continue;
				}
				for(int j=0;j<ans.length() - 1;j++) if(op[ ans[j] ][ ans[ans.length() - 1] ]){
					ans = "";
					break;
				}
				break;							
			}
		}
		
		printf("Case #%d: ",_);
		cout << "[";
		for(int i=0;i<(int)ans.length()-1;i++) cout << ans[i] << ", ";
		if(ans.length()) cout << ans[ans.length()-1];
		cout << "]\n";
	}
	return 0;
}
