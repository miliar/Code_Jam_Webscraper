#include <fstream>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

/*ifstream fin("GCJ P B.in");
ofstream fout("GCJ P B.out");

#define cin fin
#define cout fout*/

char cmb[256][256];
bool clr[256][256];

string buf;
int n;

void init(){
	int cbn,cln;
	char st,ed,rel,b;
	cin >> cbn;
	for(int i=0;i<cbn;i++){
		cin >> st >> ed >> rel;
		cmb[st][ed]=cmb[ed][st]=rel;
	}
	cin >> cln;
	for(int i=0;i<cln;i++){
		cin >> st >> ed;
		clr[st][ed]=clr[ed][st]=true;
	}
	cin >> n;
	cin.get(b);
	getline(cin,buf);
}

void process(){
	for(int i=1;i<n;i++){
		if(cmb[ buf[i] ][ buf[i-1] ]){
			buf[i-1]=cmb[ buf[i] ][ buf[i-1] ];
			buf.erase(i,1);
			--i;
			--n;
		}
		for(int j=0;j<i;j++){
			if(clr[ buf[i] ][ buf[j] ]){
				buf.erase(0,i+1);
				n-=i+1;
				i=0;
				break;
			}
		}
	}
	cout << '[';
	for(int i=0;i<n-1;i++)
		cout << buf[i] << ", ";
	if(n)
		cout << buf[n-1];
	cout << ']' << endl;
}

int main(){
	int tn;
	cin >> tn;
	for(int i=0;i<tn;i++){
		memset(cmb,0,sizeof(cmb));
		memset(clr,0,sizeof(clr));
		init();
		cout << "Case #" << i+1 << ": ";
		process();
	}
	return 0;
}