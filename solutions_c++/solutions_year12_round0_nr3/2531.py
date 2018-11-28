#include <cstdio>
#include <iostream>
#include <sstream>

using namespace std;

void rotate(string &str) {	
	if(str.size() == 0)
		return;
	
	char ch = str[str.size()-1];
	str.erase(str.end()-1);
	str.insert(str.begin(), ch);
}

int getnum(string &str) {
	int factor = 1;
	int num = 0;
	for(string::reverse_iterator it = str.rbegin(); it != str.rend(); it++) {
		num += ((*it)-'0')*factor;
		factor*=10;
	}
	return num;
}

void tostring(string &str, int num) {
	while(num > 0) {
		str.insert(0, 1, num%10+'0');
		num /= 10;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	
	for(int t=0; t!=T; t++) {
		
		long long int count = 0;
		
		int A, B;
		scanf("%d %d", &A, &B);
		//printf("read\n");
		
		for(int i=A; i<=B; i++) {
			//if(i%10000 == 0)
				//printf("%d\n", i);
			
			//stringstream ss1;
			//ss1 << i;
			string str;
			tostring(str, i);
			//ss1 >> str;
			//break;
			while(true) {
				rotate(str);
				int num = getnum(str);
				//cout << "str:" << str << ", num:" << num << endl;
				//stringstream ss;
				//ss << str;
				//ss >> num;
				
				//break;
				
				if(num == i)
					break;
				
				if(num > i && num <= B)
					count++;
			}
		}
		
		printf("Case #%d: %lld\n", t+1, count);
		
	}
}
