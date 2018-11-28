#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MAXN 10050
#define MAXL 12

const int inf=100000;

int chorder[128];

class Char {
	public:
		char c;
		int x;
		Char() {}
		Char(char ci,int xi):c(ci),x(xi) {
			c=ci;
			x=xi;
		}
/*		operator char() const {
			return c;
		}*/
		const bool operator==(const Char &b) const {
			return c==b.c&&x==b.x;
		}
		const bool operator!=(const Char &b) const {
			return c!=b.c||x!=b.x;
		}
		const bool operator<(const Char &b) const {
			if(chorder[c]!=chorder[b.c]) return chorder[c]<chorder[b.c];
			return x<b.x;
		}
		void print() const {
			printf("<%c,%d>",c,x);
		}
};
class Word {
	public:
		int len,id;
		Char str[MAXL];
		void init(const char* s) {
			for(len=0;s[len];len++)
				str[len]=Char(s[len],len);
			sort();
		}
		void sort() { std::sort(str,str+len); }
		const bool operator<(const Word &b) const {
			int i;
			if(len!=b.len) return len<b.len;
			for(i=0;i<len;i++)
				if(str[i]!=b.str[i]) return str[i]<b.str[i];
			return 0;
		}
		void print() const {
			int i;
			for(i=0;i<len;i++)
				str[i].print(); puts("");
		}
};


bool tried[128];
inline bool valid(const Word &w,int cmpl) {
	int i;
	if(w.len>cmpl) {
		if(tried[w.str[cmpl].c]) return 0;
	}
	return 1;
}
inline int cmpWord(const Word &a,const Word &b,int cmpl) {
	int i;
	if(a.len!=b.len) return (a.len<b.len?-1:1);
	for(i=0;i<a.len&&i<cmpl;i++)
		if(a.str[i]!=b.str[i]) return (a.str[i]<b.str[i]?-1:1);
	return 0;
}

int dsz;
int dlen[MAXN];
char d[MAXN][MAXL];

int qn;
char guess[30];
Word wd[MAXN];
int accum[MAXN][128];

inline void pre2() {
	int i,j;
	for(i=0;i<26;i++)
		chorder[guess[i]]=i;
	for(i=0;i<dsz;i++) {
		wd[i].init(d[i]);
		wd[i].id=i;
	}
	std::sort(wd,wd+dsz);
	for(j='a';j<='z';j++)
		accum[0][j]=0;
	for(i=0;i<dsz;i++) {
		for(j='a';j<='z';j++)
			accum[i+1][j]=0;
		for(j=0;j<wd[i].len;j++)
			accum[i+1][wd[i].str[j].c]=1;
	}
	for(i=1;i<=dsz;i++)
		for(j='a';j<='z';j++)
			accum[i][j]+=accum[i-1][j];
/*	for(i=0;i<dsz;i++) {
		wd[i].print();
		for(j='a';j<='z';j++)
			printf("%d ",accum[i][j]);puts("");
	}*/
}

inline int bsearchl(const Word& w,int revlen) {
	int l=-1,r=dsz,m,res;
	while(l<r-1) {
		m=(l+r)>>1;
		res=cmpWord(wd[m],w,revlen);
		if(res<0) l=m;
		else if(res>0) r=m;
		else {
			if(!valid(wd[m],revlen)) l=m;
			else r=m;
		}
	}
	return r;
}
inline int bsearchr(const Word &w,int revlen) {
	int l=-1,r=dsz,m;
	while(l<r-1) {
		m=(l+r)>>1;
		if(cmpWord(wd[m],w,revlen)>0) r=m;
		else l=m;
	}
	return l;
}

inline int play(const Word &w) {
	int i,revlen,lb,rb,occ,pt=0;
	char g;
	bool flag;
	revlen=0;
//	puts("==");
//	w.print();
//	puts("==");
	memset(tried,0,sizeof(tried));
	for(i=0;i<26;i++) {
		g=guess[i];
		lb=bsearchl(w,revlen);
		rb=bsearchr(w,revlen);
		occ=accum[rb+1][g]-accum[lb][g];
//		printf("<%d %d %d %d>\n",revlen,lb,rb,occ);
		tried[g]=1;
		if(occ==0) continue;
//		printf("[%c]",g);
		flag=0;
		while(revlen<w.len&&w.str[revlen].c==g) {
			flag=1;
			revlen++;
		}
		if(!flag) pt++;
		if(revlen==w.len) {
//			puts("");
			return pt;
		}
	}
	fprintf(stderr,"error!\n");
}

inline int solve() {
	int i,g,opt=-1,opti;
	for(i=0;i<dsz;i++) {
		g=play(wd[i]);
		if(g>opt||g==opt&&wd[i].id<opti) {
			opt=g;
			opti=wd[i].id;
		}
	}
//	fprintf(stderr,"<%d>\n",opt);
	return opti;
}

int main(void)
{
	int t,i,id,casenum=1;
	scanf("%d",&t);
	while(t--) {
		scanf("%d %d",&dsz,&qn);
		for(i=0;i<dsz;i++) {
			scanf("%s",d[i]);
			dlen[i]=strlen(d[i]);
		}
		printf("Case #%d:",casenum++);
		for(i=0;i<qn;i++) {
			scanf("%s",guess);
			pre2();
			id=solve();
			printf(" %s",d[id]);
		}
		puts("");
	}
}
