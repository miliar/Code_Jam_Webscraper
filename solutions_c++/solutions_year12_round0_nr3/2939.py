#pragma warning(disable : 4786)
#include<stdio.h>
#include<string.h>
#include<map>
#include<algorithm>
using namespace std;

typedef pair<int, int> pii;
map<pii, int> M;
	pii ol;


char s[10],r[10],t[10];

void i2s(int d){
	int i=0,j;
	while(d>0){
		t[i++]=(d%10)+48;
		d/=10;
	}

	s[i]=0;
	j=0;

	for(i--;i>=0;i--)
	s[j++]=t[i];
}

int s2i(){
	int res=0,d,i;
	d=10;
	for(i=0;i<strlen(r);i++){
		res=res*d+r[i]-48;
	//	d*=10;
	}

	return res;
}


int main(){
//	freopen("ii.in", "r", stdin);
//	freopen("arif.out", "w", stdout);

	__int64 res;
	int t, cs, A,B,n,j,k,i,m,p;
	scanf("%d", &t);
	for(cs=1; cs<=t; cs++){
		res = 0;
		scanf("%d%d", &A, &B);
		M.clear();
		for(i=A; i<=B; i++){
			i2s(i);
			n=strlen(s);
			for(j=n-1; j>=1; j--){
				for(k=0;j+k<n;k++)
					r[k]=s[j+k];
				for(p=0;p<j;p++,k++)
					r[k]=s[p];
				r[n]=0;
				
				m=s2i();

				if(m>i){
					if(m<=B){
						
						ol =make_pair(i, m);
						if( M.find(ol) == M.end() ){
							M[ol]=res++;
						//	printf("%d -- %d\n",i,m);
						}
					}
				}
			}
		}
			printf("Case #%d: %I64d\n", cs, res);
	}
	return 0;
}