#include<iostream>
#include<fstream>
#include<cstring>
#include<vector>
using namespace std;
class charinfo
{
      public:
             char value;
             int weight;
             charinfo(char pvalue,int pweight)
             {
                    value=pvalue;
                    weight=pweight;
             }
};
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int T;
    long long int ans,i,j,k,l,m,temp;
    char message[65];
    char stdweight[65];
    stdweight[0]=1;
    stdweight[1]=0;
    for(i=2;i<65;i++) stdweight[i]=i;
    bool found;
    int base,power;
    input>>T;
    for(i=0;i<T;i++)
    {
                    input>>message;
                    vector<charinfo> charwts;
                    
                    l=0;
                    for(j=0;j<strlen(message);j++)
                    {
                    found=false;                              
                    for(k=0;k<charwts.size();k++)
                    {
                                if(charwts[k].value==message[j])
                                {
                                                               found=true;
                                                               break;
                                }
                    }
                    if(found==false)                                               
                    charwts.push_back(charinfo(message[j],stdweight[l++]));  
                    }
                  //  for(j=0;j<charwts.size();j++) cout<<charwts[j].value<<"  "<<charwts[j].weight<<"\n";
                    //cin>>j;
                    
                    base=charwts.size();
                    if(base==1) base=2;
                    ans=0;
                    for(j=strlen(message)-1;j>=0;j--)
                    {
                                                                  
                                                     for(l=0;l<charwts.size();l++)
                                                     {
                                                                                  if(charwts[l].value==message[j])
                                                                                  {
                                                                                                                  m=charwts[l].weight;
                                                                                                                  break;
                                                                                  }
                                                     }
                                                     power=strlen(message)-1-j;
                                                     temp=1;
                                                     
                                                     for(l=0;l<power;l++) temp=temp*base;
                                                     ans=ans+temp*m;
                                                    // cout<<j<<" char="<<message[j]<<" pow="<<power<<" wt="<<m<<" base="<<base<<" ans="<<ans<<"\n";
                    }
                    output<<"Case #"<<(i+1)<<": "<<ans<<"\n";
                    }
                                                     
                                                     
                    

    
    input.close();
    output.close();
   // cin>>i;
    return 0;
}
