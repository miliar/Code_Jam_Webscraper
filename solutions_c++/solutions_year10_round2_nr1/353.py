#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <set>
using namespace std;
int main()
{
	FILE* fptr = fopen("c:\\temp\\a.in","r");
	char ch[2000], *p;
	int N, n, m, i, j;
	fscanf(fptr,"%d",&N);
	set<string> s, t;
	for(int I=1; I<=N; ++I)
	{
		s.clear();
		t.clear();
        fscanf(fptr,"%d%d",&n,&m);
		fgets(ch,2000,fptr);
		for(i=0; i<n; ++i)
		{
			p = fgets(ch,2000,fptr);
			int r = strlen(p);
			while( p[r-1] == '\r' || p[r-1] == '\n' )
				p[r-1] = 0;
			s.insert(p);
		}
		for(i=0; i<m; ++i)
		{
			p = fgets(ch,2000,fptr);
			int r = strlen(p);
			while( p[r-1] == '\r' || p[r-1] == '\n' )
				p[r-1] = 0;
			t.insert(p);
		}
		int times = 0;
		for( set<string>::iterator it = t.begin(); it != t.end(); ++it )
		{
			string r = *it;
			if ( r=="/" )
				continue;
			int pos = 1;
			for(;;)
			{
				int newpos = r.find('/',pos);
				string exists = (newpos<0?r:r.substr( 0, newpos ));
				if( s.find(exists) == s.end() )
				{
					++times;
					s.insert(exists);
				}
				if( newpos < 0 )
					break;
				pos = newpos+1;
			}
		}
		printf("Case #%d: %d\n", I, times);
	}
	return 0;
}