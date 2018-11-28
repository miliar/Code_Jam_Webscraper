#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
	int t,count1=1;
	string s;
	int a[123];
	for(int i=0; i<97; ++i){
		a[i]=0;
	}
	a[32]=32;
	a[97]=121;
	a[98]=104;
	a[99]=101;
	a[100]=115;
	a[101]=111;
	a[102]=99;
	a[103]=118;
	a[104]=120;
	a[105]=100;
	a[106]=117;
	a[107]=105;
	a[108]=103;
	a[109]=108;
	a[110]=98;
	a[111]=107;
	a[112]=114;
	a[113]=122;
	a[114]=116;
	a[115]=110;
	a[116]=119;
	a[117]=106;
	a[118]=112;
	a[119]=102;
	a[120]=109;
	a[121]=97;
	a[122]=113;

	cin>>t;
	cin.ignore();
	while(t--){
		getline(cin,s);
		int len=s.length();
		cout<<"Case #"<<count1<<": ";
		for(int i=0; i<len; ++i){
			cout<<(char)a[s[i]];
		}
		cout<<endl;
		count1++;
	}
	return 0;
}
