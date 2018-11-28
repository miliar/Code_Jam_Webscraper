#include <iostream>
#include <string>

using namespace std;

int main(){
	int l,d,n;
	cin >> l >> d>>n;
	string a[5500];
	for(int i=0;i<d;i++)
		cin >> a[i];
	for(int i=1;i<=n;i++){
		string str;
		cin >> str;
		bool b[20][30];
		for(int x=0;x<20;x++) for(int y=0;y<30;y++) b[x][y] = false;
		int pos =0;
		for(int j=0;j<l;j++){
			if(str[pos]=='('){
				pos++;
				while(str[pos]!=')'){
					b[j][str[pos]-'a']=true;
					pos++;
				}
			}
			else{
				b[j][str[pos]-'a']=true;
			}
			pos++;
		}
		int cnt =0;
		for(int x=0;x<d;x++){
			bool ok = true;
			for(int y=0;y<l;y++)
				if(!b[y][a[x][y]-'a'])
					ok = false;
			if(ok) cnt++;
		}
printf("Case #%d: %d\n",i,cnt);
	}
	
	
	return 0;
}
