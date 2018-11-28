#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<list>
using namespace std;
vector<int>a;
list<int>c;
int kil;
void rex(int pot,long long sum,int last){
	//cout<<pot<<' '<<sum<<' '<<last<<endl;
	if(last==a.size()){
		//cout<<"yo"<<endl;
		//list<int>::iterator i;
		//int yes=1;
		/*for(i=c.begin();i!=c.end();i++){
			if(sum==(*i)){
				yes=0;
				break;
			}
		}
		if(yes){*/
		//	cout<<sum<<endl;
			c.push_back(sum);
			sum=sum>0?sum:-sum;
			kil+=(sum==0 || sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0 );
	//	}
		return;
	}
	//+
	
	long long che=0;
	long long st=1;
	int i;
	for(i=pot;i>=last;i--){
		che+=a[i]*st;
		st*=10;
	}
	rex(pot+1,sum+che,pot+1);
	//-
	if(last!=0){
		rex(pot+1,sum-che,pot+1);
	}
	//NA
	if(pot!=a.size()-1)
		rex(pot+1,sum,last);
};

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	cin>>t;
	int iii;
	for(iii=1;iii<=t;iii++){
		string s;
		cin>>s;
		a.resize(s.size());
		int i;
		for(i=0;i<s.size();i++)
			a[i]=s[i]-'0';

		kil=0;
		c.resize(0);
		rex(0,0,0);
		cout<<"Case #"<<iii<<": "<<kil;
		cout<<endl;
	}
	return 0;
}