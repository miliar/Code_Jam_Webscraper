#include <string>
#include <iostream>
using namespace std;
const string com = "welcome to code jam";

int main(){
	int n;
	cin>>n;
	string s;
	int com_len = com.length();
	getline(cin,s);
	for(int f=1;f<=n;f++){
		getline(cin, s);
		//cout << s<< endl;
		int d[1000];
		int len = s.length();
		for(int i=0;i<1000;i++) d[i] = 0;
		d[0] = 1;
		for(int i=0;i<len;i++)
			for(int j=com_len-1;j>=0;j--)
				if(s[i] == com[j]){
					d[j+1]+=d[j];
					//printf("!!! %d %d %d %d\n", i, j, d[j+1], d[j]);
					if(d[j+1] >0) d[j+1] %= 10000;
				}
		printf("Case #%d: %04d\n",f,d[com_len]);
	}
	return 0;
}
