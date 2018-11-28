#include <fstream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

struct caster{
	char _1,_2,_3;

};

int main()
{
	ifstream fin;
	fin.open("test1.txt");
	ofstream fout;
	fout.open("test2.txt");
	
	int t;
	fin>>t;
	
	for (int i=0; i<t; i++)
	{
		int c,d,n;
		fin>>c;
		vector<caster> cv(c);
		for (int j=0; j<c; j++)
		{
			fin.ignore(1);
			fin>>cv[j]._1>>cv[j]._2>>cv[j]._3;
		}
		fin>>d;
		vector<caster> dv(d);
		for (int j=0; j<d; j++)
		{
			fin.ignore(1);
			fin>>dv[j]._1>>dv[j]._2;
		}
		fin>>n;
		fin.ignore(1);
		vector<char> a(n);
		for (int j=0; j<n; j++) fin>>a[j];
		list<char> ans;
		int size(0);
		for (int j=0; j<n; j++)
		{
			bool flag(true);
			if (size>0)
			for (int ind=0; ind<c; ind++)
			{
				if (cv[ind]._1==a[j]&&cv[ind]._2==ans.back()) { ans.pop_back(); ans.push_back(cv[ind]._3); flag=false; break; }
				if (cv[ind]._2==a[j]&&cv[ind]._1==ans.back()) { ans.pop_back(); ans.push_back(cv[ind]._3); flag=false; break; }
			}
			if (flag)
			for (int ind=0; ind<d; ind++)
			{
				if (dv[ind]._1==a[j]) 
				{
					if (find(ans.begin(),ans.end(),dv[ind]._2)!=ans.end())
					{
					ans.clear();
					size=0;
					flag=false;
					break;
					}
				}
				if (dv[ind]._2==a[j]) 
				{
					if (find(ans.begin(),ans.end(),dv[ind]._1)!=ans.end())
					{
					ans.clear();
					size=0;
					flag=false;
					break;
					}
				}
			}
			if (flag)
			{
			ans.push_back(a[j]);
			size++;
			}
		}
		fout<<"Case #"<<i+1<<": [";
		while (size>1)
		{
			fout<<ans.front()<<", ";
			ans.pop_front();
			size--;
		}
		if (size>0) fout<<ans.front();
		fout<<']'<<endl;
	}
	
	fin.close();
	fout.close();

	return 0;
}

/*
					for (unsigned ind=i+1; i<a.length(); i++)
					{
						if (a[ind]==f)
						{
							if (ind<min)
							{
								min=ind;
								cast=cv[l];
							}
						break;
						}
					}
	
*/