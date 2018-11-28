#include<iostream>
#include<string>
using namespace std;
int T,n;
string S;
char s[40];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for (int t=1;t<=T;t++){
		cin>>S;
		S='0'+S;
		n=S.size();
		for (int i=0;i<n;i++)
			s[i]=S[i];
		for (int i=n-1;i>=0;i--)
			if (s[i-1]<s[i]){
				int tmp=i;
				for (int j=i;j<n;j++)
					if (s[j]>s[i-1] && (s[j]<s[tmp]))
						tmp=j;
				char ch=s[tmp];s[tmp]=s[i-1];s[i-1]=ch;
				sort(s+i,s+n);
				break;
			}
		cout<<"Case #"<<t<<": ";
		if (s[0]=='0')
			for (int i=1;i<n;i++)
				cout<<s[i];
		else
			for (int i=0;i<n;i++)
				cout<<s[i];
			cout<<endl;
	}
	return 0;
}
