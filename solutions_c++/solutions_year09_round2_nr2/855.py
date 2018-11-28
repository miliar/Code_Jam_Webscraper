#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI; 
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;
typedef long long int64;
typedef unsigned long long uint64;
const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);

int comp_(const void *a,const void *b)
{
	return -*(char*)a+*(char*)b;
} 
int comp(const void *a,const void *b)
{
	return *(char*)a-*(char*)b;
} 

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	

	int T;
	cin>>T;
	double n[100];
	FOR(k,0,T){
		char ch[100];
		cin>>ch;
		int lc=strlen(ch);
		//string st=ch;
		bool f=true;
		int pos;
		for (pos=lc-2;pos>=0;--pos)
			if (ch[pos]<ch[pos+1]) {f=false;break;}

		if (f==false){



			int t=pos+1;
			for(int i=pos+2;i<lc;++i)
				if (ch[i]>ch[pos]&&ch[i]<ch[t]) t=i;
			char cc;
			cc=ch[t];
			ch[t]=ch[pos];
			ch[pos]=cc;
			qsort(ch+pos+1,lc-pos-1,sizeof(char),comp);
		}else{
			int t=0;
			for(int i=1;i<lc;++i)
				if (ch[i]>'0'&&ch[i]<ch[t]) t=i;
			char cc;
			cc=ch[t];
			ch[t]=ch[0];
			ch[0]=cc;
			
			ch[lc]='0';
			++lc;
			ch[lc]=0;

			qsort(ch+1,lc-1,sizeof(char),comp);
			

		}
		cout<<"Case #"<<k+1<<": ";
		
		cout<<ch<<endl;
	}
	return 0;

}