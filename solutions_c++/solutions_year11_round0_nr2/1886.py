#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int c,d,n;
char s1[40][5],s2[40][5],s[105];

void solve() {
	char list[105],c1,c2;
	bool flag;
	int len=0;
	for (int i=0;s[i];i++) {
		list[len++]=s[i];
		if (len>=2) {
			c1=list[len-2];
			c2=list[len-1];
			for (int j=0;j<c;j++)
				if (s1[j][0]==c1&&s1[j][1]==c2||s1[j][1]==c1&&s1[j][0]==c2) {
					len--;
					list[len-1]=s1[j][2];
				}
		}
		if (len>=2) {
			c1=list[len-1];
			flag=false;
			for (int k=0;k<len-1;k++) {
				c2=list[k];
				for (int j=0;j<d;j++)
					if (s2[j][0]==c1&&s2[j][1]==c2||s2[j][1]==c1&&s2[j][0]==c2) {
						flag=true;
						break;
					}
				if (flag) break;
			}
			if (flag) len=0;
		}
	}
	cout<<"[";
	for (int i=0;i<len-1;i++)
		cout<<list[i]<<", ";
	if (len)
		cout<<list[len-1]<<"]"<<endl;
	else
		cout<<"]"<<endl;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>c;
		for (int i=0;i<c;i++) cin>>s1[i];
		cin>>d;
		for (int i=0;i<d;i++) cin>>s2[i];
		cin>>n;
		cin>>s;
		printf("Case #%d: ",++kase);
		solve();
	}
	return 0;
}
