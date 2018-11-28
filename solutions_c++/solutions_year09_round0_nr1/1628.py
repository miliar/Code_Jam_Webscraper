#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

#define LL 15
#define DD 5000

char str[DD][LL];
int main()
{
//	freopen("A-small-attempt2.in","r",stdin);
	//freopen("A-small-attempt2.out","w",stdout);

	int L,D,N;
	if (scanf("%d %d %d",&L,&D,&N) == 3){
		for (int i = 0 ;i < D ;i++){
			scanf("%s",str[i]);
		}
		bool left = false;
		char s[3*DD];
		for (int j = 0 ;j < N ;j++){
			scanf("%s",s);
			int re = 0;
			for (int i = 0 ;i < D ;i++){
				int len = strlen(str[i]);
				int len2 = strlen(s);
				int start = 0;
				int l = 0;
				for (l = 0 ;l < len && start<len2 ;l++){
					if (s[start] != str[i][l]){
						if (s[start]!='('){
							break;
						}else{
							start++;
							int have = false;
							while(s[start] != ')' && s[start] != 0){
								if (s[start] == str[i][l]){
									have = true;
								}
								start++;
							}
							if (!have){
								break;
							}
						}
					}
					start++;
				}
				if (l==len && start ==len2){
					re++;
				}
			}
			cout << "Case #" << j+1 <<": " << re << endl;
		}
	}
	
}
