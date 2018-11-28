#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);
	int T,R,k,N, temp, out=0, s, l;
	vector<int> g;
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>R>>k>>N;
		for(int j=1;j<=N;j++){
			cin>>temp;
			g.push_back(temp);
		}
		for(int j=1;j<=R;j++){
			s=g[0];
			for(l=1;s<=k && l<=g.size();l++)
				s+=g[l];
			if(l!=1)
				s=s-g[l-1];
			out+=s;
			for(int m=0;m<l-1;m++)
				g.push_back(g[m]);
			g.erase(g.begin(),g.begin()+l-1);
		}
		cout<<"Case #"<<i<<": "<<out<<endl;
		out=0;
		g.clear();
	}
	return 0;
}
			
