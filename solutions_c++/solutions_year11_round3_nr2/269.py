#if 1
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <algorithm>
#include <functional>
#include <iterator>	
#include <list>
#include <queue>
#include <climits>
#include <hash_set>
#include <hash_map>
#include <ctime>
//#include "BinaryTree.h"
//#include "numrep.h"
using namespace std;

string	Directory = "C:\\";
string	files[]={	"-test.txt",			//0
					"-small-practice.in",	//1
					"-large-practice.in",	//2
					"-small.in",			//3
					"-large.in",			//4
					"-small-attempt",		//5
					"-large-attempt"		//6
					};
int		InputSelect		= 4;
string	ProblemLetter	= "B";	
bool	FileOutput		= 1;	//stdout is redirected into a file
bool	SeperateOutput	= 0;	//Produce a seperate output file for each input
string	Attemp			= "1";

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

typedef				__int64		int64;
typedef unsigned	__int64		uint64;
typedef unsigned	__int32		uint;

typedef list<int> li;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<int64> vl;
typedef map<int,int> mii;
typedef mii::iterator miiit;
typedef multimap<int,int> mmii;
typedef mmii::iterator mmiiit;

char* alph="abcdefghijklmnopqrstuvwxyz";


void init(int T)
{
	 
}
uint64 a[1000];
uint64 d[1000000];

void main2()
{
	uint64  i,j,count=0,n,L,t,N,C,k;

	cin >> L>>t>>N>>C;
	fi(C)
		cin>>a[i];
	
	for(k=0;k*C<N;k++)
		for(i=0;i<C;i++)
			d[k*C+i]=2*a[i];

	uint64  ti=0;
	fi(N)
	{
		ti+=d[i];
		if(ti>t) break;
	}
	
	if(i==N)
	{ cout<<ti<<endl;
	return;}

	d[i]=ti-t;
	ti=t;

	sort(d+i,d+N,greater<uint64>());
	if(L>0)
	fj(L)
	{
		if(i+j==N)
			break;

		if(d[i+j]%2)
			cerr<<"asdAsd"<<endl;
		ti+=d[i+j]/2;
	}
	else
		j=0;
	for(i=i+j;i<N;i++)
		ti+=d[i];



	//printf("%.12lf\n",middle);
	cout<< ti <<endl;	
}


int main()
{	
	if(InputSelect>=5)
		files[InputSelect]+=Attemp+".in";

	if(freopen( (Directory+ProblemLetter+files[InputSelect]).data(), "r", stdin )==NULL)
	{
		cout  << "FILE NOT FOUND"  << endl;
		cerr  << "FILE NOT FOUND"  << endl;
		exit(1);
	}

	if(FileOutput)
		if(SeperateOutput)
			freopen( (Directory+"Output-"+ProblemLetter+files[InputSelect]).data() ,"w",stdout);
		else
			freopen( (Directory+"Output.txt").data() ,"w",stdout);
			
	clock_t start = clock();

	int T,i;
	scanf_s("%d\n", &T) ;
	init(T);
	fo(i,1,T+1) {
		cerr << "Case #" << i <<endl;		
		cout << "Case #" << i << ": ";
		main2();
	}

	cerr<<"Elapsed:"<<(clock()-start)*1.0/CLOCKS_PER_SEC<<endl;
	
	return 0;
}

#endif