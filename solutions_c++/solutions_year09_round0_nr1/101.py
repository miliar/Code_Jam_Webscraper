#include<iostream>
#include<string>
using namespace std;

int main()
{

	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int l,d,n;
	cin>>l>>d>>n;
	string s[5000];
	for(int i=0;i<d;i++)
		cin>>s[i];
	int b[15]['z'+1];

	char ch;
	for(int i=0;i<n;i++){
		memset(b,0,sizeof(b));
		for(int j=0;j<l;j++){
			cin>>ch;
			if(ch=='('){
				while(1){
					cin>>ch;
					if(ch==')')break;
					b[j][ch]=1;
				}
			}else{
				b[j][ch]=1;
			}
		}
		int sum=0;
		for(int j=0;j<d;j++){
			int flag=1;
			for(int k=0;k<l;k++)
				if(b[k][s[j][k]]==0)flag=0;
			if(flag)sum++;
		}
		cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	return 0;
}

