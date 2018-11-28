// Jai Mata Di
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	fstream in("A-small.in",ios::in);
	fstream out("A-small.out",ios::out);
	if(!in.is_open() || !out.is_open())
	{
		cout<<"File opening Error";
	}

	int l,d,notc;
	vector<string> dict;
//inout n's
	in>>l>>d>>notc;	
//input dict
	for(int i=0;i<d;i++)
	{
		string s;
		in>>s;
		dict.push_back(s);
	}

	for(int k=1;k<=notc;k++)
	{
		vector<string> a;
	//input RE
		for(int i=0;i<l;i++)
		{
			char c;
			in>>c;
			if(c!='(')
			{
				string s="";
				s.push_back(c);
				a.push_back(s);	
			}
			else
			{
				string s="";
				in>>c;
				while(c!=')')
				{
					s.push_back(c);
					in>>c;
				}
				a.push_back(s);
			}
		}
/*	// Print
		for(int i=0;i<l;i++)
		{
			out<<a[i]<<"\n";
		}	
*/
	// Check for each dictionary Entry.Count Right Entries.
		int count=0;
		for(int i=0;i<d;i++)
		{
			bool isPossible=true;
			for(int j=0;j<l && isPossible;j++)
			{	
				size_t found;
				found=a[j].find_first_of(dict[i][j],0);			
				if(found==string::npos)
				{
					isPossible=false;
				}
			}
			if(isPossible==true)
				count++;
		}
	//Output Answer
		out<<"Case #"<<k<<": "<<count<<endl;
	}
}
