#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

int main () {
	int T;
	fstream cin("A-large.in");
	ofstream cout("output.txt");
	cin>>T;
	for (int run=1;run<=T;++run) {
		int n;
		cin>>n;
		int c1=0,c2=0,p1=1,p2=1;
		for (int i=0;i<n;++i) {
			string str;
			cin>>str;
			char ch = str[0];
			cin>>str;
			int button = atoi (str.c_str());
			//cout<<ch<<" "<<button<<endl;
			if (ch=='O') {
				if (c1<c2) {
					int t=c2-c1;
					int d = abs (button-p1);
					if (t>d)
						c1 = c2+1;
					else
						c1=c2+d-t+1;
					p1=button;
				}
				else {
					int d = abs(button-p1);
					c1+=d+1;
					p1=button;	
				}
			}
			else {
				if (c2<c1) {
					int t=c1-c2;
					int d = abs (button-p2);
					if (t>d)
						c2 = c1+1;
					else
						c2=c1+d-t+1;
					p2=button;
				}
				else {
					int d = abs(button-p2);
					c2+=d+1;
					p2=button;	
				}
			}
			//cout<<c1<<" "<<c2<<endl;
		}
		int res = max (c1,c2);
		cout<<"Case #"<<run<<": "<<res<<endl;
	}
}
