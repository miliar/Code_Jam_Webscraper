
#include <cstdio>
#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std ;

#define FOR(i,s,e) for(i = (s); i <= (e); ++i)
#define FORDOWN(i,s,e) for(i = (s); i >= (e); --i)
#define FOREACH(it,v) for(it = (v).begin(); it != (v).end() ; ++it)

#define mp makepair


int sum(vector<int>::iterator beg,	vector<int>::iterator end)
{
	int sm = 0 ;
	vector<int>::iterator it ;
	for(it =beg; it != end; it++) sm += *it ;
	return sm ;

}

void reverse(vector<int> & v)
{
	int i;
	FOR(i,0,(v.size()-1)/2)
		swap(v[i],v[v.size()-1-i]) ;
}

void solve(FILE * ip, char *buf)
{
	int p,k,d,i,n ;
	vector<int> let ;

	fscanf(ip,"%d%d%d",&p,&k,&n) ;
	let.resize(n) ;

	FOR(i,0,n-1)
		fscanf(ip,"%d",&let[i]) ;

	if (p*k < n)
	{
		sprintf(buf,"Impossible") ;
		return ;
	}

	sort(let.begin(),let.end()) ;
	reverse(let) ;

	int keystrokes = 0, prod = 1 ;
	vector<int>::iterator it = let.begin() ;

	while (it != let.end())
	{
		int range = min (let.end() - it, k) ;
		keystrokes += prod*sum(it,it+range) ;
		printf("%d %d %d\n",prod,range, keystrokes) ;
		it = it + range ;
		++prod ;
	}

//	sprintf(buf,"%d %d %d %d",p,k,n,keystrokes) ;
	sprintf(buf,"%d",keystrokes) ;

}


char buf[10000] ;

int main()
{
	int numcases = 0, caseno = 0;
	FILE *ip = fopen("C:\\Users\\Zoheb\\Documents\\Visual Studio 2008\\Projects\\GCJ\\GCJ\\tp.in","rt") ;
	fscanf(ip,"%d",&numcases) ;
	FILE *op = fopen("C:\\Users\\Zoheb\\Documents\\Visual Studio 2008\\Projects\\GCJ\\GCJ\\output.txt","wt") ;
	assert(ip && op) ;

	printf("Number of cases = %d\n", numcases) ;
	FOR(caseno,1,numcases)
	{
		solve(ip,buf) ;
		printf("Case #%d: %s\n",caseno,buf) ;
		fprintf(op,"Case #%d: %s\n",caseno,buf) ;
	}

	fclose(ip) ;
	fclose(op) ;

	getchar() ;
	return 0 ;
}