#define Llong long long
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>


#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))
#define mL 200
using namespace std;

ifstream inp("D:\\googleCodeJam\\Saving the Universe\\A-large.in");
ofstream onp("D:\\googleCodeJam\\Saving the Universe\\A-large.out" , ios::out);

char engine_names[200][200];
int engine_numbers, query_numbers;
int used[100];
char aquery[200];
int num = 0;
int main()
{
	int n;
	inp >> n;
	int j;
	for (int i = 0; i < n; i++ ) 
	{
		inp >> engine_numbers;
		inp.getline(aquery, 200);
		for (  j = 0; j < engine_numbers; j++)
			inp.getline(engine_names[j], 200);
		if ( i == 6 )
		for (  j = 0; j < engine_numbers; j++)
		cout<< engine_names[j]<<endl;
		inp >> query_numbers;
		inp.getline(aquery, 200);
		num = 0;
		cout<<endl;
		fill_(used , 0);
		for (  j = 0; j < query_numbers; j++) {
			inp.getline(aquery, 200);
			if ( i == 6 ) cout<<aquery<<endl;
			int p;
			
			for ( p = 0; p < engine_numbers; p++)
				if ( strcmp( aquery, engine_names[p] ) == 0 ) break;
			used[p] = 1;
			int toswitch = 1;
			for ( int k = 0; k < engine_numbers; k++)
				if ( used[k] == 0 ) toswitch = 0;
			
			if (toswitch) {num++; fill_(used, 0); used[p] = 1;} 	
			
		}
		
		onp<<"Case #"<< i + 1<<": "<< num<< endl;
		
	}
	
	
}