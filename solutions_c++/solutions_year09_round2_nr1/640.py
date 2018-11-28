#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <set>
using namespace std;
double d[100000];
string s[100000];
int q[100000];
int main(){
	int h;
	cin >> h;
	string str;
	for(int f=1;f<=h;f++){
		int l;
		cin >> l;
		getline(cin, str);
		char c;
		int mode =0;
		int node = 0;
		int st=0;
		string tmp;
		q[st]=1;
		for(int i=0;i<100000;i++) {d[i] = -1; s[i] = "";}
		for(int i=0;i<l;i++){
			getline(cin, str);
			istringstream ss(str);
			while(true){
				if(mode == 0){
					if(ss >> c){
						if(c=='(') {mode=1; node = node*2+q[st]%2; st++; q[st]=0;} 
						else if(c==')'){node = node /2; q[st]++; st--; q[st]++;}
						else { if(!(ss >>tmp)) tmp = ""; tmp = tmp.insert(0,1,c); s[node] = tmp;}
					} else break;
				}else if(mode ==1){
					if(ss >> d[node])
						mode =0;
					else break;
				}
			}
		}
/*
		for(int i=0;i<10;i++){
printf("%d: %lf %s\n",i,d[i],s[i].c_str());
		}
	*/	
printf("Case #%d:\n", f);
		cin >> l;
		for(int i=0;i<l;i++){
			cin >> str;
			int n;
			string fea[104];
			cin >> n;
			for(int j=1;j<=n;j++)
				cin >> fea[j];
			fea[0] = str;
			int cur=1;
			bool have;
			double p =1;
			while(d[cur]>-0.5){
				p*=d[cur];
				have = false;
				for(int j=0;j<=n;j++)
					if(s[cur] == fea[j]){
						have = true;
						break;
					}
				cur*=2;
				if(!have) cur++;
			}
			printf("%.9lf\n",p);
//printf("%I64f\n",p);
			//cout << p <<endl;
		}

	}
	return 0;
}
