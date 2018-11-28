/*
 * A.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: carlosjosetoribio
 */

#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define PROB 2
#if PROB == 1
int main()
{
	cin.sync_with_stdio(false);
	freopen("out.txt","w",stdout);
	char arr[300];
	arr[ 'a' ] = 'y';
	arr[ 'b' ] = 'h';
	arr[ 'c' ] = 'e';
	arr[ 'd' ] = 's';
	arr[ 'e' ] = 'o';
	arr[ 'f' ] = 'c';
	arr[ 'g' ] = 'v';
	arr[ 'h' ] = 'x';
	arr[ 'i' ] = 'd';
	arr[ 'j' ] = 'u';
	arr[ 'k' ] = 'i';
	arr[ 'l' ] = 'g';
	arr[ 'm' ] = 'l';
	arr[ 'n' ] = 'b';
	arr[ 'o' ] = 'k';
	arr[ 'p' ] = 'r';
	arr[ 'q' ] = 'z';
	arr[ 'r' ] = 't';
	arr[ 's' ] = 'n';
	arr[ 't' ] = 'w';
	arr[ 'u' ] = 'j';
	arr[ 'v' ] = 'p';
	arr[ 'w' ] = 'f';
	arr[ 'x' ] = 'm';
	arr[ 'y' ] = 'a';
	arr[ 'z' ] = 'q';
	
	
	int T;
	cin >> T;
	string A;
	getline(cin,A);
	for(int t = 1;  t<=T ; ++t)
	{
		getline(cin,A);
		cout << "Case #"<<t<<": ";
		for(int j = 0; j < A.size(); ++j)
			cout << (A[j]==' '?' ':arr[A[j]]);
		cout << endl;
	}

	return 0;
}
#elif PROB == 2

int main()
{
	cin.sync_with_stdio(false);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc)
	{
		int N,S,P;
		cin >> N >> S >> P;
		int ma = 0;
		for(int i = 0; i < N; ++i)
		{
			int s; 
			cin >> s;
			int a = s/3 , b = s/3 , c = s/3;
			if( s%3==1 )c++;
			if( s%3==2 )b++ , c++;
			
			if( c  >= P )
				ma++;
			else if(S > 0)
			{
				if(b > 0 && c-b==0)c++ , b--;
				if(c >= P)
					S--, ma++;
			}
		}
		cout <<"Case #"<<tc <<": "<< ma << endl;
	}
	
	return 0;
}

#endif




