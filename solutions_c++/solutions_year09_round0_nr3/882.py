#include <iostream>
#include <string>
using namespace std;
#define mod 10000

string text;
char txt[512];
string key = "welcome to code jam";

int dp[32],dp2[32],n;
int main(){
	int cas,idx;
	cin.getline(txt,512);
	sscanf(txt,"%d",&cas);
	idx=0;
	while(cas--){
		idx++;
		cin.getline(txt,512);
		text = string(txt);
		n = text.size();
		int i,j;
		for(i=0;i<19;i++)
			dp[i]=0;
		dp[i]=1;
		for(i=n-1;i>=0;i--){
			for(j=0;j<20;j++){
				dp2[j]=dp[j];
				if(j<19 && text[i]==key[j])
					dp2[j]+=dp[j+1];
				dp2[j] %= mod;
			}
			memcpy(dp,dp2,sizeof dp);
		}
		char rem[5];int ans = dp[0];rem[4]=0;
		for(i=3;i>=0;i--){
			rem[i]=ans%10+'0';ans/=10;
		}
		cout << "Case #"<<idx << ": " << string(rem,rem+4) << endl;
	}
	return 0;
}
