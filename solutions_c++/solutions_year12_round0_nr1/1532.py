#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>

using namespace std;

char tr[]="yhesocvxduiglbkrztnwjpfmaq";

int main() {
	
	int n;
	
	cin>>n;
	int k=0;
	string str;
	getline(cin, str);
	
	while (k<n) {
		
		getline(cin, str);
		for (int i=0;i<str.length();++i) {
			if (str[i]<=' ') { 
				continue;
			}
			str[i]=tr[str[i]-'a'];
		}
		k++;
		cout<<"Case #"<<k<<": "<<str<<endl;
		
	}
	
	
	return 0;
}

