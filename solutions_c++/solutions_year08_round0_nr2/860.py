#include <iostream>
#include <string>
#define N 300
using namespace std;

int test;
int t;
int na,nb;
int abi[N],abo[N];
int bai[N],bao[N];
int f[N][2];
int cnt[2];
string s;


int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%i",&test);
	for (int z=1;z<=test;z++){
		printf("Case #%i: ",z);
		scanf("%i",&t);
		scanf("%i %i",&na,&nb);
		cnt[0]=cnt[1]=0;
		memset(f,0,sizeof(f));
		memset(abi,0,sizeof(abi));
		memset(abo,0,sizeof(abo));
		memset(bai,0,sizeof(bai));
		memset(bao,0,sizeof(bao));
		for (int i=0;i<na;i++){
			cin>>s;
			abi[i]=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			cin>>s;
			abo[i]=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
		}
		for (int i=0;i<nb;i++){
			cin>>s;
			bai[i]=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			cin>>s;
			bao[i]=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
		}
		int lef=0;
		int rig=0;
		

		for (int i=0;i<na;i++)
			for (int j=i+1;j<na;j++)
				if (abi[i]>abi[j] || (abi[i]==abi[j] && abo[i]>abo[j])){
					swap(abi[i],abi[j]);
					swap(abo[i],abo[j]);
				}
		for (int i=0;i<nb;i++)
			for (int j=i+1;j<nb;j++)
				if (bai[i]>bai[j] || (bai[i]==bai[j] && bao[i]>bao[j])){
					swap(bai[i],bai[j]);
					swap(bao[i],bao[j]);
				}
		int i=0;
		int j=0;
		//for (int i=0;i<na;i++) printf("%i %i  -  %i %i\n",abi[i]/60,abi[i]%60,abo[i]/60,abo[i]%60);
		//for (int i=0;i<nb;i++) printf("%i %i  -  %i %i\n",bai[i]/60,bai[i]%60,bao[i]/60,bao[i]%60);

		
		while (i<na || j<nb){
			int cur=(int)1e9;
			int pos=-1;
			if (i<na && cur>abi[i]){
				cur=abi[i];
				pos=1;
			}
			if (j<nb && cur>bai[j]){
				cur=bai[j];
				pos=2;
			}
			for (int k=0;k<i;k++)
				if (abo[k]+t<=cur && !f[k][0]){
					cnt[1]++;
					f[k][0]=1;
				}
			for (int k=0;k<j;k++)
				if (bao[k]+t<=cur && !f[k][1]){
					cnt[0]++;
					f[k][1]=1;
				}
			if (pos==1){
				i++;
				if (!cnt[0]) lef++;
				else cnt[0]--;
			}else{
				j++;
				if (!cnt[1]) rig++;
				else cnt[1]--;
			}
		}
		printf("%i %i\n",lef,rig);
	}

	return 0;
}
