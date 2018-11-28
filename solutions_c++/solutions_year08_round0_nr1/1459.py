#include <iostream>
#include <string>
#include <string.h>
using namespace std;
int ty[400];



int main(){

	freopen("A-large.in","r",stdin);
	freopen("1o.txt","w",stdout);
	
	int n,i,j,k,l,s,q,sq[100],en,re,ap;
	string sn[100],qn;
	char ch;
	
	scanf("%d\n",&n);
	for(k=0;k<n;++k){
		
		scanf("%d\n",&s);
		for(i=0;i<s;++i){
//			sn[i]="";
//			scanf("%c",&ch);
//			while (ch!=10){
//				sn[i]=sn[i]+ch;
//				scanf("%c",&ch);
//			}
			getline(cin,sn[i]);
		}
		scanf("%d\n",&q);
		en=-1;
		re=0;
		ap=0;
		for(i=0;i<s;++i) sq[i]=-1;
		for(i=0;i<q;++i){
//			qn="";
//			scanf("%c\n",&ch);
//			while (ch!=10){
//				qn=qn+ch;
//				scanf("%c",&ch);
//			}
			getline(cin,qn);

			for(j=0;j<s;++j)
				if (!strcmp(sn[j].c_str(),qn.c_str())){
					if (sq[j]<=en) {++ap;sq[j]=i;}
					if (ap==s){
						for(l=0;l<s;++l)
							if (en<sq[l]) en=sq[l]-1;
						++re;
						ap=1;
					}
				}
		}
		cout<<"Case #"<<k+1<<": "<<re<<endl;
	}

	return 0;

}