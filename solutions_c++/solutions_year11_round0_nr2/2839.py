#include "iostream"
#include "fstream"
#include "string"
using namespace std;
int main()
{
	ifstream is;
	ofstream ost;
	
	//is.open("test");
	//is.open("B-small-attempt0.in");
	is.open("B-large.in");
	ost.open("output");
	
	int T, C, D, N;
	
	is>>T;
	for(int rc=1; rc<=T; rc++)
	{
		char bs[50][3], os[50][2];
	
		is>>C;
		for(int i=0; i<C; i++) { is>>bs[i][0]; is>>bs[i][1]; is>>bs[i][2]; }

		is>>D;
		for(int i=0; i<D; i++) { is>>os[i][0]; is>>os[i][1]; }	
	
		char c, pc;
		string out = "";
		size_t found;

		is>>N;
		
		is>>pc;
		out.push_back(pc);
		
		int j;
		for(j=0; j<(N-1); j++)
		{
			int flag = 0;
			is>>c;
			
			for(int i=0; i<C; i++)
			{
				if((bs[i][0] == c && bs[i][1] == pc) || (bs[i][0] == pc && bs[i][1] == c))				
				{
					c = bs[i][2];
					out = out.substr(0, out.length() - 1);
					break;
				}
			}
			
			for(int i=0; i<D; i++)
			{
				if(os[i][0] == c)
				{
					found = out.find_first_of(os[i][1]);
					
					if(found!=string::npos)
					{
						out.clear();
						flag=1; j++;
						if(j<(N-1)) { is>>pc; out.push_back(pc); }
						break;
					}
				}
				if(os[i][1] == c)
				{
					found = out.find_first_of(os[i][0]);
					
					if(found!=string::npos)
					{
						out.clear();
						flag=1; j++; 
						if(j<(N-1)) { is>>pc; out.push_back(pc);  }
						break;
					}					
				}
			}
			
			if(flag == 0)
			{
				out.push_back(c);  
				pc = c;
			}
		}
		
		string final = "[";
		
		for(int i=0; i<out.length(); i++)
		{
			final = final + out[i] + ", ";
		}
		
		final = final.substr(0, final.length() - 2) + "]";

		cout<<"Case #"<<rc<<": "<<final<<endl;
		ost<<"Case #"<<rc<<": "<<final<<endl;
	}
	
	ost.flush();

	is.close();
	ost.close();
	
	return 0;
}