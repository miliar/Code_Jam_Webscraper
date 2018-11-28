#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;

int a[26] = {121, 104, 101, 115, 111, 99, 118, 120, 100, 117, 105, 103, 108, 98, 107, 114, 'z',
 116, 110, 119, 106, 112, 102, 109, 97, 'q'};

int main()
{
	int n, c=1;
	cin >> n;
	getchar();
	while(n--)
	{
		string s;
		getline(cin, s);
		for(int i=0; i<s.size(); i++)
			if(s[i]!=' ')
				s[i]=a[s[i]-'a'];
		printf("Case #%d: ", c++);
		cout << s << endl;
	}
}
