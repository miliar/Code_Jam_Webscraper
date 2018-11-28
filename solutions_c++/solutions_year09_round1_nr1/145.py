#include <iostream>
#include <sstream>
#include <cassert>
using namespace std;

const int LIMIT = 11814486;
int happy[LIMIT];
bool loop[LIMIT];

inline int ssum(int h, int b) {
	int s=0;
	while(h) s+=(h%b)*(h%b), h/=b;
	return s;
}

bool rekur(int h, int b) {
	if(loop[h]) return happy[h]&1<<b;
	loop[h]=true;
	int s = ssum(h,b);
	bool ok = s==1 || rekur(s,b);
	if(ok) happy[h]|=1<<b;
	return ok;
}

void happies() {
	memset(happy, 0, sizeof(happy));
	for(int b=2;b<=10;++b) {
		memset(loop, false, sizeof(loop));
		for(int h=0;h<LIMIT;++h)
			rekur(h,b);
	}
	fprintf(stderr, "Done\n");
}

int main() {
	happies();
	char buff[100];
	fgets(buff,100,stdin);
	int T;
	sscanf(buff, "%d",&T);
	for(int t=0;t<T;++t) {
		fgets(buff,100,stdin);
		istringstream stream(buff);
		int B=0,b;
		while(stream>>b)
			B|=1<<b;
		int i=2;
		for(;i<LIMIT;++i)
			if((happy[i]&B)==B) break;
/*		if(i==LIMIT) {
			for(;i<LIMIT2;++i) {
				bool ok = true;
				for(b=2;(1<<b)<=B;++b)
					if(B&(1<<b)) {
						int s = ssum(i,b);
						if(!(happy[s]&(1<<b))) {
							ok = false;
							break;
						}
					}
				if(ok) break;
			}	
		}*/
		assert(i<LIMIT);
		printf("Case #%d: %d\n",t+1,i);
	}
}