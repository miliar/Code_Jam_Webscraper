#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
int main()
{
	int i,j;
	int kase =1 ;
	int t;
	char str[100];
	char tmp[100];
	cin >> t;
	
	for(kase=1;kase <=t;kase++){
		cin >> str;
		int n = strlen(str);
		strcpy(tmp,str);
		next_permutation(str,str+n);
		sort(tmp,tmp+n);	
//		cout <<str<<endl;
		cout <<"Case #"<<kase <<": ";

		if(strcmp(str,tmp) ==0){
			sort(str,str+n);
			tmp[0] = str[0];
			tmp[1] = '0';
			strcpy(tmp+2,str+1);
			while(tmp[0] =='0')
				next_permutation(tmp,tmp+1+n);
			cout <<tmp <<endl;
		}
		else cout <<str <<endl;
		
	}

}
