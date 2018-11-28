#include <stdio.h>
#include <string>

using namespace std;

const string TARGET = "welcome to code jam";

int ans(string str, string target){
	if(target.empty())
		return 1;	
	int ret;
	ret = 0;
	for(int i=0; i<str.length(); i++)
		if(str[i] == target[0])
			ret += ans(str.substr(i+1), target.substr(1));
	return ret;
}

int main(){
	int n;
	scanf("%d", &n);
	getchar();
	for(int i=0; i<n; i++){
		char str[512];
		gets(str);
		int out;
		out = ans(str, TARGET)%10000;
		printf("Case #%d: ", i+1);
		if(out < 10)
			printf("000");
		else if(out < 100)
			printf("00");
		else if(out < 1000)
			printf("0");
		printf("%d\n", out);
	}
	return 0;
}
