#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

int f(vector<string>& vs,vector<string>& vq)
{
	int index = 0,ret=0,cur_s=-1;
	map<string,int> m;
			
	for (int i=0;i<vs.size();i++) m[vs[i]] = i;
			
	while (index<vq.size())
	{
		if (index==0)
		{
			int minv,mini = -1;
			vector<int> v(10000,-1);
			
			for (int i=index;i<vq.size();i++) 
			{
				if (v[m[vq[i]]]==-1) v[m[vq[i]]] = i;				
			}

			minv = v[0], mini=0;
			for (int i=0;i<vs.size();i++) 
			{
				if (minv<v[i] && i!=cur_s) 
				{
					mini = i;
					minv = v[i];
				}
				if (i!=cur_s && v[i]==-1) return ret;
			}

			cur_s = mini;
		}

		if (vq[index] == vs[cur_s])
		{
			ret++;
			int minv,mini = -1;
			vector<int> v(10000,-1);
			
			for (int i=index;i<vq.size();i++) 
			{
				if (v[m[vq[i]]]==-1) v[m[vq[i]]] = i;				
			}

			minv = v[0], mini=0;
			for (int i=0;i<vs.size();i++) 
			{
				if (minv<v[i] && i!=cur_s) 
				{
					mini = i;
					minv = v[i];
				}
				if (i!=cur_s && v[i]==-1) return ret;
			}

			cur_s = mini;			
		}
		index++;
	}
	return ret;
}

int main()
{
	int t=0,n;
	stringstream ss;

	cin>>n;
	ofstream outs;


	while (n--)
	{
		int s,q;
		vector<string> vs,vq;

		cin>>s>>ws;

		while (s--)
		{
			string str;

			getline(cin,str);
			vs.push_back(str);
		}

		cin>>q>>ws;
		while (q--)
		{
			string str;

			getline(cin,str);
			vq.push_back(str);
		}

		t++;
		ss<<"Case #" <<t<<": "<<f(vs,vq)<<endl;
	}
	cout<<ss.str()<<endl;
	outs.open("a.txt");
	outs<<ss.str()<<endl;
}