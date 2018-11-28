//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("outB.txt","w",stdout);
	char b[500];//,c[500];
	int I=1,t,j;
	long long x,y;
	bool f;
	for(cin>>t,fgetc(stdin);I<=t;I++) {
	gets(b);
	//strcpy(c,b);
	//cout<<b<<' '<<c<<'\n';
	//do {
		f=next_permutation(b,b+strlen(b));
		//cout<<atoi(c)<<' '<<atoi(b)<<' '<<f<<'\n';
		//if(!f) 
	//}
	//while(atoi(c)>=atoi(b));
	printf("Case #%d: ",I);
	if(f) puts(b);
	else {
		int i=0;
		while(b[i]=='0') i++;
		putchar(b[i]);
		for(j=0;j<=i;j++) putchar('0');
		puts(&b[i+1]);
	}
	}
	return 0;
}
