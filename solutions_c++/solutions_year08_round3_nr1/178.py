#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int n,p,k,l;
int freq[1005];

int main()
{
	freopen("A-large.in", "rt", stdin);
	FILE* fp = fopen( "out.txt", "wt" );
	int t;
	int i,j;

	cin>>t;
	for( i=0; i<t; i++ ){
		cin>>p>>k>>l;
		for( j=0; j<l; j++ ) {
			cin>>freq[j];
		}


		sort( &freq[0], &freq[l] );
		int s,e;
		s=0; e=l-1;
		int temp;
		while( s<e ) {
			temp = freq[s]; freq[s]=freq[e]; freq[e]=temp;
			s++;
			e--;
		}

		long long ans=0;
		int cnt=1;
		int st=0;
		bool impossible=false;
		while( st < l ) {

			for( j=0; j<k; j++ ) {
				if( st+j >= l ) {
					st = l;
					break;
				}

				ans += (long long)(cnt*freq[st+j]);
			}
			st = st+k;
			cnt++;

		
		}

		fprintf(fp, "Case #%d: %lld\n", i+1, ans );


		
	}
	fclose(fp);

	return 0;
}