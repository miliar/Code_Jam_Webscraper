// Round 1B: B.cpp

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>


long m=-1, st;
void procOne(char* num, int len,  int pos) {
	if(pos>=len) {
		long value=atoi(num);
		if( (m<0 || value<m) && value>st) 
			m=value;
	}
	for(int k=pos; k<len; k++) {
		char t=num[pos]; num[pos]=num[k]; num[k]=t;
		procOne(num, len, pos+1);
		t=num[pos]; num[pos]=num[k]; num[k]=t;
	}
}

int main() {
	int no; scanf("%d", &no);
	for(int i=0; i<no; i++) {
		char num[25]; memset(num, '\0', 25); scanf("%s", num); 
		m=-1; st=atoi(num); num[strlen(num)]='0';
		procOne(num, strlen(num), 0);
		if(m<0) printf("Case #%d-------------------: %s0\n", i+1, num); 
		else printf("Case #%d: %ld\n", i+1, m);
	}
	
	return 0;
}
