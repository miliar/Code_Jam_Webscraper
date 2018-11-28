#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>

using namespace std;


int sn,qn;
int ans;

char sname[105][105];
char qname[1005][105];
char temp[105];


void solve()
{
	int i,j;
	int st;

	int tmaxdist;
	int maxdist, maxsn;
	int nowsearch;
	ans=0;
	st=0;

	nowsearch=-1;
	while(st<qn)
	{
		maxdist=-1;
		for( i=0; i<sn; i++ ) {
			if( i==nowsearch ) continue;

			tmaxdist=-1;
			for( j=st; j<qn; j++ ) 
			{
				if( strcmp( qname[j], sname[i] )==0 ) {
					tmaxdist=j;
					break;
				}
			}
			if( tmaxdist == -1 ) tmaxdist=10000;

			
			if( maxdist < tmaxdist ) {
				maxdist=tmaxdist;
				maxsn = i;
			}
		}

		if( maxdist == 10000 ) break;

		nowsearch=maxsn;
		st=maxdist;
		ans++;


	}


}

int main()
{
	freopen( "A-large.in", "r", stdin );
	int i,j,tc;
	int n;
	cin>>n;

	FILE* fp=fopen("out.txt", "wt");

	for( tc=0; tc<n; tc++ )
	{
		cin>>sn;
		cin.getline(temp, 105 );
		for( i=0; i<sn; i++ )
		{
			cin.getline(sname[i], 105 );
		}
		cin>>qn;
		cin.getline(temp, 105 );
		for( i=0; i<qn; i++ )
		{
			cin.getline(qname[i], 105 );
		}

		solve();


		fprintf(fp, "Case #%d: %d\n", tc+1, ans );
		//cout<<"Case #"<<tc+1<<": "<<ans<<endl;

	}
	fclose(fp);
	return 0;
}