#include<string> 
#include<iostream> 
#include<vector>
#include<cstdio>
using namespace std; 
int main(){ 
	freopen("C-large.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int n; 
	cin>>n;
	int i; 
	char*s=new char[1000];
	cin.getline(s,1000);
	string w="welcome to code jam"; 
	for(i=0;i<n;i++){ 
		cin.getline(s,1000);
		vector<int>a(19);
		int kil=0;
		int i1,i2;
		for(i1=0;s[i1];++i1){
			for(i2=0;i2<w.size();i2++){
				if(s[i1]==w[i2]){
					if(i2==0)
						a[i2]++;
					else
						a[i2]+=a[i2-1];

				}
				a[i2]%=10000;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		kil=a[w.size()-1];
		string rez="";
		while(kil){
			rez=char('0' + kil%10)+rez;
			kil/=10;
		}
		while(rez.size()<4)
			rez="0"+rez;
		cout<<rez<<endl;

	}
	return 0; 
}