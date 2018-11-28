#include <stdio.h>
#include <string.h>
#include <map>
#include <string>
using namespace std;

map<string, int> s;

int hasfeature[10005], featureid;
double p;
char r[10000], zp[100];
int zpn=0;
int offset, x;
string zzp;

void go(int flag){
	//printf("flag=%d [%s]\n",flag,r+x);
	while(r[x]!='(') ++x;
	int op;
	double pz;
	++x;
	sscanf(r+x,"%lf%n",&pz,&op);
	if(flag) {p*=pz;//printf("here %.7lf %.7lf\n",p, pz);
	}
	x+=op;
	while(r[x]==' ' || r[x]=='\n') ++x;
	if(r[x]==')'){
		++x;
		return;
	}else{
		zpn=0;
		while(r[x]>='a' && r[x]<='z'){
			zp[zpn++]=r[x++];
		}
		zp[zpn]=0;
		zzp=(string)zp;
		//printf("zzp=%s\n",zzp.c_str());
		if(s.find(zzp)!=s.end() && hasfeature[s[zzp]]==1){
			go(flag);
			go(0);
		}else{
			go(0);
			go(flag);
		}
		while(r[x]!=')') ++x;
		++x;
		
	}
}

int main(void)
{
	int T, n, i, j;
	char z[100];
	int cs=0;
	string bz;
	scanf("%d",&T);
	gets(z);
	while(T--){
		int L, A;
		offset=0;
		scanf("%d",&L);
		gets(z);
		while(L--){
			gets(r+offset);
			while(r[offset]) ++offset;
		}
		scanf("%d",&A);
		printf("Case #%d:\n", ++cs);
		s.clear();
		featureid=0;
		while(A--){
			p=1.0;
			scanf("%s",z);
			memset(hasfeature,0,sizeof(hasfeature));
			scanf("%d",&n);
			while(n--){
				scanf("%s",z);
				bz=(string)z;
				if(s.find(bz)==s.end()){
					++featureid;
					s[bz]=featureid;
				}
				hasfeature[s[bz]] = 1;
			}
			x=0;
			go(1);
			printf("%.7lf\n",p);
		}
	}
	return 0;
}
