#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int n;
	for( int k = 1; k <= t; k++ ){
	cin>>n;
	char a[n+1];
	int pb[n+1];
	for(int i = 1; i <= n; i++ )
	{
		cin>>a[ i ];
		cin>>pb[i];
	}

	int mtime = 0;
	int bc = 1;
	int oc = 1;
	int bn = 1;
	int bnext = 0;
	int on = 1;
	int onext = 0;
	while( bn <= n && a[bn] != 'B' )
	bn++;
	if( bn <= n )
	bnext = pb[bn];
	
	
	while( on <= n && a[on] != 'O'  )
	on++;
	if( on <= n )
	onext = pb[on];
	
	
	for( int j = 1; j <= n; j++ ){
	
	if( bn == j )
	{
		mtime = mtime + fabs(bnext - bc) + 1;
		if( fabs(bnext - bc) + 1 < fabs(onext - oc ))
		if( onext > oc )
		oc = oc + fabs( bnext -bc)+1;
		else
		oc = oc - (fabs( bnext - bc ) + 1);
		else
		oc = onext;
		bc = bnext;
		
		if( bn < n ){bn++;
		while( bn <= n && a[bn] != 'B'  )
		bn++;
		if( bn <= n )
		bnext = pb[bn];
		}
	}
	else 
	{
		mtime = mtime + fabs(onext - oc) + 1;
		if( fabs(onext -oc) + 1  < fabs( bnext - bc))
		if( bnext > bc )
		bc = bc + fabs(onext - oc)+1;
		else
		bc = bc - (fabs(onext - oc) + 1 );
		else
		bc = bnext;
		oc = onext;
		if( on < n ){on++;
		while( on <= n && a[on] != 'O' )
		on++;
		if( on <= n )
		onext = pb[on];
		}
	}
	}
	cout<<"Case #"<<k<<": "<<mtime<<endl;
	}
	return 0;
}
