//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

bool f[200000];
char d[20000];
unsigned long long int r[200000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	unsigned long long int I=1,t,i,n;
	char num[500];
	for(cin>>t,fgetc(stdin);I<=t;I++) {
		memset(f,0,sizeof(f));
		gets(num);
		unsigned int b=0;
		for(i=0;num[i];i++) if(!f[num[i]]) {
				f[num[i]]=1;
				b++;
		}
		if(b<2) b=2;
		memset(d,-1,sizeof(d));
		int j=0;
		d[num[0]]=r[0]=1;
		for(i=1;num[i];i++) {
			if(j==1) j++;
			if(d[num[i]]>(-1)) r[i]=d[num[i]];
			else {
				r[i]=d[num[i]]=j;
				j++;
			}
		}
		unsigned long long ans=0;
		int k;
		for(k=0;num[k];k++) {
			ans=ans*b+r[k];
		}
		cout<<"Case #"<<I<<": "<<ans<<'\n';
	}
	return 0;
}
