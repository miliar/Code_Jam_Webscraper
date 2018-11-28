#include <iostream>

using namespace std;

string str;
int n;
string utama="welcome to code jam";
int dp[505][19];

int main(){
	int i,j,ii;
	char dumi;
	
	scanf("%d%c",&n,&dumi);
	for (ii=0;ii<n;ii++){
		memset(dp,0,sizeof(dp));
		getline(cin,str);
		if (str[0]=='w') dp[0][0]=1;
		for (i=1;i<str.length();i++){
			dp[i][0]=dp[i-1][0];
			if (str[i]=='w') dp[i][0]++;
			dp[i][0]%=10000;
			for (j=1;j<=min(i,(int)utama.length()-1);j++){
				dp[i][j]=dp[i-1][j];
				if (str[i]==utama[j])
					dp[i][j]+=dp[i-1][j-1];
				dp[i][j]%=10000;
			}
		}
		/*for (i=0;i<str.length();i++){
			for (j=0;j<utama.length();j++){
				cout << dp[i][j] << ' ' ;	
			}	
			cout << endl;
		}*/
		printf("Case #%d: ",ii+1);
		//cout << dp[str.length()-1][utama.length()-1] << endl;
		string out="";
		while (dp[str.length()-1][utama.length()-1] > 0){
			out=char(dp[str.length()-1][utama.length()-1]%10+48) + out;
			dp[str.length()-1][utama.length()-1]/=10;
		}
		
		while (out.length()<4){
			out = '0' + out;	
		}
		
		cout << out << endl;
	}
	
	return 0;	
}
