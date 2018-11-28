#include <iostream>
#include <vector>
#include <string>
using namespace std;

int el, d, n, cnt, out;
string s;
bool mode;
bool foi[5100];
bool aux[5100];
vector<string> in;

int main(){
	cin >> el >> d >> n;
	for(int i=0; i<d; i++){
		cin >> s;
		in.push_back(s);
	}
	for(int i=0; i<n; i++){
		cin >> s;
		cout << "Case #" << i+1 << ": "; //cout << endl;
		cnt=0; memset(foi, true, sizeof(foi)); out=d;
		for(int j=0; j<s.length() && out>0; j++){
			char c = s.at(j);
			if(c=='('){
				mode=true;
				memset(aux,false,sizeof(aux));
			}
			if(c==')'){
				mode=false;
				for(int k=0; k<d; k++){
					foi[k]=foi[k] && aux[k];
					if(!foi[k]) out--;
				}
				if(out>0) out=d;
			}
			if(c>='a' && c<='z'){
				for(int k=0; k<d;k++){
					if(foi[k]){
						if(mode) aux[k] = aux[k] || in[k].at(cnt) == c;
						else foi[k] = foi[k] && in[k].at(cnt) == c;
						//cout << c << ">[" << cnt << "]:" << in[k] << " " << (mode?aux[k]:foi[k]) << endl;
					}
				}
			}
			if(!mode) cnt++;
		}
		for(int j=0; j<d && out>0; j++)
			if(!foi[j]) out--;
		cout << out << endl;
	}
}