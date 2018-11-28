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
		M.clear();
		int n,i,j;
		scanf("%d",&n);
		for(i=0; i<20; ++i) scanf("%d",&X[i]);
		printf("Case #%d:\n", I+1);
		if( !sum(0) )
			printf("Impossible\n");

/*
		vector<int> v;
		multiset<int> s;
		int n,i,x;
		scanf("%d",&n);
		int sum=0;
		for(i=0;i<n;++i) { scanf("%d",&x); v.push_back(x); sum+=x; s.insert(x); }
		printf("Case #%d: ", I+1);
		multiset<int>::iterator it = s.begin();
		int min = *it;
		++it;
		int min2 = *it;
		for(i=0;i<n;++i)
		{
			double p;
			if( v[i]==min )
			{
				p = 0.5 * ( 1+ (min2-v[i])/(double)sum );
			}
			else
			{
				p = 0.5 * ( 1+ (min-v[i])/(double)sum );
			}
			printf(" %lf", p);
		}
		printf("\n");
*/
	}
	return 0;
}


