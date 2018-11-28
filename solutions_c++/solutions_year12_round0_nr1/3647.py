#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
#define REP(i,b,n) for(int (i)=(b);(i)<(n);(i)++)
#define rep(i,n)   REP(i,0,n)

int pre()
{
	freopen("E:\\A.in","r",stdin);freopen("E:\\preOut.out","w",stdout);
	char alpha[26],google[26];
	char A[3][300],line[300];

	rep(i,3)gets(A[i]);
	rep(i,3){
		gets(line);
		for(int j=0;line[j]!=0;j++){
			alpha[A[i][j]-'a']=line[j];
			google[line[j]-'a']=A[i][j];
		}
	}
	rep(i,26)
		cout<<((alpha[i]>='a'&&alpha[i]<='z')?alpha[i]:' ');
	cout<<'\n';
	rep(i,26)
		cout<<((google[i]>='a'&&google[i]<='z')?google[i]:' ');
	
	fflush(stdout);
	return 0;
}

int main()
{
	freopen("E:\\My Document\\Downloads\\A-small-attempt0.in","r",stdin);freopen("E:\\A.out","w",stdout);
	char alpha[]="yhesocvxduiglbkrztnwjpfmaq";
	char line[101];
	int t;
	cin>>t;
	gets(line);

	rep(i,t){
		gets(line);
		for(int j=0;line[j]!=0;j++)
			if(isalpha(line[j]))line[j]=alpha[line[j]-'a'];
		printf("Case #%d: %s\n",i+1,line);
	}

	fflush(stdout);
	return 0;
}
