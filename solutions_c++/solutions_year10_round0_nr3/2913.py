#include<cstdio>

int groupArr[1000];
long long euros;
int pos;

int main() {
	
	int cases;
	scanf("%d", &cases );
	
	int rounds,capacity, groups;
	for( int i=1; i<=cases; i++ ) {
		scanf( "%d %d %d", &rounds, &capacity, &groups );
		euros = pos = 0;
		
		for( int k=0; k<groups; k++ ) {
			scanf("%d", &groupArr[k] );
		}
		
		int gain, cap, startat;
		for( int r=0; r<rounds; r++ ) {
			gain = cap = 0;
			startat = pos;
			while( cap+groupArr[pos] <= capacity ) {
				cap += groupArr[pos];
				gain += groupArr[pos];
				pos = (pos + 1) % groups;
				
				if( pos == startat ) break;
			}
			
			if( gain == 0 ) break;
			euros += gain;
		}
		
		printf("Case #%d: %lld\n",i, euros);
	}
	
	return 0;
}
