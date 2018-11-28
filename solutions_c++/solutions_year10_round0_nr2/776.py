#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<deque>
using namespace std;
string operator - (const string &a, const string &b)
{
	string res,a_,b_;
	a_=a;b_=b;
	int flag=0;
	res.resize(a.length());
	for (int i=a.length()-1;i>=0;i--)
		if (a_[i]-flag<b_[i])
		{
			res[i]=a_[i]-flag+10-b_[i]+'0';
			flag=1;
		}
		else
		{
			res[i]=a_[i]-flag-b_[i]+'0';
			flag=0;
		}
	return res;
}
int main()
{
 ifstream in("input.txt");
 ofstream out("output.txt");
 int T,test;
 in >> T;
 for (test=0;test<T;test++)
 {
	 int N;
	 vector<string> C;
	 in >> N;
	 int mN=0;
	 for (int i=0;i<N;i++)
	 {
		string tmp;
		in >> tmp;
		bool flag=true;
		for (int j=0;j<i-mN;j++)
			if (C[j]==tmp) {flag=false;break;}
		if (flag)
			C.push_back(tmp);
		else
			mN++;
	 }
	N-=mN;
	 int max_len=0;
	 int nul=0;
	 for (int i=0;i<N;i++)
		 if (C[i].length()>max_len) max_len=C[i].length();
	 for (int i=0;i<N;i++)
	 {	
		 int tmp=C[i].length();
		 for (int j=0;j<max_len-tmp;j++)
			 C[i]="0"+C[i];
	 }

	 sort(C.begin(),C.end());
	 string first=C[0];
	 			
	 vector<string>::iterator i=C.begin();
	 vector<string>::iterator i0=C.begin(); 
	 i++;
	 for (i;i!=C.end();i++)
		 *i=(*i)-(*i0);
	 for (int j=0;j+1<N;j++)
		 C[j]=C[j+1];
	 N--;
	 C.pop_back();
	 while (C[0]!="1" && C[0]!=C[N-1])
	 {
		 for (int i=1;i<N;i++)
			 C[i]=C[i]-C[0];
		 sort(C.begin(),C.end());
	 }
	 while (first>C[0]) first=first-C[0];
	 string res=C[0]-first;

	 out << "Case #" << test+1 << ": ";
	 int ii=0;
	 while (res[ii]=='0') ii++;
	 if (ii==res.length()) out << '0';
	 for (ii;ii<res.length();ii++)
		 out << res[ii];
	 out << endl;
 }
 return 0;
}