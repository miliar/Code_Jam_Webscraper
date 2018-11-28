#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define rp(i,l,r) for ( int i=(int)(l); i<=(int)(r); ++i )

int n;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.txt","w",stdout);
	cin >> n;
	scanf("%*c");
	string s="yhesocvxduiglbkrztnwjpfmaq"; 
	rp( i,1,n )
	{
		string t;
		getline( cin , t );
		rp( j,0,t.size()-1 ) if ( t[j]!=' ' ) t[j]=s[t[j]-'a'];
		cout << "Case #" << i << ": " << t << endl;
	} // 0 - 0
} // 0 - 0