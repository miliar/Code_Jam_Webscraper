#include<iostream>
using namespace std;
int main()
{
	freopen("next.txt", "r", stdin);
	freopen("test.txt", "w", stdout);
	int l,d,n;
	cin>>l>>d>>n;
	char  dict[6000][32];
	char w[2048];
	gets(w);
	for(int i = 0;i<d;i++)
		gets(dict[i]);
	
	for(int t = 1; t <=n; t++)
	{
		int ans = 0;
		
		int a[16][26] = {0};
		gets(w);
		int s = strlen(w);
		for(int i = 0,j = 0;i<s, j<l;j++)
		{
			if(i>=s||j>=l)
				break;
			if(w[i]=='(')
			{
				i++;
				while(w[i]!=')')
				{
					a[j][w[i]-'a'] = 1;
					i++;
				}
				i++;
			}
			else
			{
				a[j][w[i]-'a'] = 1;
				i++;
			}
		}
		for(int i =0;i<d;i++)
		{
			int b = 1;
			for(int j = 0;j<l;j++)
				if(!a[j][dict[i][j]-'a'])
				{
					b =0;
					break;
				}
			if(b)
				ans++;
		}


		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}