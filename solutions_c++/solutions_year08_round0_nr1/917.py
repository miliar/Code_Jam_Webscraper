//Grzegorz Prusak: problem "saving the universe" (code.jam 2008)
#include <cstdio>
#include <string>
#include <map>
#include <set>

//loops
#define REP(i,n)   for(register int i=0; i<(n); ++i) 
#define FOR(i,p,k) for(register int i=(p); i<=(k); ++i)

//****************************************************

const int len_max = 120;

//****************************************************

int main()
{
	int n; scanf("%d",&n);
	FOR(i,1,n)
	{
		int s; scanf("%d\n",&s);
		std::map<std::string,int> M; 
		REP(j,s){ char a[len_max+1]; gets(a); M[std::string(a)] = j; }
		
		int q; scanf("%d\n",&q);
		std::set<int> S;
		int res = 0;
		REP(j,q)
		{
			
			char a[len_max+1]; gets(a);
			S.insert(M[std::string(a)]);
			if(S.size()==s){ res++; S.clear(); S.insert(M[std::string(a)]); }		
		}
		
		printf("Case #%d: %d\n",i,res);
	}
}

