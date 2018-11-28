#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <deque>
#include <set>
using namespace std;

int res (string s)
{
	int i,kol1=0,kol2=0,kol3=0;
	for (i=0; i<4; i++)
		if (s.at(i)=='X') kol1++;
		else if (s.at(i)=='O') kol2++;
		else if (s.at(i)=='T') kol3++;
	if (kol1+kol3==4 && kol2==0) return 1;
	if (kol2+kol3==4 && kol1==0) return 2;
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin); freopen("output.txt","w",stdout);
	int i,j,n;
	bool flag;
	string s1,s2,s3,s4,s;
	cin>>n;
	for (i=1; i<=n; i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>s1>>s2>>s3>>s4;
		s.clear();
		if (res(s1)==2 || res(s2)==2 || res(s3)==2 || res(s4)==2)
		{
			cout<<"O won"<<endl;
			continue;
		}
		if (res(s1)==1 || res(s2)==1 || res(s3)==1 || res(s4)==1)
		{
			cout<<"X won"<<endl;
			continue;
		}
		s+=s1.at(0); s+=s2.at(0); s+=s3.at(0); s+=s4.at(0); 
		//cout<<s<<endl;
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s.clear(); s+=s1.at(1); s+=s2.at(1); s+=s3.at(1); s+=s4.at(1); 
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s.clear(); s+=s1.at(2); s+=s2.at(2); s+=s3.at(2); s+=s4.at(2); 
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s.clear(); s+=s1.at(3); s+=s2.at(3); s+=s3.at(3); s+=s4.at(3); 
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s.clear(); s+=s1.at(0); s+=s2.at(1); s+=s3.at(2); s+=s4.at(3); 
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s.clear(); s+=s1.at(3); s+=s2.at(2); s+=s3.at(1); s+=s4.at(0); 
		if (res(s)==1) {cout<<"X won"<<endl; continue;} else if (res(s)==2) {cout<<"O won"<<endl; continue;}
		s=s1+s2+s3+s4;
		flag=0;
		for (j=0; j<s.size(); j++)
			if (s.at(j)=='.') {flag=1; break;}
		if (flag) cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	}
	return 0;
}