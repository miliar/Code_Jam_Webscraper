#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<map>
#include<fstream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int K=T;
	ofstream fout("out.txt");
	while(T--){
		int N, S, P;
		cin>>N>>S>>P;
		int x;
		int ans=0;
		for(int i=0;i<N;i++)
		{
			cin>>x;
			//cout<<ceil(x/3.0)<<endl;
			if(ceil(x/3.0)>=P) ans++;
			else if(ceil(x/3.0)==P-1&&S>0&&x%3!=1&&x!=0)
			{	
				ans++;
				S--;
			}
		}	 
		fout<<"Case #"<<K-T<<": "<<ans<<endl;
	}	 
	return 0;
}

