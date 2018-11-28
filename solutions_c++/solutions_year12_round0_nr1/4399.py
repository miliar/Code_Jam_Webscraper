#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const long long MNAX=100000;

const string ss = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	long long n,i,j;
	int test;
	cin>>test;
	getchar();
	
	for (int t=1;t<=test;++t){
		cout<<"Case #"<<t<<": ";
		
		char ch = '=';

		ch = getchar();
		while (ch != '\n'){
			//cin>>ch;
			if (ch!=' '){
				ch = ss[ch - 'a'];
			}

			cout<<ch;
			ch = getchar();
			
		}

		cout<<'\n';
	}

	return 0;
}