#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		int m;
		cin>>m;
		int op=1,os=0,bp=1,bs=0,now=0;
		for(int i=0;i<m;i++){
			string a;int b;
			cin>>a>>b;
			if(a[0]=='O'){
				now=max(os+abs(b-op),bs)+1;
				op=b;os=now;
			}else{
				now=max(bs+abs(b-bp),os)+1;
				bp=b;bs=now;
			}
		}
		cout<<"Case #"<<x<<": "<<now<<endl;
	}
}