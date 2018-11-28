//A.cpp
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
int L , D , N;
char w[5000][16];
char s[1000];
int c;
bool match(char *pt , char *w)
{
	int l = 0;
	bool find;
	for ( int i=0 ; i<L ; ++i ) 
		if ( '('!=pt[l] && ')'!=pt[l] ) 
		{
			if ( w[i]!=pt[l] ) return false;
			++l;
		}
		else
		{
			find = false;
			for ( ++l ; !('a'<=pt[l] && pt[l]<='z') && '\0'!=pt[l] ; ++l );
			for ( ; 'a'<=pt[l] && pt[l]<='z' && '\0'!=pt[l] ; ++l ) 
				if ( w[i]==pt[l] ) find = true;
			if ( !find ) return false;	
		}
	return true;
}
int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	scanf("%d%d%d\n" , &L , &D , &N);
	for ( int i=0 ; i<D ; ++i ) 
		gets(w[i]);
	for ( int i=1 ; i<=N ; ++i ) 
	{	
		gets(s);
		c = 0;
		for ( int j=0 ; j<D ; ++j ) 
			if ( match(s , w[j]) ) ++c;
		printf("Case #%d: %d\n" , i , c);	
	}
	return 0;
}
