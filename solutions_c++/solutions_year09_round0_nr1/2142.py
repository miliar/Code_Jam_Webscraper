#include <iostream>
#include <set>
#include <vector>
#include <string>


using namespace std;

int main()
{
	int l,d,n;
	set<string> s;
	set<string>::iterator it;
	string temp;

	freopen("input.txt","r",stdin);
	freopen("op.txt","w",stdout);
	cin>>l>>d>>n;
	for(int i=0;i<d;i++)
	{
		cin>>temp;
		s.insert(temp);
	}
	//n=1;//remove this after test
	int i,j,case_no=1;
	while(n!=0)
	{
		vector<string> parsed;
		cin>>temp;
		string t;
		int flag=0;
		t="";
		for(i=0;i<(int)temp.size();i++)
		{
			if(flag == 0)
			{
				if(temp.at(i) == '(')
				{
					flag=1;
					continue;
				}
				t=t+temp.at(i);
				parsed.push_back(t);
				t="";
			}
			else
			{
				for(j=i;temp.at(j)!=')';j++)
					t+=temp.at(j);
				parsed.push_back(t);
				i=j;
				flag=0;	
				t="";;							
			}
		}
		/*cout<<"The parsed string is \n";
		for(i=0;i<(int)parsed.size();i++)
			cout<<parsed[i]<<"\n";*/
		int count=0;
		
		for ( it=s.begin() ; it != s.end(); it++ )
		{	
			t=*it;
			//cout<<t<<"\n";
			size_t found;
			int valid=1;
			for(i=0;i<(int)parsed.size();i++)
			{
				found=parsed[i].find_first_of(t.at(i),0);
				//cout<<t.at(i)<<"\t"<<parsed[i]<<endl;
				if(found==string::npos)
				{
					valid=0;
					continue;
				}
			}
			if(valid == 1)
				count++;
			
		}
		//cout<<"The number of matches are "<<count<<"\n";
		cout<<"Case #"<<case_no<<": "<<count<<endl; 
		case_no++;
		
		n--;
	}
	return 0;
}
