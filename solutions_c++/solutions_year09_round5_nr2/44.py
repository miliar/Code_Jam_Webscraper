#include <iostream>
#include <vector>

using namespace std;

struct Tterm{
	int l;
	int t[5];
};
Tterm poly[5];
int k, d, termNum;
int status[10];
const int mod = 10009;
vector<int> letters;
int n;
int a[100][26];

void init()
{
	char s[100];
	cin>>s>>k;
	termNum = 0;
	for (int i=0; i<5;i++)
		poly[i].l = 0;
		
	for (int i=0; s[i]; i++)
		if (s[i]=='+') termNum++;
		else {
			poly[termNum].t[poly[termNum].l++] = s[i]-'a';
		}
	termNum++;
	memset(a,0,sizeof(a));
	cin>>n;
	for (int i=0; i<n; i++)
	{
		cin>>s;
		for (int j=0; s[j]; j++)
			a[i][s[j]-'a']++;
	}
}
int calc(vector<int> &v)
{
	int ans = 0, s;
	for (int i=0; i<n; i++)
	{
		s = 1;
		for (vector<int>::iterator l = v.begin(); l!=v.end(); l++)
			s=(s*a[i][*l])% mod;
		ans=(ans+s)%mod;
	}
//	for (int i=0; i<v.size(); i++)
// 	    cout<<v[i]<<' ';
//	cout<<"ans: "<<ans<<endl;

	return ans;
}
int calc(Tterm & term)
{
	int ans = 0;	
	int tot = 1, l = term.l;	
	
	for (int i=0; i<l; i++)	
		tot*=d;
	memset(status, 0, sizeof(status));
	for (int s=0; s<tot;s++)
	{
		int sum=1;
		for (int num=0; num<d; num++)
		{
			letters.clear();
			for (int i=0; i<l; i++)
				if (status[i]==num) 
					letters.push_back(term.t[i]);
			if (!letters.empty())
				sum=(sum*calc(letters))%mod;
			else sum=(sum*n) %mod;
			if (sum==0) break;
		}
		ans+=sum;
		//increase status
		status[0]++;
		for (int i=0; i<l && status[i]>=d; i++)
		{
			status[i]%=d;
			status[i+1]++;
		}
	}
	return ans;
}
int calc()
{
	int ans = 0;
	for (int i=0; i<termNum; i++)
	{
//        cout<<calc(poly[i])<<' ';
		ans=(ans+calc(poly[i]))% mod;
    }
//    cout<<endl;
	return ans;
}
int main()
{
	int t;
	cin>>t;
	for (int i=0; i<t;i++)
	{
		cout<<"Case #"<<i+1<<":";
		init();
		for (d=1; d<=k; d++)
		{
			cout<<' '<<calc();
		}
		cout<<endl;
	}
	return 0;
} 
