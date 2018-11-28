#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
    ifstream ipF("A-large.in");
    ofstream opF("out.txt");
    
    int L, D, N, i,j,m,n;
    ipF >> L >> D >> N;
    
    vector<string> case_vector;
    
    vector<string> ip_words;
    vector<int> count;
    string temp,case_temp,substrtemp;
    bool no_fault=true;
    for(i=0;i<D;i++)
    {
           ipF>>temp;
           ip_words.push_back(temp);
    }
    
    for(i=0;i<N;i++)
    {
           ipF>>temp;
           case_vector.push_back(temp);
           count.push_back(0);
    }
    
    for(i=0;i<D;i++)
    {
           //for every input word         
           temp=ip_words[i];
           
           for(j=0;j<N;j++)
           {
                 //for every test case
                 case_temp=case_vector[j];
                 m=0;
                 n=0;
                 no_fault=true;
                 while(m<L && no_fault)
                 {
                           if(case_temp[n]!='(')
                           {
                                 if(case_temp[n]!=temp[m]) no_fault=false;
                                 else n++;
                           }
                           else 
                           {
                                no_fault=false;
                                while(case_temp[n]!=')')
                                {
                                      n++;
                                      if(case_temp[n]==temp[m])no_fault=true;         
                                }
                                n++;
                           }
                           m++;
                 }
                 if(no_fault)count[j]++;          
           }         
    }
    for(i=0;i<N;i++)
    {
           opF << "Case #" << i+1 <<": "<<count[i]<<endl;         
     }
}
