#include<iostream>
#include<algorithm>
#define fo(i,u,d) for(int i=u;i<=d;i++)
#define fod(i,d,u) for(int i=d;i>=u;i--)
using namespace std;
int t1=1,tt;
long long n,nn;
int f[20],d[30];
char s[30];

int main(){
	freopen("bl.in","r",stdin);
	freopen("b.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%s\n",&s);
	//	cin>>n;nn=n;
	//	fo(i,1,9)f[i]=0;
	//	d[0]=0;
		d[0]=strlen(s);
		fo(i,1,d[0])
			d[d[0]-i+1]=s[i-1]-48;
	/*	while(n>0){
			d[++d[0]]=n%10;
			f[n%10]++;
			n/=10;
		}*/
		bool ok=true;
		fo(i,1,d[0]-1)
			if (d[i+1]<d[i]){ok=false;break;}
		printf("Case #%d: ",t1);
		if (ok){
			int t=1;
			if (d[1]==0)
				fo(i,2,d[0])
					if (d[i]>0){
						swap(d[1],d[i]);
						t=i;
						break;
					}
			fo(i,1,t)printf("%d",d[i]);
			printf("0");
			fo(i,t+1,d[0])printf("%d",d[i]);
		}
		else
		fo(i,1,d[0]-1)
			if (d[i+1]<d[i]){
				int t=i;
				fo(j,1,i)
					if ((d[j]>d[i+1])&&(d[j]<d[t]))
						t=j;
				swap(d[i+1],d[t]);
				sort(d+1,d+i+1);
				fod(j,d[0],i+1)printf("%d",d[j]);
				fo(j,1,i)printf("%d",d[j]);
				break; 
			}
		printf("\n");
	} 
	return 0;
}


			
			
				
			
	
	
