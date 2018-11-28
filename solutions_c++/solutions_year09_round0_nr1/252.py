#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define sz size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

int n,l,d;
bool M[10000][26];

int main(){

 	cin>>l>>d>>n;

    
   
	vector<string>S(d);
	FORN(i,d)
		cin>>S[i];
	FORN(CASEEE,n){
		string tmp;
		cin>>tmp;
		//
		 
		
		memset(M,0,sizeof M);
		int pos=0;
		int K=0;

		while (pos<tmp.size())
		if (tmp[pos]=='('){
			pos++;
			while(tmp[pos]!=')'){
				M[K][tmp[pos++]-'a']=1;
			}
			pos++;
			K++;
		}	
		else {
			M[K++][tmp[pos++]-'a']=1;
		}

		int res=0;
			
		if (K==l){
		
			foreach(it,S){
				bool add=true;
				FORN(x,l){
					if (!M[x][(*it)[x]-'a']){
						add=false;break;
					}
				}
				if (add){
					res++;
				}
			}
			
		}
		printf("Case #%d: %d\n",CASEEE+1,res);

	}
    


    return 0;
}




