#include<iostream>
#include<string>
using namespace std;

int d[1000][1000],ts,tests;

int main()
{
	freopen("E:\\1.txt","rt",stdin);
	freopen("E:\\2.txt","wt",stdout);
	 string pat = "welcome to code jam"; 
	 cin >> tests;
	 char r[1000];
	 cin.getline(r,1000);
	 for(int tt = 0; tt < tests; tt++)
	 {
		 char s[1000];
		 ts = 0;
		 cin.getline(s,1000);
		 int n = strlen(s);
		 for(int i = 0; i < 1000; i++)
			 for(int j = 0; j < 1000; j++) d[i][j] = 0;
		 for( int i = 0; i < n; i++)
		 {
			 for(int j = 0; j < pat.length(); j++) if ( s[i] == pat[j] )
			 {
				 if ( j > 0 ) for(int k = 0; k < i; k++) { if ( s[k] == pat[j-1] ) d[i][j] = (d[i][j] + d[k][j-1])%10000;  }
				 else d[i][0] = 1;		 
			 }			
		 }
		 for(int i = 0; i < n; i++) ts = (ts + d[i][pat.length()-1])%10000;
		 printf("Case #%d: %04d\n", tt+1,ts);
	 }
	 return 0;
}