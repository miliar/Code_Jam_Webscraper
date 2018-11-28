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

const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);

int pos[128];
int npos[128];

int comp(const void *a,const void *b)
{
	return *(int*)a-*(int*)b;
} 



int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	

	int T;
	cin>>T;

	FOR(k,0,T){

		char ch[1000];
		cin>>ch;
		int le=strlen(ch);
		zero(pos);
		zero(npos);
		int cur=int(ch[0]);
		int max=0;
		for(int i=le-1;i>=0;--i){
			int temp=ch[i];
			if (pos[temp]==0) ++max;
			pos[temp]=i+1;
			

		}
		
		
		npos[cur]=1;

		for(int j=1;j<max;++j){
			int s=255;
			int ccur;
			for(int i=0;i<128;++i)
				if (pos[i]>pos[cur]&&pos[i]<s) {s=pos[i];ccur=i;}
			if (j==1) npos[ccur]=0;
			else npos[ccur]=j;
			cur=ccur;
			
		}
		if (max==1) max=2;
		unsigned long long  ans=0;
		unsigned long long  we=1;
		for(int i=le-1;i>=0;--i){
			int temp=ch[i];
			ans+=npos[temp]*we;
			we*=max;
		
		}		
		cout<<"Case #"<<k+1<<": "<<ans;

		cout<<endl;
	}
	return 0;

}