#include <iostream>
#include <vector>
#include <string>

using namespace std;

int calc (string s)
{
	int resp=1;
	for (int i=1;i<s.size();i++)
	{
		if (s[i]!=s[i-1])
			resp++;
	}
	return resp;
}

int main()
{
	int N;
	cin >> N;
	for (int caso=1;caso<=N;caso++)
	{
		int k;
		cin >> k;
		vector <int> per(k);
		string s;
		cin >> s;
		for (int i=0;i<k;i++)
		{
			per[i]=i;
		}
		int min=s.size()+1;
		do
		{
			string t="";
			for (int i=0;i*k<s.size();i++)
			{
				int base=i*k;
				for (int j=0;j<k;j++)
				{
					t+=s[base+per[j]];
				}
			}
			int res=calc(t);
			if (res<min)
				min=res;
		}while(next_permutation(per.begin(),per.end()));
		cout << "Case #" << caso << ": " << min << endl;
	}
}
