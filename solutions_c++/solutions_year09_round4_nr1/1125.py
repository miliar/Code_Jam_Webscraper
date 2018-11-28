//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

struct mat{
	int col[100];
	int pos;
}tmp;
struct mat m[1000];
int k;
void swap(struct mat &a,struct mat &b) {
	k++;
	struct mat t;
	t=a;
	a=b;
	b=t;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A1.out","w",stdout);
	int I=1,t;
	
	int i,j,l,r,n;
	char c;
	int f;
		for(cin>>t;I<=t;I++) {
			memset(m,0,sizeof(m));
			cin>>n;
			for(i=1;i<=n;i++) {
				fgetc(stdin);
				for(j=1;j<=n;j++) {
					c=fgetc(stdin);
					m[i].col[j]=c-'0';
				}
				j=n;
				while(!m[i].col[j]) {
					j--;
				}
				m[i].pos=j;
			}
			//for(i=1;i<=n;i++) for(j=1;j<=n;j++) cout<<m[i].col[j];
			k=0;
			//cout<<' '<<k<<'\n';
			
			//do{
				//f=0;
			for(i=1;i<=n;i++) {
				if(m[i].pos>i) {
					//f=1;
					for(j=1;;j++) {
						//if((i-j)>0) if(m[i-j].pos<=i) {l=i-j;break;}
						if((i+j)<=n) if(m[i+j].pos<=i) {l=i+j;break;}
					}
					//cout<<i<<' '<<l<<' '<<k<<' '<<m[i].pos<<'\n';
					if(l>i) for(j=l;j>i;j--) swap(m[j],m[j-1]);
					else for(j=l;j<i;j++) swap(m[j],m[j+1]);
				}
				/*for(f=1;f<=n;f++) {
				for(r=1;r<=n;r++) cout<<m[f].col[r]<<' ';
				cout<<'\n';
			}*/
			}
			//}
			//while (f);
			
			printf("Case #%d: %d\n",I,k);
		}
	return 0;
}
