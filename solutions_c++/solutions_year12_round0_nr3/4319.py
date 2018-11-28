#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

#define floop(i,n) for(int i = 0; i < (int)(n); i++)
#define floopi(i,m,n) for(int i = m; i < (int)(n); i++)
#define floopd(i,m,n) for(int i = m; i > (int)(n); i--)

typedef long long l2;
typedef vector<string> vstr;

int compare(int,int,int);

//#define TEST
#define SMALL
//#define LARGE

void main()
{

#ifdef TEST
	freopen("a.txt", "rt", stdin);
	freopen("b.txt", "wt", stdout);
#endif
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large-practice.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

   int T,A,B,num;
   string s;
   scanf("%d\n", &T);
   floop(i,T)
   {
	    num = 0;
		scanf("%d\n", &A);
		scanf("%d\n", &B);
		
		floopi(j,A,B)
			num+=compare(j,A,B);

		printf("Case #%d: %d\n",i+1,num);
   }
}

int compare(int a, int A, int B)
{
	string s2,s3,s11;
	int total = 0,same = 0;
	char * as = new char [10];

	itoa(a,as,10);
	string s1(as);

	int len = s1.length();
	if(len == 1)
		return false;

	floop(i,len)
	{
		s2 = s1.substr(len - i - 1,i+1);
		s3 = s1.substr(0,len - i - 1);
		s11 = s2+s3;
		int temp = atoi(s11.c_str());
		if(temp <= B && temp > a && temp != same)
		{
			same = temp;
			total++;
		}
	}
	return total;
}