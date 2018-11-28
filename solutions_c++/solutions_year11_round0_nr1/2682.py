#include <iostream>
#include <cmath>
#include <string>
using namespace std;
struct Node{
	char s;
	int x;
}a[105];
int main()
{
	//freopen("E: \\A-small-attempt0.in","r",stdin);
	//freopen("E: \\A-small.out","w",stdout);
	int T,n,cnt=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(int i =0 ; i < n; i++)
			cin>>a[i].s>>a[i].x;
		int pos1=1,pos2=1,ans=0,tmp;
		for(int i = 0 ; i < n ; i ++) {
			if(a[i].s == 'O') {
				tmp = abs(a[i].x - pos1) + 1;
				ans += tmp;
				pos1 = a[i].x;
				for (int j = i +1 ; j < n ; j ++) {
					if( a[j].s == 'B') {
						if(abs(pos2 - a[j].x) <= tmp) pos2 = a[j].x;
						else if (pos2 < a[j].x) pos2 += tmp;
						else pos2 -= tmp;
						break;
					}
				}
			}
			else {
				tmp = abs(a[i].x - pos2) + 1;
				ans+= tmp;
				pos2 = a[i].x;
				for(int j = i +1 ; j < n ; j ++) {
					if(a[j].s == 'O') {
						if(abs(pos1 - a[j].x) <= tmp) pos1 = a[j].x;
						else if (pos1 < a[j].x) pos1 += tmp;
						else pos1 -= tmp;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",++cnt,ans);
	}
	return 0;
}