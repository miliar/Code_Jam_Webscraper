#include <cstdio>
#include <queue>
#include <vector>

using namespace std;

typedef struct Group{

	long long num;
	int index;

	Group(){ num = 0; index = -1; }
	Group( long long in_num , int in_index ){ num = in_num; index = in_index; }
}G;

long long R,K,N;
queue<G> waitQueue;
queue<G> rollQueue;
vector<long long> money;

long long solve( void ){

	bool again = false;
	money.clear();
	money.push_back( 0 );

	int curR = 0;
	while( true ){

		if( waitQueue.front().index == 0 && again == true )
			break;

		curR ++;
		if( curR > R )
			break;

		again = true;

		long long curK = 0;
		while( !waitQueue.empty() && curK + waitQueue.front().num <= K ){
			curK += waitQueue.front().num;
			rollQueue.push( waitQueue.front() );
			waitQueue.pop();
		}

		money.push_back( curK );

		while( !rollQueue.empty() ){
			waitQueue.push( rollQueue.front() );
			rollQueue.pop();
		}

	}

	for( int i = 1 ; i < money.size() ; i ++ )
		money[i] = money[i-1] + money[i];

	if( curR >= R )
		return money[ money.size()-1 ];

	return (R/curR)*money[ money.size()-1 ] + money[R%curR] ;
}

void readData( void ){


	while( !waitQueue.empty() )
		waitQueue.pop();
	while( !rollQueue.empty() )
		rollQueue.pop();

	long long t_input;
	for( int i = 0 ; i < N ; i ++ ){
		scanf("%lld",&t_input);
		waitQueue.push( G( t_input , i ) );
	}

	return;
}

int main( void ){

	freopen( "C-small-attempt0.in" , "r" , stdin );
	freopen( "C-small-attempt0.out" , "w" , stdout );

	//freopen( "C-large.in" , "r" , stdin );
	//freopen( "C-large.out" , "w" , stdout );

	int testcases;
	scanf("%d",&testcases);
	for( int cases = 1 ; cases <= testcases ; cases ++ ){

		scanf("%lld%lld%lld",&R,&K,&N);
		readData();
		printf("Case #%d: %lld\n",cases,solve());
	}

	//system("pause");

	return 0;
}