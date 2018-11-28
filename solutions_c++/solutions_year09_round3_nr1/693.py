#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define SZ(c) (c).size()
typedef vector<int> VI;


int main(){
	FILE *in;
	in= fopen("A-small-attempt0.in","rt");
	freopen("x.out", "w+", stdout);
	int T=0;
	int i,p,d;
	char ch;
	VI num(62);
	VI alpha(256,-1);
	for(ch=fgetc(in);ch!='\n';T=T*10+ch-'0',ch=fgetc(in));
	REP(t, T){
		cout<<"Case #"<<(t+1)<<": ";
		for(i=0,ch=fgetc(in);ch!='\n'&&ch!=EOF;num[i]=ch,ch=fgetc(in),i++);
		REP(o,SZ(alpha))
			alpha[o]=-1;
		alpha[num[0]]=1;
		num[0]=1;
		for(p=1;p<SZ(num)&&alpha[num[p]]==1;num[p]=1,p++);
		alpha[num[p]]=0;
		num[p]=0;
		int numeric=2;
		FOR(o,p+1,i){
			if (alpha[num[o]]<0) 
			{
				alpha[num[o]]=numeric;
				numeric++;
			}
			num[o]=alpha[num[o]];
		}
		VI res(19,0);
		VI mnoj(19,0);
		VI mnojres(19,0);
		mnoj[18]=1;
		for(int o=i-1;o>=0;o--){
			REP(l,19)
				mnojres[l]=0;
			d=0;
			for(int k=18;k>=0;k--){
				mnojres[k]=(num[o]*mnoj[k]+d)%10;
				d=(num[o]*mnoj[k]+d)/10;
			}
			d=0;
			for(int k=18;k>=0;k--){
				p=(res[k]+mnojres[k]+d)/10;
				res[k]=(res[k]+mnojres[k]+d)%10;
				d=p;
			}
			d=0;
			for(int k=18;k>=0;k--){
				p=(numeric*mnoj[k]+d)/10;
				mnoj[k]=(numeric*mnoj[k]+d)%10;
				d=p;
			}
		}
		p=0;
		while(res[p]==0)p++;
		FOR(k,p,19)cout<<res[k];
		cout<<endl;
	}
	return 0;
}
