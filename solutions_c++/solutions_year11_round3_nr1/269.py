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
#include "BinaryTree.h"
#include "numrep.h"
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
string	ProblemLetter	= "A";	
bool	FileOutput		= 1;	//stdout is redirected into a file
bool	SeperateOutput	= 0;	//Produce a seperate output file for each input
string	Attemp			= "0";

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

char A[50][50];

void main2()
{
	int i,j,count=0,n,R,C;
	string s;
	cin >> R>>C;
	cout<<endl;

	fi(R){
		cin>>s;
		fj(C)
			A[i][j]= s[j];
	}

	fi(R-1) fj(C-1)
		if(A[i][j]=='#' && A[i+1][j]=='#' && A[i][j+1]=='#' && A[i+1][j+1]=='#')
		{
			A[i][j]='/';A[i+1][j]='\\';A[i][j+1]='\\';A[i+1][j+1]='/';
		}

	fi(R) fj(C)
		if(A[i][j]=='#'){
			cout<<"Impossible"<<endl;
			return;}

	fi(R){ fj(C)
		cout<<A[i][j];
		cout<<endl;
	}
	
	//printf("%.12lf\n",middle);
	//cout<< 0 <<endl;	
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