// Author : Team Heisenbug
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <cstring>

using namespace std;

#define F first
#define S second
#define mp make_pair
#define pb push_back
typedef vector<int> VI;
typedef vector<VI> VII;
typedef pair<int,int> PII;
typedef long long LL;
string translate = "abcdefghijklmnopqrstuvwxyz";
string new_trans = "yhesocvxduiglbkrztnwjpfmaq";
int main() {
	int T;
	scanf("%d",&T);
	for(int cno=1;cno<=T;cno++) {
		string temp;
		char c;
		if(cno == 1)
		scanf("%c",&c);
		getline(cin, temp);
		printf("Case #%d: ",cno);
		for(int i=0;i<temp.size();i++) {
			if(temp[i] != ' '){
				printf("%c",new_trans[temp[i]-'a']);
			}
			else {
				printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}


