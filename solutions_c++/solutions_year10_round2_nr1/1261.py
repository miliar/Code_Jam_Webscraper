#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct dir{
int par;
string name;
vector<int> childs;
};


int main()
{
	int num_case;

	cin>>num_case;

	for(int i=0; i!=num_case; i++)
	{
		int N,M;
		cin>>N; 
		cin>>M;

		vector<dir> v;
		v.reserve(200);

		dir d;
		d.par=0;
		
		v.push_back(d);

		
		
		for(int j=0; j!=N ; j++)
		{
			string s;
			cin>>s;
			
			int m=0,k=0;
			
			int s_size=s.size();
			while(k<s_size)
			{
				k++;			
					string name;
					while(k<s_size && s[k]!='/')
					{
					name.push_back(s[k]);
					k++;
					}

				int c_size=v[m].childs.size();
				bool flag=0;
				for(int t=0; t!=c_size; t++)
				{
					
					if(name.compare(v[v[m].childs[t]].name)==0)
					{
						flag=1;
						m=v[m].childs[t];
						break;
					}
								
				}
				if(!flag)
				{

					dir d;
					d.par=m;
					d.name=name;
					name.clear();
				v.push_back(d);
			v[m].childs.push_back(v.size()-1);
			m=v.size()-1;
					while(k<s_size)
					{
					
					k++;
					while(k<s_size && s[k]!='/')
					{
					name.push_back(s[k]);
					k++;
					}
					dir d;
					d.par=m;
					d.name=name;
					name.clear();
					v.push_back(d);
					v[m].childs.push_back(v.size()-1);
					m=v.size()-1;

					}
				}

				
			}
		}
		/*
		for(int l=0; l!=v.size(); l++)
		{
			cout<<l<<v[l].name<<" "<<v[l].par<<"chi ";

			int c_size=v[l].childs.size();
			for(int r=0; r!=c_size; r++)
			cout<<v[l].childs[r]<<" ";
			cout<<endl;
		}
		*/
		int count=0;
		
		
		for(int j=0; j!=M ; j++)
		{
			string s;
			cin>>s;
			
			int m=0,k=0;
			
			int s_size=s.size();
			while(k<s_size)
			{
				k++;			
					string name;
					while(k<s_size && s[k]!='/')
					{
					name.push_back(s[k]);
					k++;
					}

				int c_size=v[m].childs.size();
				bool flag=0;
				for(int t=0; t!=c_size; t++)
				{
					if(name.compare(v[v[m].childs[t]].name)==0)
					{
						flag=1;
						m=v[m].childs[t];
						break;
					}
								
				}
				if(!flag)
				{

					dir d;
					d.par=m;
					d.name=name;
					name.clear();
				v.push_back(d);
				count++;
			v[m].childs.push_back(v.size()-1);
			m=v.size()-1;
					while(k<s_size)
					{
					
					k++;
					while(k<s_size && s[k]!='/')
					{
					name.push_back(s[k]);
					k++;
					}
					dir d;
					d.par=m;
					d.name=name;
					name.clear();
					v.push_back(d);
					count++;
					v[m].childs.push_back(v.size()-1);
					m=v.size()-1;

					}
				}

				
			}

			
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;

		/*
		for(int l=0; l!=v.size(); l++)
		{
			cout<<l<<v[l].name<<" "<<v[l].par<<"chi ";

			int c_size=v[l].childs.size();
			for(int r=0; r!=c_size; r++)
			cout<<v[l].childs[r]<<" ";
			cout<<endl;
		}
		cout<<"over"<<endl;
				
		*/
	}

	return 0;
}
