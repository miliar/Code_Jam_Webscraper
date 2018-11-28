#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <map>

//#define DEBUG

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("Bout.txt", "w", stdout);

	int t, n, s, p, tcase;
	cin>>t;
	for (tcase=1; tcase<=t; tcase++){
		int count = 0;
		cin>>n>>s>>p;
		int thrH, thrL;
		thrH = p*3-2;
		thrL = thrH-2;
		if (p==1){
			thrL = thrH;
		}

		while(n--){
			int sc;
			cin>>sc;
			if(sc >= thrH){
				++count;
				continue;
			}
			if(sc >= thrL && s!=0){
				++count;
				--s;
				continue;
			}
		}
		cout<<"Case #"<<tcase<<": "<<count<<endl;
	}

	return 0;
}