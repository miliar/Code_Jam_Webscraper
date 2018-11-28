#import<iostream>
#import<vector>

using namespace std;


int main(){
	int T,N,S,p;
	scanf("%d",&T);
	int i = 1;
	while(T--){
		int ans = 0;
		scanf("%d %d %d",&N, &S, &p);
		int n = N;
		int up = (p-1) * 3;
		int doneS = 0;
		while(n--){
			int value;	
			 scanf(" %d", &value);
			 if(value > up )
				ans++; 
			 else if(doneS < S && ( value == up || value == up -1  ) && value != 0){
				ans++;
				doneS++;
			}	
			 	
		}

		printf("Case #%d: %d\n",i++,ans);
	}
	return 0;
}
