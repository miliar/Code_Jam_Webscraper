

#include <iostream>
#include <memory.h>
using namespace std;

int main()
{
	freopen("E://C-small-attempt1.in","r",stdin);
	freopen("E://yyy.txt","w",stdout);
	char ch[20]="welcome to code jam";
	int pre[256][4];
	for(int i=0;i<256;i++)pre[i][0]=-1;
	pre[int('w')][0]=0;pre[int('w')][1]=-1;
	pre[int('e')][0]=1;pre[int('e')][1]=6;pre[int('e')][2]=14;pre[int('e')][3]=-1;
	pre[int('l')][0]=2;pre[int('l')][1]=-1;
	pre[int('c')][0]=3;pre[int('c')][1]=11;pre[int('c')][2]=-1;
	pre[int('o')][0]=4;pre[int('o')][1]=9;pre[int('o')][2]=12;pre[int('o')][3]=-1;
	pre[int('m')][0]=5;pre[int('m')][1]=18;pre[int('m')][2]=-1;
	pre[int(' ')][0]=7;pre[int(' ')][1]=10;pre[int(' ')][2]=15;pre[int(' ')][3]=-1;
	pre[int('t')][0]=8;pre[int('t')][1]=-1;
	pre[int('d')][0]=13;pre[int('d')][1]=-1;
	pre[int('j')][0]=16;pre[int('j')][1]=-1;
	pre[int('a')][0]=17;pre[int('a')][1]=-1;
	int T,t=1;
	char ph[500];
	int a[19];
	cin>>T;
	cin.getline(ph,500);
	while(t<=T)
	{
		cin.getline(ph,500);
		memset(a,0,19*sizeof(int));
		for(int i=0;ph[i];i++)
		{
			if(ph[i]=='w'){
				a[0]++;
				continue;
			}
			for(int j=0;pre[int(ph[i])][j]!=-1;j++)
			{
				a[pre[int(ph[i])][j]]=(a[pre[int(ph[i])][j]]+a[pre[int(ph[i])][j]-1])%10000;
			}
		}
		cout<<"Case #"<<t<<": "<<a[18]/1000<<a[18]/100%10<<a[18]/10%10<<a[18]%10<<endl;
		t++;
	}
	return 0;
}