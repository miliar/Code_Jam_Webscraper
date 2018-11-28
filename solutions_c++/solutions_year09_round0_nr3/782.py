#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	int t,num=0,s[20];
	scanf("%d",&t);
	getchar();
	char a[1000];
	while(t--) {
		memset(s,0,sizeof(s));	
		cin.getline(a,1000,'\n');
		int l=strlen(a),i;
		for(i=0;i<l;i++) {
			if(a[i]=='w') {
				s[0]++;
			}
			else if(a[i]=='e') {
				s[1]+=s[0];
				if(s[1]>=10000) s[1]-=10000;
				s[6]+=s[5];
				if(s[6]>=10000) s[6]-=10000;
				s[14]+=s[13];
				if(s[14]>=10000) s[14]-=10000;
			}
			else if(a[i]=='l') {
				s[2]+=s[1];
				if(s[2]>=10000) s[2]-=10000;
			}
			else if(a[i]=='c') {
				s[3]+=s[2];
				if(s[3]>=10000) s[3]-=10000;
				s[11]+=s[10];
				if(s[11]>=10000) s[11]-=10000;
			}
			else if(a[i]=='o') {
				s[4]+=s[3];
				if(s[4]>=10000) s[4]-=10000;
				s[9]+=s[8];
				if(s[9]>=10000) s[9]-=10000;
				s[12]+=s[11];
				if(s[12]>=10000) s[12]-=10000;
			}
			else if(a[i]=='m') {
				s[5]+=s[4];
				if(s[5]>=10000) s[5]-=10000;
				s[18]+=s[17];
				if(s[18]>=10000) s[18]-=10000;
			}
			else if(a[i]==' ') {
				s[7]+=s[6];
				if(s[7]>=10000) s[7]-=10000;
				s[10]+=s[9];
				if(s[10]>=10000) s[10]-=10000;
				s[15]+=s[14];
				if(s[15]>=10000) s[15]-=10000;
			}
			else if(a[i]=='t') {
				s[8]+=s[7];
				if(s[8]>=10000) s[8]-=10000;
			}
			else if(a[i]=='d') {
				s[13]+=s[12];
				if(s[13]>=10000) s[13]-=10000;
			}
			else if(a[i]=='j') {
				s[16]+=s[15];
				if(s[16]>=10000) s[16]-=10000;
			}
			else if(a[i]=='a') {
				s[17]+=s[16];
				if(s[17]>=10000) s[17]-=10000;
			}
		}
		printf("Case #%d: %04d\n",++num,s[18]);
	}
	return 0;
}