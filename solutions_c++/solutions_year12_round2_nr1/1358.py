#include <stdio.h>

#include <map>
#include <set>
#include <vector>
using namespace std;

multimap<int, int> M;

int X[20];

void print_line(int bit)
{
	bool first = true;
	for(int i=0; i<20; ++i)
	{
		if( bit & (1<<i) )
		{
			if(first) first=false; else putchar(' ');
			printf("%d", X[i]);
		}
	}
	printf("\n");
}
void handle_found( int sum, int bit )
{
	typedef multimap<int,int>::iterator P;
	pair<P, P> range = M.equal_range(sum);
	for( P it=range.first; it!=range.second; ++it )
	{
		if( it->first == sum && (it->second & bit) == 0 )
		{
			print_line(it->second);
			print_line(bit);
		}
	}
}

bool sum(int pos)
{
	if( pos == 20 )
		return false;

	multimap<int, int> N;
	for(multimap<int,int>::iterator it = M.begin(); it!=M.end(); ++it)
	{
		int newsum = it->first+X[pos];
		int newbit = it->second | (1<<pos);
		if( M.find(newsum) != M.end() )
		{
			handle_found( newsum, newbit );
			return true;
		}
		N.insert( pair<int,int>(newsum, newbit) );
	}
	if( M.find(X[pos]) != M.end() )
	{
		handle_found (X[pos], 1<<pos);
		return true;
	}
	M.insert( pair<int,int>(X[pos], 1<<pos) );
	M.insert( N.begin(), N.end() );

	return sum(pos+1);	
}

int main(int argc, char* argv[])
{

	int N;
	scanf("%d",&N);
	char ch[1025];
	gets(ch);
	for(int I=0; I<N; ++I)
	{
/*
		M.clear();
		int n,i,j;
		scanf("%d",&n);
		for(i=0; i<20; ++i) scanf("%d",&X[i]);
		printf("Case #%d:\n", I+1);
		if( !sum(0) )
			printf("Impossible\n");
*/

		vector<int> v;
		vector<double> t;
		int n,i,x;
		scanf("%d",&n);
		double sum=0;
		for(i=0;i<n;++i) { scanf("%d",&x); v.push_back(x); t.push_back(1); sum+=x; }
		printf("Case #%d:", I+1);
		double target = sum*2;
		double overall = n;
		for(i=0;i<n;++i)
		{
			if( sum*2/n < v[i] )
			{
				t[i] = 0;
				target -= v[i];
				--overall;
			}
		}
		for(i=0;i<n;++i)
		{
			if( t[i] == 1 )
			{
//				if( target/overall < v[i] )
//					break;
				t[i] = (target/overall-v[i])/sum;
			}
		}
		for(i=0;i<n;++i)
			printf(" %lf", 100*t[i]);
		printf("\n");

	}
	return 0;
}


