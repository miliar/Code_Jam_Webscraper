#include <iostream>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
	int tcases;
	cin>>tcases;
//	cout<<"testcases = "<<tcases<<endl;
	for(int t=0;t<tcases;++t)
	{
		int n,inp,cnt=0;
		string line;

		cin>>n;
		getline(cin,line);//dummy

//		cout<<"engines = "<<n<<endl;


		vector<string> v;
		for(int i=0;i<n;++i)
		{
			getline(cin,line);
//			cout<<line<<endl;
			if(!line.empty())
				v.push_back(line);
		}
//		cout<<" v.size()="<<v.size()<<endl;
		n=v.size();
				
		cin>>inp;
		getline(cin,line);
//		cout<<" inputs="<<inp<<endl;

		map<string,int> m;
		while(inp--)
		{			
			getline(cin,line);
			m[line]++;
//			cout<<line<<":"<<m[line]<<" togle="<<cnt<<endl;
			int nonz=0;
			for (int i=0;i<n;i++)
			{
//			cout<<"i="<<i<<" n="<<n<<endl;
				if(m[v[i]])
					nonz++;
			}
			if(nonz==n)
			{
				cnt++;
				m.clear();
				m[line]++;
			}			
		}
		cout<<"Case #"<<t+1<<": "<<cnt<<endl;			
	}
	
	return 0;
}

