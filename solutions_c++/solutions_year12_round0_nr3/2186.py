#include <sstream>
#import <stdlib.h>
#import <iostream>
#import <map>
#import <set>
using namespace std;

char st[100];

int checkFor(const char *a ,const char *b){
	int len = strlen(a);
	strcpy(st, a);
	strcat(st , a);

	int ans = 0;
	set<string> s;
	for( int i = 1; i< len; i++){
		char * cmp = st+i;
		int ret = strncmp(cmp, b, len);
		if( ret <= 0){
			ret = strncmp(a, cmp, len);
			if(ret < 0){
				pair<set<string>::iterator,bool> ret;
				string 	newnumber = cmp;
				newnumber = newnumber.substr(0 , len);
				ret = s.insert(newnumber);
				if(ret.second == true)
					ans++;
			}
		} 
	}
	return ans;
}



int main()
{
	int N,A,B;
	const char *a, *b;
	scanf("%d",&N);
	int i = 1;
	while(N--){
		string sb;
		stringstream ssb;

		scanf("%d %d",&A,&B);
		
		ssb << B;
		sb = ssb.str();
		b = sb.c_str();
		
			int ans = 0;		
		for(int j = A; j < B; j++){
			string sa;
			stringstream ssa;
			ssa << j;
			sa = ssa.str();
			a = sa.c_str();


			ans += checkFor(a,b);	
		}	
		printf("Case #%d: %d\n",i++,ans);
	}
}
