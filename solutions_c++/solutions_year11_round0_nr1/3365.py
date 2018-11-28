#include <stdio.h>
#include <math.h>
#include <string.h>

int all[100];
int name[100];
int a[100];
int cnta,cntb;
int b[100];

int main()
{
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for ( int t=0; t<T; t++ ){
		int n;
		scanf("%d",&n);
		memset(all,0,sizeof(all));
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		cnta = 0, cntb = 0;
		for ( int i=0; i<n; i++){
			char ch[2];
			scanf("%s %d",ch,&all[i]);
			if ( ch[0]=='B' ) {
				name[i] = 'B';
				b[cntb++] = all[i];
			}
			else {
				name[i] = 'A';
				a[cnta++] = all[i];
			}			
		}
		//
		int res = 0;
		int currentA=1, currentB=1;
		char nowMoving='A';
		int addUpTime=0;
		for ( int i=0; i<n; i++ ){
			if ( name[i]=='A' ){
				int d = abs(all[i]-currentA);
				if ( name[i]==nowMoving ){
					res += d+1;
					currentA = all[i];
					addUpTime += d+1;
				}
				else{
					if ( addUpTime>=d ){
						res += 1;
						currentA = all[i];
						addUpTime = 1;
					}
					else{
						res += 1+(d-addUpTime);
						currentA = all[i];
						addUpTime = 1+(d-addUpTime);
					}
				}		
				nowMoving = 'A';	
			}
			//B
			else{
				int d = abs(all[i]-currentB);
				if ( name[i]==nowMoving ){
					res += d+1;
					currentB = all[i];
					addUpTime += d+1;
				}
				else{
					if ( addUpTime>=d ){
						res += 1;
						currentB = all[i];
						addUpTime = 1;
					}
					else{
						res += 1+(d-addUpTime);
						currentB = all[i];
						addUpTime = 1+(d-addUpTime);
					}
				}
				nowMoving = 'B';  	
			}
		}
		printf("Case #%d: %d\n",t+1,res);
	}
	return 0;
}
