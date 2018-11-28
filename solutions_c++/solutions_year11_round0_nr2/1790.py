#include <iostream>
#include <cstdio>
#include <string>
#include <stack>
#include <vector>

using namespace std;
const int cntLet='Z'+10;
char res[cntLet][cntLet];
char s[30];
int opp[cntLet][cntLet];
int main () {
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0; t<T; t++) {
		for (int i='A'; i<='Z'; i++)
			for (int j='A'; j<='Z'; j++)
				res[i][j]=opp[i][j]=0;
		int k;
		cin>>k;
		for (int i=0; i<k; i++) {
			scanf("%s",s);
			res[s[0]][s[1]]=res[s[1]][s[0]]=s[2];
		}
		cin>>k;
		for (int i=0; i<k; i++) {
			scanf("%s",s);
			opp[s[0]][s[1]]=opp[s[1]][s[0]]=1;
		}
		cin>>k;
		char st[200];
		int sp=0;
		scanf("%s",s);
		for (int i=0; i<k; i++) {
			if (sp) {
				if (res[st[sp-1]][s[i]]) { 
					char add=res[st[sp-1]][s[i]];
					sp--;
					st[sp++]=add;
				} else {
					st[sp++]=s[i];
					for (int j=0; j<sp; j++) 
						if (opp[st[j]][s[i]]) {
							sp=0;
							break;
						}
				}
			} else st[sp++]=s[i];
		}
		cout<<"Case #"<<t+1<<": [";
		for (int i=0; i<sp; i++) {
			cout<<st[i];
			if (i!=sp-1) cout<<", ";
		}
		cout<<"]"<<endl;
	}
}