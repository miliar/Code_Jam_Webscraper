#include<cstdio>
const int L=15;
const int D=5000;
int l,d,n,b[L][26];
char a[D][L],ch;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for (int i=0;i<d;i++)
		scanf("%s",&a[i]);
	for (int i=0;i<n;i++){
		for (int j=0;j<l;j++)
			for (int k=0;k<26;k++)
				b[j][k]=0;
		getchar();
		for (int j=0;j<l;j++){
			ch=getchar();
			if (ch!='(')
				b[j][ch-'a']=1;
			else
				while ((ch=getchar())!=')')
					b[j][ch-'a']=1;
		}
		int ans=0;
		for (int j=0;j<d;j++){
			int flag=1;
			for (int k=0;k<l;k++)
				flag=flag && b[k][a[j][k]-'a'];
			ans+=flag;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
