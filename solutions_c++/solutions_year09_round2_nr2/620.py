#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<cmath>
#include<algorithm>

using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	for (int kase = 1; kase <= t; ++ kase) {
		cout<<"Case #"<<kase<<": ";
		string S,tmp;
		cin>>S;
		tmp=S;
		sort(tmp.begin(),tmp.end());
		reverse(tmp.begin(),tmp.end());
		if(tmp==S)
		{
			reverse(tmp.begin(),tmp.end());
			int cnt = 0,l=tmp.length();
			for(; cnt <l ; ++cnt){
				if(tmp[cnt] !='0')break;

			}
			cout << tmp.substr(cnt,1);
			for(int i = 0;i <= cnt ; ++i) cout <<"0";
			if(l>cnt+1)
				cout<<tmp.substr(cnt+1);
		}
		else
		{
			next_permutation(S.begin(),S.end());
			cout<<S;
		}
		cout <<endl;


	}
	return 0;

}

