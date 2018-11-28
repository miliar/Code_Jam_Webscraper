#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<sstream>
#include<istream>
#include<fstream>
using namespace std;
 
string input = "B-large.in";
string output = "B-large.out";
 
int main()
{
        int t,n,s,p;
        ifstream fs ( input.c_str() , ifstream::in );
        fs>>t;
        ofstream os;
        os.open(output.c_str());
        for(int i=0;i<t;++i)
        {
                fs >> n >> s >> p;
                vector<int> gp(n);
                int count = 0;
                for(int j=0;j<n;++j)
                {
                        fs >> gp[j];
                        vector<int> trip(3,gp[j]/3);
                        int extra = (gp[j]%3);
						
						if(extra == 2)
						{
							++trip[1];
							--extra;
						}
						trip[0]+=extra;
						int max_diff = trip[0]-trip[1];
						while(max_diff <= 2)
						{
							if(trip[0] >= p )
							{
								if(max_diff == 2)
								{
									if(s==0) break;
									--s; 
								}
								++count;
								break;
							}
							++trip[0];
							--trip[1];
							if(trip[0] > 10) break;
							if(trip[1] < 0) break;
							max_diff = trip[0]-trip[1];
						}
                }
                os << "Case #" << i+1 << ": " << count << endl;
        }
 
        return 0;
}