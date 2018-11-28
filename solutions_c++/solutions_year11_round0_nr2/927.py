#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int t;
int c,d,n;
string s;
char nw[30][30];
int bad[30][30];

void solve(int testcase){
	memset(nw,0,sizeof(nw));
	memset(bad,0,sizeof(bad));
	scanf("%d",&c);
	for (int i=0; i<c; i++){
		string cur;
		cin>>cur;
		nw[cur[0]-'A'][cur[1]-'A']=nw[cur[1]-'A'][cur[0]-'A']=cur[2]-'A';
	}
	scanf("%d",&d);
	for (int i=0; i<d; i++){
		string cur;
		cin>>cur;
		bad[cur[0]-'A'][cur[1]-'A']=bad[cur[1]-'A'][cur[0]-'A']=1;
	}
	scanf("%d",&n);
	cin>>s;
	string res="";
	res+=s[0];
	for (int i=1; i<s.length(); i++){
		if (res.length()==0) res+=s[i]; else
		{
			if (nw[res[(int)res.length()-1]-'A'][s[i]-'A'])
				res[(int)res.length()-1]=nw[res[(int)res.length()-1]-'A'][s[i]-'A']+'A'; else
				res+=s[i];
			for (int j=0; j<res.length(); j++)
				for (int k=j+1; k<res.length(); k++)
					if (bad[res[j]-'A'][res[k]-'A']) res="";
		}
	}

	printf("Case #%d: ",testcase);
	printf("[");
	for (int i=0; i<(int)(res.size())-1; i++)
		printf("%c, ",res[i]);
	if (res.length()>0) printf("%c",res[(int)res.length()-1]);
	printf("]\n");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);

	for (int i=1; i<=t; i++)
		solve(i);	

	return 0;
}