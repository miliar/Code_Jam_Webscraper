#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include<cmath>
#include<sstream>
#define lint long long int
using namespace std;
int main()
{
    lint count=1;
   string inp;
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    
    
    string col = "0";string pcol;lint butt;lint nomoves=0;
    lint oprev=1,ocurr=1,bprev=1,bcurr=1;lint odiff=0,bdiff=0,total=0;lint notcs;
    fin>>notcs; getline(fin,inp);
    for(lint i=0;i<notcs;i++)
    {
            getline(fin,inp);
           
              stringstream input;
            input << inp;
            input>>nomoves;
            for(lint j=0;j<nomoves;j++)
            {
                pcol=col;
                input>>col>>butt;                
               
                if(col == "O")
                {
                     oprev=ocurr;
                     ocurr=butt;
                     odiff+= abs(ocurr-oprev) + 1;//cout<<"odiff"<<odiff<<"\n";
                    if(pcol==col || pcol == "0") 
                    {
                          total+=abs(ocurr-oprev) + 1;
                          bdiff=0;
                    }
                    else
                    {
                        if(odiff<=bdiff)
                             {
                             total+=1;
                             bdiff=0;
                             odiff=1;
                             }
                        else {
                             odiff=odiff-bdiff;
                             
                             total+=(abs(ocurr-oprev) + 1 - bdiff);
                             bdiff=0;
                             }
                    }
                        
                }
                if(col == "B")
                {
                     bprev=bcurr;
                     bcurr=butt;
                     bdiff+= abs(bcurr-bprev) + 1;
                    if(pcol==col || pcol == "0") 
                    {
                          total+=abs(bcurr-bprev) + 1;
                          odiff=0;
                    }
                    else
                    {
                        if(bdiff<=odiff)
                             {
                             total+=1;
                             odiff=0;
                             bdiff=1;
                             }
                        else {
                             bdiff=bdiff-odiff;
                             
                             total+= (abs(bcurr-bprev) + 1 - odiff);
                             odiff=0;
                             }
                    }
                        
                }
            }
            fout<<"Case #"<<count<<": "<<total<<"\n";
             cout<<"Case #"<<count<<": "<<total<<"\n";
            total=0;col="0";oprev=1;ocurr=1;bprev=1;bcurr=1;odiff=0;bdiff=0;inp="";
            count++;
    }
    int y; cin>>y;
    return 0;
}
