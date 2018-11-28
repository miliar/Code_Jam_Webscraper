#include <iostream>
#include <string>
using namespace std;
int main(){
	int h;
	cin >> h;
	string s;
	getline(cin,s);
	for(int f=1;f<=h;f++){
		getline(cin,s);
		int len = s.length();
		len--;
		int a[10];
		for(int i=0;i<10;i++) a[i]=0;
		int max = s[len] - '0';
		int last = max;
		a[max]++;
		len--;
		while(len>=0){
			last = s[len] - '0';
			len--;
			a[last]++;
			if(last > max) {max = last;}
			else if(last < max){
				break;
			}
		}
		char c[25];
		int clen = 0;
		if(last < max){
			for(int i=0;i<=len;i++,clen++){
				c[clen] = s[i];
			}
			for(int i=last+1;i<10;i++)
				if(a[i] >0){
					c[clen]=i+'0';
					clen++;
					a[i]--;
					break;
				}
		}
		else{// add 0
			for(int i=1;i<10;i++)
				if(a[i] >0){
					c[clen]=i+'0';
					clen++;
					a[i]--;
					break;
				}
			a[0]++;
		}
		for(int i=0;i<10;i++)
			while(a[i]>0){
				c[clen]=i+'0';
				clen++;
				a[i]--;
			}
		c[clen]='\0';
		printf("Case #%d: %s\n",f,c);
	}
	
}
