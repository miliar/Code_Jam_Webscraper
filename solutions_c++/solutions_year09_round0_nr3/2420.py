/**Author Nasini Madhava Rao**/
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
string sequence="welcome to code jam";
string input;
int dp[500][500];
void init(){
	inc(i,500)
		inc(j,500)
		dp[i][j] =-1;
}
int func(int index1,int index2){
	if(index1==sequence.size())
		return 1;
	if(index2==input.size())
		return 0;
	if(dp[index1][index2]!=-1)
		return dp[index1][index2];
	int ans=0;
	int maxVal=1000;
	for(int i=index2;i<input.size();i++){
		if(input[i]==sequence[index1]){
			ans+=func(index1+1,i+1);
			if(ans>=maxVal)
				ans%=maxVal;
		}
	}
	return dp[index1][index2]=ans;
}
int main(){

		int nt;
		cin>>nt;
		getchar();
		for(int i=1;i<=nt;i++){
			getline(cin,input);
			init();
			int val= func(0,0);
			char str[100];
			sprintf(str,"%d",val);
			string ans="";
			for(int j=0;j<4-strlen(str);j++)
				ans.pb('0');
			for(int j=0;j<strlen(str);j++){
				ans.pb(str[j]);
			}
			printf("Case #%d: ",i);
			fprintf(stdout,ans.c_str());
			printf("\n");
		}
return EXIT_SUCCESS;
}
