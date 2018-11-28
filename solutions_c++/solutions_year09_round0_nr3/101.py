#include<iostream>
#include<iomanip>
#include<string>
using namespace std;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int n;
	cin>>n;
	char m[20]="welcome to code jam";
	int r[20];
	char s[1000];
	cin.getline(s,1000);
	for(int i=0;i<n;i++){
		memset(r,0,sizeof(r));
		r[0]=1;
		cin.getline(s,1000);
		for(int j=0;j<strlen(s);j++){
			for(int k=0;k<19;k++){
				if(s[j]==m[k]){
					r[k+1]+=r[k];
					r[k+1]%=10000;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<setfill('0')<<setw(4)<<r[19]<<endl;
	}
	return 0;
}