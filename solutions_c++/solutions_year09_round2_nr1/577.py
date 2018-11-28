#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

struct Node {
	int left,right;
	string str;
	double val;
	Node() {left=right=-1;}
	void split();
	double find();
};

char s[100*80*2];
char buf[82];
int cnt,add;

Node nd[100000];
int nn;
void Node::split() {
	left=right=-1;
	while(s[cnt]==' ') ++cnt;
	if (s[cnt]!='(') { printf("WRONG AT BEGINNER OF TREE %d\n", nn); puts(s+cnt); exit(1); }
	++cnt;	// '('
	sscanf(s+cnt,"%lf%n",&val,&add), cnt+=add;
//	printf("  val=%f\n", val);
	while(s[cnt]==' ') ++cnt;
//	printf("node[%d]...\n", nn-1);
	if (s[cnt]==')') { /*puts("NO CHILD");*/ ++cnt;  return; }
//	puts("LEFT RIGHT");
	char tmp[100];
	sscanf(s+cnt,"%s%n",tmp,&add),cnt+=add;
//	puts(tmp);
	str=string(tmp);
	left = nn;
	nd[nn++].split();
	right = nn;
	nd[nn++].split();
	while(s[cnt]==' ')	++cnt;
	if (s[cnt]!=')') { printf("WRONG ED OF TREE %d\n", nn); exit(1); }
	++cnt;
}

vector<string> fea;

double Node::find() {
	if (left==-1)	return val;
	for (int i=0;i<fea.size();i++)
		if (str==fea[i]) {
//			printf("left\n");
			return val*nd[left].find();
		}
//	printf("right\n");
	return val*nd[right].find();
}

int main() {
	int z;
	gets(buf), sscanf(buf,"%d",&z);
	for (int Zz=1; Zz<=z; ++Zz) {
		gets(buf);
//		printf("..");
//		puts(buf);
//		puts("-");
		int L;
		sscanf(buf,"%d", &L);
//		printf("L=%d\n", L);
		int len = 0;
		while (L--) {
			gets(s+len);
			len += strlen(s+len);
		}
		nn=0;
		cnt=0,add;
		nd[nn++].split();

		int A;
		gets(buf);
		sscanf(buf,"%d",&A);
		printf("Case #%d:\n",Zz);
		while (A--) {
			gets(buf);
//			puts(buf);
			int cnt=0,add;
			sscanf(buf,"%s%n",s,&add), cnt+=add;
			int n;
			sscanf(buf+cnt,"%d%n",&n,&add), cnt+=add;
			fea.clear();
			while (n--) {
				char s[100];
				sscanf(buf+cnt,"%s%n",s,&add), cnt+=add;
				fea.push_back(string(s));
			}
			printf("%.7f\n", nd[0].find());
		}
	}
	return 0;
}
