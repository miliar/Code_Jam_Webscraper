// Tim  

#include <queue> 
#include <map> 

#include <set>
#include <stack> 
#include <list>
#include <numeric>

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b)  for (int i=int(a); i<=int(b); ++i)
#define Ford(i,a,b) for (int i=int(a); i>=int(b); --i) 
#define Rep(i,n)    for (int i=0; i<int(n); ++i)
#define RepV(i,v)   for (int i=0; i<sz(v); ++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef pair <int,int> PI;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
typedef long long LL;

const string pr_name="Ds";
const int oo=10000;
int T,n,k,res=0;
string s;
VI per;

string perm(){
	string a;
	Rep(j,sz(s)/k){
		RepV(i,per)
			a.push_back(s[j*k+per[i]]);
	}
	return a;
}

int qqq(string a){	
	return unique(All(a))-a.begin(); 
}



int main() {
	freopen((pr_name+".in").c_str(),"rt",stdin);
	freopen((pr_name+".out").c_str(),"wt",stdout);
	
	scanf("%d\n",&T);
	For(TT,1,T){
		scanf("%d\n",&k);
		getline(cin,s);
		per.assign(k,0);
		RepV(i,per) per[i]=i;
		res=sz(s);
		do {
			res=min(res,qqq(perm()));			

		}while (next_permutation(All(per)));


		printf("Case #%d: %d\n",TT,res);
	}


	return 0;
}


