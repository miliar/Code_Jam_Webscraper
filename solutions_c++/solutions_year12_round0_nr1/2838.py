/*	Martuza
 * 	Islamic University
 *  martuza.cse@gmail.com
 * */

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
 
#include <cmath>
#include <iostream>
#include <fstream>
 
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <stack>

using namespace std;
 
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
 
#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define CLR(a) memset(a, 0, sizeof(a))
#define MCLR(a) memset(a, -1, sizeof(a))
#define READ(input) freopen("input", "r", stdin);
#define WRITE(output) freopen("output", "w", stdout):
#define sf scanf
#define pf printf
#define re return
 
#define all(a) a.begin(),a.end()
#define pb push_back
#define vi vector<int>
#define qi queue<int>
#define pqi priority_queue<int>
#define msi map<string, int>
 
#define i64 long long
#define pi (2.0*acos(0.0))
#define eps (1e-11)
#define inf 1e9

int main(){
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int tc,kas = 0;
	scanf("%d", &tc);
	getchar();
	while(tc--){
		char w[110] = {0};
		gets(w);
		int l = strlen(w);
		for(int i = 0; i < l; i++){
				 if(w[i] == 'a') w[i] = 'y';
			else if(w[i] == 'b') w[i] = 'h';
			else if(w[i] == 'c') w[i] = 'e';
			else if(w[i] == 'd') w[i] = 's';
			else if(w[i] == 'e') w[i] = 'o';
			else if(w[i] == 'f') w[i] = 'c';
			else if(w[i] == 'g') w[i] = 'v';
			else if(w[i] == 'h') w[i] = 'x';
			else if(w[i] == 'i') w[i] = 'd';
			else if(w[i] == 'j') w[i] = 'u';
			else if(w[i] == 'k') w[i] = 'i';
			else if(w[i] == 'l') w[i] = 'g';
			else if(w[i] == 'm') w[i] = 'l';
			else if(w[i] == 'n') w[i] = 'b';
			else if(w[i] == 'o') w[i] = 'k';
			else if(w[i] == 'p') w[i] = 'r';
			else if(w[i] == 'q') w[i] = 'z';
			else if(w[i] == 'r') w[i] = 't';
			else if(w[i] == 's') w[i] = 'n';
			else if(w[i] == 't') w[i] = 'w';
			else if(w[i] == 'u') w[i] = 'j';
			else if(w[i] == 'v') w[i] = 'p';
			else if(w[i] == 'w') w[i] = 'f';
			else if(w[i] == 'x') w[i] = 'm';
			else if(w[i] == 'y') w[i] = 'a';
			else if(w[i] == 'z') w[i] = 'q';
		}
		printf("Case #%d: %s\n", ++kas, w);
	}
	
	
	return 0;
} 
