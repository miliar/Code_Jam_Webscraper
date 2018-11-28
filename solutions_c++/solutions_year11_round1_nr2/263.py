#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k,m,n,p[10010],w;
int make[10010],y[27],ma,ans;
char s[10001][11],t[27];
bool hv[27];
const int mod=10000007;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int tcase;
	y[0]=1;
	for (i=1;i<=26;i++) y[i]=(y[i-1]*26)% mod;
	scanf("%d",&tcase);
	for (f=1;f<=tcase;f++){
		printf("Case #%d:",f);
		scanf("%d%d",&n,&m);
		gets(t);
		for (i=1;i<=n;i++)gets(s[i]);
	//  for (i=1;i<=n;i++) cout<<s[i]<<endl;
		for (g=1;g<=m;g++){
			gets(t);
			ma=-1;
			for (i=1;i<=n;i++){
				memset(make,0,sizeof(make));
				h=strlen(s[i]);
				//cout<<'#'<<h<<' '<<n<<' '<<s[i]<<endl;
				c=0;
				memset(hv,0,sizeof(hv));
				for (j=1;j<=n;j++) if (strlen(s[j])==h){
					c++;p[c]=j;
					for (k=0;k<h;k++) hv[s[j][k]-96]=1;
					}
				//for (j=1;j<=26;j++) printf("%d ",hv[j]);printf("\n");
				a=0;
				for (w=0;w<26;w++) if (hv[t[w]-96]){
					//for (j=1;j<=26;j++) printf("%d ",hv[j]);printf("\n");
	 				// cout<<"## "<<t[w]<<" ##"<<endl;
					for (j=1;j<=c;j++) {
						e=p[j];
						for (k=0;k<h;k++) if (s[e][k]==t[w])
						 	make[e]=make[e]+(1<<k);}
				//	printf("%d %d\n",make[2],make[3]);
					a++;
					for (k=0;k<h;k++) if (s[i][k]==t[w]){
						a--;break;}
					d=0;
					for (j=1;j<=c;j++) if (make[p[j]]==make[i]) {
						d++;p[d]=p[j];}
					c=d;
					if (c==1) {
					//	printf("%d %s %d\n",i,s[i],a);
						if (a>ma){
							ma=a;
							for (k=0;k<h;k++) ans=i;}
						break;}
					memset(hv,0,sizeof(hv));
					//for (j=1;j<=c;j++) printf("%d ",p[j]);printf("\n");
					for (j=1;j<=c;j++) for (k=0;k<h;k++) hv[s[p[j]][k]-96]=1;
				}
			}
			printf(" %s",s[ans]);
			}
		printf("\n");
	}
	return 0;
}



