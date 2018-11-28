#include <iostream>
#include <string>

using namespace std;

int main(){
	int h;
	cin >>h;
	string s;
	for(int f=1;f<=h;f++){
		cin >> s;
		int len = s.length();
		int c[200];
		for(int i=0;i<200;i++) c[i]=0;
		int base =0;
		for(int i=0;i<len;i++){
			if(c[s[i]] ==0){
				base++;
				c[s[i]] = -1;
			}
		}
		if(base < 2) base = 2;
		long long ans = 0;
		int count =0;
		for(int i=0;i<len;i++){
			if(c[s[i]]==-1){
				if(count ==0) c[s[i]]=1;
				else if(count == 1) c[s[i]] = 0;
				else c[s[i]] = count;
				count++;
			}
			ans *= base;
			ans += c[s[i]];
		}
printf("Case #%d: ", f);
cout << ans << endl;
	}
	return 0;
}
