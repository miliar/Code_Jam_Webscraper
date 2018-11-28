#include <iostream>
#include <string>
#include <vector>

using namespace std;
string needle = "welcome to code jam";
string hay;
int P[510][20];
int rec(int i,int j)
{
	if(j==0) return (hay[i]==needle[j]);
	if(P[i][j]!=-1) return P[i][j];
	P[i][j] = 0;
	if(hay[i]==needle[j])
	for(int k=0;k<i;k++) P[i][j]+=rec(k,j-1);
	return P[i][j]%10000;
}
int main()
{
	int N;
	scanf("%d\n",&N);
	int ctr = 0;
	while(N--)
	{
		for(int i=0;i<510;i++) for(int j=0;j<20;j++) P[i][j]=-1;
		char word[600];
		cin.getline(word,550);
		hay = word;
		int ans = 0;
		for(int i=0;i<hay.length();i++)
			ans += rec(i,needle.length()-1);
		printf("Case #%d: %.4d\n",++ctr,ans);
	}
}
