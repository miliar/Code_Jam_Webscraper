#include <cstdio>
#include <cstring>
#include <map>
using namespace std;
#define REP(i,n) for (int i=0;i<(n);i++)

map<char, int> m;
int alpcount=0;

char buf[256];

int getint()
{
	fgets(buf, 256, stdin);
	return atoi(buf);
}

char* getline()
{
	fgets(buf, 256, stdin);
	return buf;
}

int main()
{
	int tc=getint();
	for (int tno=1; tno<=tc; tno++) {
		char* l = getline();
		alpcount=0;
		m.clear();

		int len=strlen(l);		
		int ml=0;
		REP(i,len) {
			if (l[i]=='\n'||l[i]=='\r') break;
			char c = l[i];
			if ( m.find(c) == m.end() ) {
				if (alpcount==0) m[c]=1;
				else if (alpcount==1) m[c]=0;
				else m[c]=alpcount;
				alpcount++;
			}
			ml=i;
		}
		long long base=alpcount;
		if (base==1) base=2;
		long long curdig=1;
		long long minv=0;
		for (int i=ml;i>=0;i--) {
			char c = l[i];
			minv += curdig * m[c];
			curdig *= base;
		}
		printf("Case #%d: %lld\n", tno, minv);
	}
	return 0;
}

