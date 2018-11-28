#include <iostream>
#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

char us[2000001];

int pow(int a, int p)
{
	int ans = 1;
	while(p){
		if(p&1)
			ans*=a;
		a*=a;
		p/=2;
	}
	return ans;
}

int main()
{

	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		
		int A,B;
		cin>>A>>B;
		long long ans =0;
		memset(us, 0, sizeof(us));
		for(int j=A;j<=B;j++){
			if(!us[j]){
				us[j]=1;
				int t=j;
				int l=0;
				int z = t%10;
				bool g =false;					
				while(t){if(t%10!=z)g=true;
			l++;t/=10;}
				if(!g)continue;
		
				long long  cnt=1;
				set<int> st;
				st.insert(j);
				for(int k=1;k<l;k++)
				{
					if(j%pow(10, k) >= pow(10,k-1)){
						int c=j%pow(10,k);
						int nb = j/pow(10,k);
						nb += c*pow(10, l-k);
						if(nb <= 2000000)us[nb]=1;
						if(nb<=B &&  nb>=A)st.insert(nb);
					}
				}
				
				cnt = st.size();
				/*if(cnt>1){
					cout<<j<<" "<< cnt<<endl;
				}*/
				ans += cnt*(cnt-1)/2;
			}
		}		
		cout<<"Case #"<<i+1<<": ";
		cout<<ans<<endl;

	}


	return 0;
}
