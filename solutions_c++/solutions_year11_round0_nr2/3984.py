#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

int main()
{
    int t,c,d,n;

    string c1,c2,c3,comb,opp,ans;
    ifstream ifs ( "t.in" , ifstream::in );

    
    ofstream myfile;
	myfile.open ("example.txt");

    int j;
    string str;
    size_t x;
    char ch,findComb;
    bool flg;
	
	ifs>>t;
    for(int i=0;i<t;i++)
    {
        ifs>>c;
        for(j=0;j<c;j++)
        {
            ifs>>str;           
            comb.append(str);
        }
        ifs>>d;
        for(j=0;j<d;j++)
        {
            ifs>>str;           
            opp.append(str);
        }
        ifs>>n;
        for(j=0;j<n;j++)
        {
			flg=false;        
        	ifs>>ch;
        	if(ans.length()!=0)
        	{
        		findComb=ans[ans.length()-1];
    
        		
        		str="";
        		str.push_back(ch);
        		str.push_back(findComb);
        
        		x=0;
    			do
				{
					x=comb.find(str,x==0?0:x+1);								//search first combination
					if(x!=string::npos && x%3==0)
					{			
						ans=ans.substr(0,ans.length()-1);
						ans.push_back(comb[x+2]);
						flg=true;
						break;
					}
				}while(x!=string::npos);
				
				
	    		str="";
        		str.push_back(findComb);
        		str.push_back(ch);

			  
        		x=-1;
        		if(!flg)
    			do
				{
					x=comb.find(str,x+1);								//search reverse combination
					if(x!=string::npos && x%3==0)
					{			
						ans=ans.substr(0,ans.length()-1);
						ans.push_back(comb[x+2]);
						flg=true;
						break;
					}
				}while(x!=string::npos);
				
			
				
				
				x=-1;
				
	            if(!flg)
					do
					{
						x=opp.find(ch,x+1);									//invoked
						if(x!=string::npos)
						{	
							if(x%2==0 && ans.find(opp[x+1])!=string::npos)
							{
								ans="";
								break;
							}
							else if(x%2==1 && ans.find(opp[x-1])!=string::npos)
							{
								ans="";						
								break;
							}	
						}
						else
					    	ans.push_back(ch);		
					}while(x!=string::npos);				
        	}
        	else
	        	ans.push_back(ch);		    
        }
        myfile<<"Case #"<<i+1<<": [";
        if(ans.length()!=0)
        {
		    for(j=0;j<ans.length()-1;j++)
			    myfile<<ans[j]<<", "; 
		    myfile<<ans[ans.length()-1];        
        }
        myfile<<"]\n";
        ans="";  
        comb="";
        opp="";
    }
    
    return 0;
}
