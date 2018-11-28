#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

char mas[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char s[120];

int main()
{
    //freopen("in.in","rt",stdin);
    //freopen("out.out","wt",stdout);

	int n;
	cin>>n;
	cin.getline(s, 101);
	for (int i=0;i<n;i++) {
		cin.getline(s, 101);
		string t="";
		for (int j=0;s[j]!=0;j++) {
			if (s[j]<'a'||s[j]>'z') {
				t+=s[j];
				continue;
			}
			int c=s[j]-'a';
			t+=mas[c];
		}
		printf("Case #%d: ",i+1);
		cout<<t;
		if (i!=n-1)
			cout<<endl;
	}
    return 0;
} 