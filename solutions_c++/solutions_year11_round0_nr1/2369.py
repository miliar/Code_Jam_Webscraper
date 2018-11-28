#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

#define mp make_pair
int abs(int a){
    return (a>0)?a:-a;
}

int main(){
	freopen("output.txt","w",stdout);
	char c;
	int k, t, t1, t2, p1, p2;
	int tt = 0, n;
	cin >> t;
	
	while(t--) {

		tt++;
		
		scanf("%d",&n);
		t1 = 0; t2 = 0;
		p1 = 1; p2 = 1;
		for(int i=0;i<n;i++){
			getchar();
			scanf("%c %d",&c,&k);
	
			if(c == 'O'){
				t1 += abs(p1 - k) + 1;
				if(t1 <= t2) t1 = t2+1;
				p1 = k;
			}
			else
			{
				t2 += abs(p2 - k) + 1;
				if(t1 >= t2) t2 = t1+1;
				p2 = k;
			}
			
		}
		
		printf("Case #%d: %d\n",tt,max(t1,t2));
	}
	return 0;
}
