#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <cstdlib>


using namespace std;

class Combine
{
	private: char f, s, r;

	public: 
		Combine(string str)
		{
			f = str[0];
			s = str[1];
			r = str[2];
		}

		string combine(string str);
		void print()
		{
			//cerr<<f<<","<<s<<","<<r<<endl;
		}
};

string Combine::combine(string str)
{
	if (str.size()<2) return str;

	if ( (str[str.size()-1]==f && str[str.size()-2]==s) ||
	     (str[str.size()-1]==s && str[str.size()-2]==f)
		 )
	{
		//cerr<<"Inside erase"<<endl;

		str.erase(str.size()-2);
		str.append(1,r);
	}

	return str;
}

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int C=0;
		cin>>C;
		vector<Combine> combine;

		for (int c=0;c<C;c++)
		{
			string str;
			cin>>str;
			combine.push_back(Combine(str));
			combine[combine.size()-1].print();
		}

		int D=0;
		cin>>D;
		vector<string> oppose;

		for (int d=0;d<D;d++)
		{
			string str;
			cin>>str;
			oppose.push_back(str);
		}

		string spell;
		int N;
		cin>>N>>spell;

		string result;
		for (int i=0;i<spell.size();i++)
		{
			result.append(1,spell[i]);
			
		//	cerr<<result<<": "<<endl; 

			for (int j=0;j<combine.size();j++)
			{
				result = combine[j].combine(result);
			}
			
			for (int j=0;j<oppose.size();j++)
			{
				size_t found1;
				size_t found2;
				found1 = result.find(oppose[j][0]);
				found2 = result.find(oppose[j][1]);

				if (found1 != string::npos && found2 != string::npos) 
					result = "";
			
			//	cerr<<result<<": "<<endl; 
			}

		}	
		
		if (result.size()>0) 
				cout<<"Case #"<<t+1<<": ["<<result[0];
		else 
				cout<<"Case #"<<t+1<<": [";
			
		for (int i=1;i<result.size();i++)
		{
			cout<<", "<<result[i];
		}
		cout<<"]"<<endl;

	
	}//test case for ends

}
