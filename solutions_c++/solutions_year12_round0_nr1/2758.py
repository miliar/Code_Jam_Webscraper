#include <iostream>
//#include <fstream>
#include <string.h>
using namespace std;
//ifstream fin("A-small-attempt0.in");
//ofstream fout("A-small-attempt0.out");
int main() {
	char dic[27]="yhesocvxduiglbkrztnwjpfmaq";
	char G[128];
	int T=0, i=0, j=0;
	cin>>T;
	cin.get();
	for (i=1; i<=T; i++) {
		cin.getline(G, 128);
		for (j=strlen(G)-1; j>=0; j--)
			if (G[j]>='a' && G[j]<='z')
				G[j]=dic[G[j]-'a'];
		cout<<"Case #"<<i<<": "<<G<<endl;
	}
//	cin.close();
//	cout.close();
	return 0;
}
