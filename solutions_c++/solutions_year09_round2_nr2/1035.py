#include <fstream>
#include <string>
#include <math.h>

using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
//ifstream fin("input.txt");
//ofstream fout("output.txt");
const int MNAX=1000;

void swap(char& x, char& y){
	int k=x;x=y;y=k;
}
void Qsort(string& a, int first, int last){
	int v, left=first, right=last;
	v=a[(left+right)/2];
	while (left<=right){
		while (a[left]<v) ++left;
		while (a[right]>v) --right;
		if (left<=right){
			swap(a[left],a[right]);
			++left; --right;
		}
	}
	if (first<right) Qsort(a,first,right);
	if (left<last) Qsort(a,left,last);
}

int main(){
	int test,t;
	fin>>test;

	for (t=1;t<=test;++t){
		string s,ans="";
		fin>>s;
		int len = s.length();
		int k=-1,i,j,iM=0,jM=0;
		for (i=0;i<len;++i){
			k=-1;
			for (j=i+1;j<len;++j){
				if (s[j]>s[i] && ((s[j]-48)<=k || k==-1)){
						k=s[j]-48;
						iM=i;
						jM=j;

			string ans1="";
			for (int ii=0;ii<iM;++ii){ans1+=s[ii];}
			ans1+=s[jM];
			string s2="";
			for (int ii=iM;ii<len;++ii){if (ii!=jM) s2+=s[ii];}
			Qsort(s2,0,s2.length()-1);
			ans1+=s2;
			if (ans1<ans || ans==""){ans=ans1;}


				}
			}
		}
		if (ans==""){
			Qsort(s,0,s.length()-1);
			ans+=s[0];
			ans+='0';
			for (i=1;i<s.length();++i){ans+=s[i];}
		}
		i=0;len=ans.length();
		while (i<len && ans[i]=='0'){++i;}
		if (i==len){
			ans="1";
			for (i=1;i<=len;++i){ans+='0';}
		}
		else{
			swap(ans[0],ans[i]);
		}

		

		fout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}