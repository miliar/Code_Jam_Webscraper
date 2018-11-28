/*
 * A.cpp
 */

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int conv(char ch) {
	if(ch>='a' && ch<='z') return int(ch-'a');
	return int(ch-'0'+26);
}

// proc. one case with number #num
void proc(char* s, int cn) {
	bool b[40]; memset(b, 0, sizeof(b)); 
	int len=strlen(s);
	for(int i=0; i<len; i++) {
		b[conv(s[i])]=true;
	}
	int cnt=0;
	for(int i=0; i<40; i++) if(b[i]) cnt++;
	if(cnt==1) cnt=2;

	int bb[40]; for(int i=0; i<40; i++) bb[i]=-1; 
	long long sum=1; 
	bb[conv(s[0])]=1;
	for(int i=1; i<len; i++) {
		int nn=conv(s[i]);
		if(bb[nn]<0) {// not assigned yet
			int choice=-1;
			for(int x=0; x<40; x++) {
				bool found=false;
				for(int xx=0; xx<40; xx++) 
					if(bb[xx]==x) {
						found=true;
						break;
					}
				if(!found) {
					choice=x;
					break;
				}
			}
			
			bb[nn]=choice;
		} 
		sum*=cnt; sum+=bb[nn];
	}
	
	printf("Case #%d: %ld\n", cn, sum);
}

int main( int argc, const char* argv[] ) {
	if(argc>1) assert(freopen(argv[1], "r",stdin));
	if(argc>2) assert(freopen(argv[2], "w",stdout));
	
	/////////////////
	int caseNum; scanf("%d", &caseNum);
	for(int i=0; i<caseNum; i++) {
		char num[80]; scanf("%s", num);
		proc(num, i+1);
	}
	return 0;
}