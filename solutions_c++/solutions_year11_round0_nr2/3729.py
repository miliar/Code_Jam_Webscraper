#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string C,O,R,ans;
int c,o,len,anslen;

void input()
{
	scanf("%d",&c);
	if(c != 0) cin >> C;
	scanf("%d",&o);
	if(o != 0) cin >> O;
	scanf("%d",&len);
	cin >> R;
}
void pro()
{
	ans = R[0];
	anslen = 1;
	for(int i=1;i<len;i++){
		ans.resize(14);
		ans[anslen++] = R[i];
		if(c != 0 && anslen >= 2){
			if( (ans[anslen-2] == C[0] && ans[anslen-1] == C[1]) || (ans[anslen-2] == C[1] && ans[anslen-1] == C[0]) ){
				ans[anslen-2] = C[2];
				anslen --;
			}
		}
		if(o != 0 && anslen >= 2){
			if(ans[anslen-1] == O[0]){
				for(int j=anslen-2;j>=0;j--){
					if(ans[j] == O[1]){
						ans = "";
						anslen = 0;
						break;
					}
				}
			}
			else if(ans[anslen-1] == O[1]){
				for(int j=anslen-2;j>=0;j--){
					if(ans[j] == O[0]){
						ans = "";
						anslen = 0;
						break;
					}
				}
			}
		}
	}
}
void output()
{
	printf("[");
	for(int i=0;i<anslen-1;i++)
		cout << ans[i] << ", ";
	if(anslen >= 1) cout << ans[anslen-1];
	cout << "]\n";
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int T,asdf = 1;
	scanf("%d",&T);
	while( T -- ){
		ans = "";
		anslen = 0;
		input();
		printf("Case #%d: ",asdf);
		pro();
		output();
		asdf ++ ;
	}
}