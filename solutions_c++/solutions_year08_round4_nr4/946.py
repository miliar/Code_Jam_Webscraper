#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()	{

	freopen("D-small-attempt0.in","r",stdin);
	freopen("my.out","w",stdout);
	
	char per[6];
	string s;
	int i,j,k,cas;

	cin>>cas;

	for(int t=1;t<=cas;t++)	{
	
		cin>>k>>s;
		for(i=1;i<=k;i++) per[i-1]='0'+i;

		int res=1<<30;

		do{
		
			string n;
			n.resize(s.size());
			for(i=0;i<s.size();i+=k)	
				for(j=0;j<k;j++) 
					n[i+j] = s[i+per[j]-'0'-1];
			
			char c='*';
			int cnt=0;
			for(i=0;i<n.size();i++) if(c!=n[i]) {
				c=n[i];
				cnt++;
			}

			res = min(res,cnt);

		}while(next_permutation(per,per+k));

		cout<<"Case #"<<t<<": "<<res<<endl;
	
	}

	return 0;
}