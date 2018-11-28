#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

struct node{
	char ss, se;
	int st, et;
};

int t, na, nb, n, ansa, ansb;
node s[110];
char stas[1000], curs[1000];
int redt[1000], m;

bool cmp(node s1, node s2)
{
	return s1.st<s2.st || (s1.st==s2.st && s1.et<s2.et);
}

void input()
{
	int i, a, b;
	char str[20];
	
	scanf("%d", &t);
	scanf("%d%d", &na, &nb);
	n=na+nb;
	
	for(i=0; i<na; i++){
		scanf("%s", str);
		a=((str[0]-'0')*10+(str[1]-'0'))*60+((str[3]-'0')*10+(str[4]-'0'));
		//printf("%s %d\n", str, a);
		scanf("%s", str);
		b=((str[0]-'0')*10+(str[1]-'0'))*60+((str[3]-'0')*10+(str[4]-'0'));
		//printf("%s %d\n", str, b);
		s[i].ss='A';
		s[i].se='B';
		s[i].st=a;
		s[i].et=b;
	}
	for(i=0; i<nb; i++){
		scanf("%s", str);
		a=((str[0]-'0')*10+(str[1]-'0'))*60+((str[3]-'0')*10+(str[4]-'0'));
		scanf("%s", str);
		b=((str[0]-'0')*10+(str[1]-'0'))*60+((str[3]-'0')*10+(str[4]-'0'));
		s[i+na].ss='B';
		s[i+na].se='A';
		s[i+na].st=a;
		s[i+na].et=b;
		
	}
	
//	for(i=0; i<n; i++) printf("%c %c %d %d\n", s[i].ss, s[i].se, s[i].st, s[i].et);
	sort(s, s+n, cmp);
	
}

int find(node sp)
{
	int i, ret=-1;
	for(i=0; i<m; i++)
		if(curs[i]==sp.ss && redt[i]<=sp.st){
			if(ret<0 && redt[ret]<redt[i]) ret=i;
		}
	return ret;
}

void solve()
{
	int i, k;
	
	for(i=0; i<1000; i++){
		stas[i]=curs[i]='X';
		redt[i]=0;
	}
	m=0;
	
	for(i=0; i<n; i++){
		k=find(s[i]);
		if(k<0){
			stas[m]=s[i].ss;
			curs[m]=s[i].se;
			redt[m]=s[i].et+t;
			m++;
		}
		else{
			curs[k]=s[i].se;
			redt[k]=s[i].et+t;
		}
	}
	
//	for(i=0; i<m; i++) printf("%c %c %d\n", stas[i], curs[i], redt[i]);
	
	ansa=0; ansb=0;
	for(i=0; i<m; i++)
		if(stas[i]=='A') ansa++;
		else ansb++;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int cc, ct;
	
	scanf("%d", &cc);
	for(ct=1; ct<=cc; ct++){
		input();
		solve();
		printf("Case #%d: %d %d\n", ct, ansa, ansb);
	}
	
	return 0;
}
