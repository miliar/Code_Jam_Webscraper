#include "stdio.h"
#include "iostream"
#include "string.h"
#include "math.h"
#include "string"
#include "vector"
#include "set"
#include "map"
#include "queue"
#include "list"
#include "stack"

using namespace std;

const char aim[25]="welcome to code jam";
char str[800];
const int mod=10000;
int num[600][20];
int len;
void deal(int pos)
{
	int i;
	switch(str[pos]){
		case 'm':
			num[pos][18]=1;
			for(i=pos+1;i<len;i++){
				if(str[i]=='e')
					num[pos][5]=(num[pos][5]+num[i][6])%mod;
			}
			break;
		case 'c':
			for(i=pos+1;i<len;i++){
				if(str[i]=='o'){
					num[pos][11]=(num[pos][11]+num[i][12])%mod;
					num[pos][3]=(num[pos][3]+num[i][4])%mod;
				}
			}
			break;
		case 'e':
			for(i=pos+1;i<len;i++){
				if(str[i]=='l')
					num[pos][1]=(num[pos][1]+num[i][2])%mod;
			}
			for(i=pos+1;i<len;i++){
				if(str[i]==' '){
					num[pos][6]=(num[pos][6]+num[i][7])%mod;
					num[pos][14]=(num[pos][14]+num[i][15])%mod;
				}
			}
			break;
		case 'o':
			for(i=pos+1;i<len;i++){
				if(str[i]=='m')
					num[pos][4]=(num[pos][4]+num[i][5])%mod;
			}
			for(i=pos+1;i<len;i++){
				if(str[i]==' ')
					num[pos][9]=(num[pos][9]+num[i][10])%mod;
			}
			for(i=pos+1;i<len;i++){
				if(str[i]=='d')
					num[pos][12]=(num[pos][12]+num[i][13])%mod;
			}
			break;
		case ' ':
			for(i=pos+1;i<len;i++){
				if(str[i]=='t')
					num[pos][7]=(num[pos][7]+num[i][8])%mod;
			}
			for(i=pos+1;i<len;i++){
				if(str[i]=='c')
					num[pos][10]=(num[pos][10]+num[i][11])%mod;
			}
			for(i=pos+1;i<len;i++){
				if(str[i]=='j')
					num[pos][15]=(num[pos][15]+num[i][16])%mod;
			}
			break;
		case 'w':
			for(i=pos+1;i<len;i++){
				if(str[i]=='e')
					num[pos][0]=(num[pos][0]+num[i][1])%mod;
			}
			break;
		case 'l':
			for(i=pos+1;i<len;i++){
				if(str[i]=='c')
					num[pos][2]=(num[pos][2]+num[i][3])%mod;
			}
			break;
		case 't':
			for(i=pos+1;i<len;i++){
				if(str[i]=='o')
					num[pos][8]=(num[pos][8]+num[i][9])%mod;
			}
			break;
		case 'd':
			for(i=pos+1;i<len;i++){
				if(str[i]=='e')
					num[pos][13]=(num[pos][13]+num[i][14])%mod;
			}
			break;
		case 'j':
			for(i=pos+1;i<len;i++){
				if(str[i]=='a')
					num[pos][16]=(num[pos][16]+num[i][17])%mod;
			}
			break;
		case 'a':
			for(i=pos+1;i<len;i++){
				if(str[i]=='m')
					num[pos][17]=(num[pos][17]+num[i][18])%mod;
			}
			break;
	}
}
void solve()
{
	int i,j;
	for(i=0;i<600;i++){
		for(j=0;j<20;j++)
			num[i][j]=0;
	}
	len=strlen(str);
	for(i=len-1;i>=0;i--){
		deal(i);
	}
	int cnt=0;
	for(i=0;i<len;i++){
		if(str[i]=='w') cnt+=num[i][0];
	}
	string ans="";
	cnt%=mod;
	if(cnt<10)
		ans="000";
	else if(cnt<100)
		ans+="00";
	else if(cnt<1000)
		ans+="0";
	cout<<ans<<cnt<<endl;
}
int main()
{
	int cs;
	cin>>cs;
	freopen("out.txt","w",stdout);
	cin.getline(str,800,'\n');
	for(int ii=1;ii<=cs;ii++){
		cout<<"Case #"<<ii<<": ";
		cin.getline(str,800,'\n');
		solve();
	}
}