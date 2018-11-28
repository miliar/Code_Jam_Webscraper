#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("A-large.out");
struct VIPE{
	long d,l;
}vipe[10003];
bool in[10003];
long str[10003],ne[10003];
bool cmp(VIPE u,VIPE v){
	return u.d<v.d;
}
int main(){
	long i,m,n,t,T,h,e;
	fin >> T;
	for (t=1;t<=T;++t){
		fin >> n;
		for (i=1;i<=n;++i){
			fin >> vipe[i].d >> vipe[i].l;
			vipe[i].l=vipe[i].d<vipe[i].l?vipe[i].d:vipe[i].l;
		}
		sort(vipe+1,vipe+n+1,cmp);
		fin >> m;
		++n;
		vipe[n].d=m;
		vipe[n].l=1000000000;
		memset(in,0,10003);
		h=1;
		e=1;
		str[1]=1;
		in[1]=1;
		for (i=2;i<=n;++i){
			while (vipe[str[h]].l+vipe[str[h]].d<vipe[i].d && h<=e) ++h;
			if (h<=e){
				vipe[i].l=vipe[i].d-vipe[str[h]].d<vipe[i].l?vipe[i].d-vipe[str[h]].d:vipe[i].l;
				if (vipe[i].l+vipe[i].d>vipe[str[e]].d+vipe[str[e]].l) str[++e]=i;
			}
			else break;
			/*else
				if (vipe[i].d==vipe[i].l){
					str[++e]=i;
					in[i]=1;
				}*/
			// fout << vipe[i].l << endl;
		}
		fout << "Case #" << t << ": " << (h<=e?"YES":"NO") << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
