#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int i,j,T,n,flag,k=0,cnt;
	char c[21];
	string s,s1,p;
	scanf("%d",&T);
	for(k=0;k<T;++k){
		scanf("%s",c);
		flag=0;
		s=s1=c;
		sort(s.begin(),s.end());
		p=s;
		if(s==s1){
			flag=1;
		}else{
			while(next_permutation(s.begin(),s.end())){
//				cout<<s<<endl;
				if(s==s1){
					flag=1;
					break;
				}
			}
		}
		if(flag==1){
			cout<<"Case #"<<k+1<<": ";
			next_permutation(s.begin(),s.end());
			if(s!=p)
				cout<<s<<endl;
			else{
				j=-1;
				cnt=0;
				while(p[++j]=='0')++cnt;
				s1=s.substr(j+1);
				cout<<p[j]<<"0";
				while(cnt--)printf("0");
				cout<<s1<<endl;
			}

		}
	}
}
