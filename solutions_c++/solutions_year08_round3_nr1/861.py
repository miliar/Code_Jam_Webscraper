#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>

using namespace std;


class mess
{
public:
	int p;
	int k;
	int l;
	int resul;
	vector<int> ld;
	vector<vector<int> > t;
	mess();
};
mess::mess()
{
	resul=0;
	int i,j,z;
	cin>>i>>j>>z;
	p=i;
	k=j;
	l=z;
	for (i=0;i<l;i++)
	{
		cin>>j;
		ld.push_back(j);
		//cout<<j<<"mmm";
	}
// 	for (i=0;i<l;i++)
// 	{
// 		cout<<ld[i];
// 	}
	sort(ld.begin(),ld.end());
	reverse(ld.begin(),ld.end());
// 	for (i=0;i<l;i++)
// 	{
// 		cout<<ld[i];
// 	}
	t.resize(k);
	 
		for (j=0;j<k;j++)
		{ 
			t[j].reserve(p);
			//cout<<p<<endl;
			 
			
	 
	}
	for (i=0;!ld.empty();i++)
	{
		for (j=0;j<k;j++)
		{ 
			 
			if (!ld.empty())
			{
				t[j].push_back(ld.back());
				//cout<<ld.back()<<"ccc"<<endl;
			ld.pop_back();
			}
			
			
			
		}
	}
	

	for (j=0;j<k;j++)
	{
		reverse(t[j].begin(),t[j].end());
	
	}
	for (j=0;j<k;j++)
	{
		
		for (i=0;i<t[j].size();i++)
		{
			resul+=t[j][i]*(i+1);
			//cout<<t[j][i]<<"aaa"<<i+1<<endl;
		}
	}



}

int main()
{
	int number;
	cin >> number;
	
	mess * p = new mess[number];
	for (int i = 0; i < number; i++)
	{
		cout << "Case #" << i + 1 << ": " << p[i].resul << endl;
	}
	
	return 1;
}