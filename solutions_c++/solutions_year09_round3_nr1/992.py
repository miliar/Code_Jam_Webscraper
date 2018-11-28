#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define log  xlog 
struct xLog {
	xLog(int i):a(i){}
	int a ;
};

const int loglevel = 0 ;
xLog xlog(loglevel);

template<typename T>
xLog & operator << (xLog &os, T t)
{
	if(os.a > 0){
		cout << t ; 
	}
	return os;
}

const int maxn=61;

int n;
int A[maxn];

map<char,int>  imap;
void solve(string st)
{
	if(st.size() == 1){
		printf("1");
		return ; 
	}
	set<char>  cset;
	for(int i = 0 ; i < st.size() ; i ++){
		cset.insert(st[i]);
	}
	int base = cset.size() ; 
	if(base == 1){
		base = 2 ;
	}
	log << "\nbase:" << base << "\n";
	imap.insert(make_pair<char,int>(st[0],1));
	set<int>  iset;
	iset.insert(1);
	A[0] = 1 ;
	int cc = 0 ;	
	for(int i = 1 ; i < st.size() ; i ++){
		if(imap.find(st[i]) ==  imap.end()){
			log << "\n can not find: " << st[i] ; 
			while(iset.find(cc) != iset.end()){
				cc ++ ;
			}
			imap.insert(make_pair<char,int>(st[i],cc));
			iset.insert(cc);
			A[i] = cc ;
			cc ++ ; 
		}else{
			A[i] = imap[st[i]];
		}
		log << "\n A[" << i << "]=" << A[i] ; 
	}
	
	unsigned long long res=0;
	unsigned bb = 1; 
	for(int i = st.size() - 1; i >=0 ; i --){
		res += A[i] * bb ;
		bb *= base ;
	}
	printf("%u",res);
	imap.clear();
	
}
int main(int argc, char** argv)
{
	freopen(argv[1],"r",stdin);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		char str[100];
		scanf("%s",str);
		n=0;
		printf("Case #%d: ",caseId);
		log << "\nstr:" << str ;
		solve(string(str));
		printf("\n");
	}
	return 0;
}
