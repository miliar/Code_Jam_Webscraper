#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <cstdio>

using namespace std;
const int MAX = 10000;

int main(int argc, char *argv[])
{
	int T,M,N,count;
	string s ="",s2 = "";
	char *tmp = new char[MAX];	
	set<string> C;

	scanf("%d\n",&T);
	for( int t = 0 ; t < T ; t++ ) {
		scanf("%d %d\n",&N,&M);
		C.clear();
		for( int n = 0 ; n < N ; n++ ) {
			s = "";
			scanf("%s\n",tmp);
			C.insert(string(tmp));	
		} 

		count = 0;
		for( int m = 0 ; m < M ; m++ )	{
			scanf("%s\n",tmp);
			string s(tmp);
			string s2 = s;	
			 for( unsigned int i = s2.size() ;  (i = s2.rfind("/",i)) != string::npos ; s2 = s2.substr(0,i) ) {
				if( C.find(s2) == C.end() ) {
					count++;
					C.insert(s2);
				}
			}
		}

		printf("Case #%d: %d\n",t+1,count);
 
	}

	delete [] tmp;
	return 0;
}
