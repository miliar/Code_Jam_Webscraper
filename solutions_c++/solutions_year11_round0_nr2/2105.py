#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 111
#define maxm 111
#define maxk 1111111

using namespace std;

int test,n,m,k;
int a[maxn][maxn];
bool b[maxn][maxn];
char c[maxk];
int sl[maxn];
char ch[maxn];
string s;

int get(char ch){
	return int(ch)-int('A');
}

void input(){
	int i,j,v,w,t;
	bool ok1,ok2,ok3;
	string p;
	memset(a,0,sizeof(a));
	memset(b,true,sizeof(b));
	ch[0]='A';
	for (i=1;i<26;i++) ch[i]=ch[i-1]+1;
	getline(cin,s);
	ok1=true;
	ok2=false;
	ok3=false;
	i=0;
	t=0;
	while (i<s.length()){
		if (s[i]==' '){
			i++;
			continue;
		}
		p="";
		for (j=i;j<s.length();j++)
			if (s[j]!=' '){
				p=p+s[j];
				v=j;
			}else break;
		i=v+1;
		if (ok3){
			t++;
			if (t>1){
				s=p;
				break;
			}
			continue;
		}
		if (ok2){
			t++;
			if (t==1){
				w=atoi(p.c_str());
				m=0;
			}else{
				m++;
				b[get(p[0])][get(p[1])]=false;
				b[get(p[1])][get(p[0])]=false;
			}
			if (m==w){
				ok3=true;
				t=0;
			}
			continue;
		}
		if (ok1){
			t++;
			if (t==1){
				w=atoi(p.c_str());
				n=0;
			}else{
				n++;
				a[get(p[0])][get(p[1])]=get(p[2]);
				a[get(p[1])][get(p[0])]=get(p[2]);
			}
			if (n==w){
				ok2=true;
				m=0;
				t=0;
			}
			continue;
		}
	}
}

bool ok(){
	int u,v;
	for (u=0;u<26;u++)
		for (v=0;v<26;v++)
			if ((sl[u]>0)&&(sl[v]>0)&&(!b[u][v])) return false;
	return true;
}

void process(){
	int i,u,v,w;
	memset(sl,0,sizeof(sl));
	k=0;
	for (i=0;i<s.length();i++){
		k++;
		c[k]=s[i];
		sl[get(s[i])]++;
		while (k>=2){
			u=get(c[k-1]);
			v=get(c[k]);
			w=a[u][v];
			if (w==0) break;
			sl[u]--;
			sl[v]--;
			sl[w]++;
			k--;
			c[k]=ch[w];
		}
		if (!ok()){
			memset(sl,0,sizeof(sl));
			k=0;
		}
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d\n",&test);
	int i,j;
	for (i=1;i<=test;i++){
		input();
		process();
		cout<<"Case #"<<i<<": [";
		for (j=1;j<k;j++) cout<<c[j]<<", ";
		if (k!=0) cout<<c[k]<<"]\n"; else
			cout<<"]\n";
	}
}
