#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;
int main()
{
	int t,c,d,n,fr,ba,temp_fr;
	string temp,in;
	vector<string> pair,opp;
	vector<char> final,opp_this;
	//map<string,int>
	
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>c;		//cout<<c<<" ";
		pair.clear();
		opp.clear();
		final.clear();
		for(int j=0;j<c;j++)
		{
			cin>>temp;			//cout<<temp<<" ";
			pair.push_back(temp);
		}
		cin>>d;				//cout<<d<<" ";
		for(int j=0;j<d;j++)
		{
			cin>>temp;			//cout<<temp<<" ";
			opp.push_back(temp);
		}
		cin>>n;					//cout<<n<<" ";
		cin>>in;				//cout<<in<<" "<<endl;
		fr=1;
		ba=0;
		
		for(fr=1,ba=0;ba<n;fr++,ba++)
		{
			temp_fr=fr;
			for(int j=0;j<pair.size();j++)
			{
				if(pair[j][0]==in[fr]&&pair[j][1]==in[ba])
					{final.push_back(pair[j][2]);fr++;ba++;break;}
				else if(pair[j][0]==in[ba]&&pair[j][1]==in[fr])
					{final.push_back(pair[j][2]);fr++;ba++;break;}
			}
			if(fr!=temp_fr)
			{
				opp_this.clear();
			for(int j=0;j<opp.size();j++)
			{
				if(opp[j][0]==in[fr])
					{opp_this.push_back(opp[j][1]);}
				if(opp[j][1]==in[fr])
					{opp_this.push_back(opp[j][0]);}
				
			}
		
			for(int j=0;j<final.size();j++)
			{
				for(int k=0;k<opp_this.size();k++)
				{
					if(final[j]==opp_this[k])
					{
						
						final.clear();
						fr++;ba++;
						break;
					}
				}
				
			}
				continue;
			}
			else
			{
				final.push_back(in[ba]);
			}
			opp_this.clear();
			for(int j=0;j<opp.size();j++)
			{
				if(opp[j][0]==in[fr])
					{opp_this.push_back(opp[j][1]);}
				if(opp[j][1]==in[fr])
					{opp_this.push_back(opp[j][0]);}
				
			}
		
			for(int j=0;j<final.size();j++)
			{
				for(int k=0;k<opp_this.size();k++)
				{
					if(final[j]==opp_this[k])
					{
						
						final.clear();
						fr++;ba++;
						break;
					}
				}
				
			}
			
		}
		cout<<"Case #"<<i+1<<": [";
		for(int j=0;j<final.size();j++)
		{
			if(j==0)
				cout<<final[j];
			else
				cout<<", "<<final[j];
		}
		cout<<"]"<<endl;
	}
}
