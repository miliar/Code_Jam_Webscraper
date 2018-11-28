#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <ctime>
using namespace std;
char a[600];
char b[600][600];
int geth(char c){
	if (c<='Z'&&c>='A') return c-'A'+10;
	else return c-'0';
}
int main(){
	int n,m,i,j,t,test,T,count;
	int x,y,z,ok,p,q,size;
	double timer;
	clock_t c1,c2;
	c1=clock();
	scanf("%d",&T);
	for (test=1;test<=T;test++){
		printf("Case #%d: ",test);
	//	printf("\n");
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++){
			scanf("%s",a);
			for (j=0;j<m;j+=4){
				t=geth(a[j/4]);
				b[i][j]=(t&8)>>3;
				b[i][j+1]=(t&4)>>2;
				b[i][j+2]=(t&2)>>1;
				b[i][j+3]=t&1;
			}
		}
		size=0;
		int cc[600]={0};
	  int d[512][512]={0};
		for (i=0;i<n;i++){
			d[i][m-1]=1;
			for (j=m-1;j>=0;j--){
				if (b[i][j]!=b[i][j+1]) d[i][j]=d[i][j+1]+1;
				else d[i][j]=1;
			}
		}
		for (t=min(n,m);t>1;t--){
			for (i=0;i+t<=n;i++)
				for (j=0;j+t<=m;j++){
					ok=1;
					z=b[i][j];
					for (x=i;ok&&x<i+t;x++)
					if (d[x][j]<t) ok=0;
					else{
						p=(x-i)&1;
						if (z==0){
								if (p==0)		q=0;
								else q=1;
						}
						else {
							if (p==0) q=1;
							else q=0;
						} 
						if (b[x][j]!=q)		ok=0;
					}
					if (!ok) continue;
					cc[t]++;
					size+=t*t;
					for (x=i;x<i+t;x++){
						p=d[x][j];
						for (y=j-1;y>=0;y--)
						if (d[x][y]>p) d[x][y]-=p;
						else break;
						for (y=j;y<j+t;y++)
						d[x][y]=0;
					}
					}
		}
		cc[1]=n*m-size;
		vector<pair<int,int> > vv;
		for (i=min(n,m);i>=1;i--){
			if (cc[i]){
				vv.push_back(make_pair(i,cc[i]));
			}
		}
		n=vv.size();
		printf("%d\n",n);
		for (i=0;i<n;i++)
		printf("%d %d\n",vv[i].first,vv[i].second);
		c2=clock();
		timer=(double)(c2-c1)/CLOCKS_PER_SEC;
		timer/=test;
		fprintf(stderr,"%d/%d %.3lf\n",test,T,timer*(T-test));
	}
	fprintf(stderr,"%.3lf\n",double(c2-c1)/CLOCKS_PER_SEC);
  return 0;
}
