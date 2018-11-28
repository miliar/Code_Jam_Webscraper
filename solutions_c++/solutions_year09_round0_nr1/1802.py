#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> dic;

int main()
{
	int l,d,n;
	cin >> l >> d >> n;

	dic.resize(d);
	for(int i=0;i<d;i++)
		cin >> dic[i];

	for(int i=0;i<n;i++)
	{
		string a;
		cin >> a;
		int cnt=0;
		for(int dicj=0;dicj<d;dicj++)
		{
			bool b=true;
			int ac=0;
			for(int j=0;j<l;j++)
			{
				if(a[ac]=='(') 
				{
					while(a[ac]!=dic[dicj][j] && a[ac]!=')') ac++;
					if(a[ac]!=dic[dicj][j])
					{
						b=false;
						break;
					}
					else if(a[ac]==dic[dicj][j])
					{
						while(a[ac]!=')') ac++;
					}
				}
				else if(a[ac]!=dic[dicj][j])
				{
					b=false;
					break;
				}
				ac++;
			}
			if(b) cnt++;
		}
		cout << "Case #"<<i+1<<": "<<cnt << endl;
	}
	
}
