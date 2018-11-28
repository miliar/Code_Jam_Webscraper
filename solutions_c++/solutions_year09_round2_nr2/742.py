#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;++t){
    	vector<int> c;
    	c.clear();
		cout<<"Case #"<<t<<": ";
		string s;
		getline(cin,s);
		for(int i=0;i<s.size();++i)
            c.push_back(s[i]-'0');
        int n=c.size();
		int min=n-1;
		while(min>0&&c[min]<=c[min-1])min--;
		min--;
		if(min<0)
		{
			for(int o=1;o<n;++o)
				c[n-o]=c[n-o-1];
			n++;
			min++;
			c[0]=0;
		}
		int max=min+1;
		for(int p=max;p<n;p++)
			if(c[p]>c[min]&&c[max]>=c[p])max=p;
        swap(c[max],c[min]);
        vector<int> c2;
        c2.clear();
        for(int o=0;o<n-min-1;++o)
			c2.push_back(c[min+o+1]);
        sort(c2.begin(),c2.end());
        for(int tt=0;tt<min+1;++tt)
    		cout<<c[tt];
        for(int tt=0;tt<n-min-1;++tt)
			cout<<c2[tt];
		cout<<endl;
	}
    return 0;
}
