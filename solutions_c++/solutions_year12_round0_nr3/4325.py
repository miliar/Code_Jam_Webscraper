#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#include <cstdlib>
#define MAX_N 50010
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
using namespace std;


int n;
int A,B;

bool recycle(int a, int b)
{
	char sa[5];char sb[5] = "";
	itoa(a,sa,10);
	itoa(b,sb,10);
	string ssa = string(sa);
	ssa+=ssa;
	if (ssa.find(sb)!=string::npos) return true;
	//if (p!=NULL) return true;
	/*
	ostringstream s1,s2;	
	s1 << a;
	sa = s1.str();

	s2 << b; sb = s2.str();
	sa +=sa;
	
	*/
	//if (sa.find(sb)!=string::npos) return true;
	return false;
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);  
	string str="";
	cin >> n;
	FR(j,n)
	{
		cin >> A >> B; int count=0;
		FOR(i,A,B-1) FOR(k,i+1,B)
		{
			if (recycle(i,k)) count++;		
		}
		cout << "Case #" << j+1 << ": " << count << endl;
	}
    return 0;
}
