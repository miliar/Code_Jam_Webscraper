#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	int t;
	fin>>t;
	int to=t;
	while(t--)
	{
		int r,k,n;
		fin>>r>>k>>n;
		vector<int> v;
		for(int i=0;i<n;i++)
		{
			int tmp;
			fin>>tmp;
			v.push_back(tmp);
		}
		int p=0;
		int total=0;
		while(r--)
		{
			int tmp=0;
			int last;
			int count=0;
			while(tmp<=k)
			{
				if(tmp>k || count>v.size())break;				
				tmp+=v[(p)%(v.size())];
				last=v[(p)%(v.size())];
				p++;
				count++;
			}
			p--;
			tmp=tmp-last;
// 			fout<<"tmp = "<<tmp<<endl;
			total+=tmp;
		}	
		fout<<"Case #"<<to-t<<":"<<" "<<total<<endl;		
	}
	return 0;
}
