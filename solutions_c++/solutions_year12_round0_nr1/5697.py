#include<iostream>
#include<string>
#include<cstdio>
#include<map>
#include<algorithm>
#include<cmath>
#include<vector>
#include<sstream>
#include<stack>
#include<queue>
#include<cstring>

#define pb push_back
#define LL long long
#define OUTPUT_TO_FILE 1
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)


using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvyeqz";
	string r = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upaozq";
	map<char,char> m;
	map<char,int> m1;
	for(int i = 0;i < s.length();i++){
		m[s[i]] = r[i];
	}

	int t,t1;
	cin>>t;
	cin.ignore();
	t1 = 1;
	while(t1 <= t){
		getline(cin,s,'\n');
		cout<<"Case #"<<t1<<": ";
		r.resize(s.length());
		for(int i = 0;i < s.length(); i++){
			r[i] = m[s[i]];
		}
		cout<<r<<endl;
		t1++;
	}
	//system("pause");
}