#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int i(string a)
{
    return atoi(a.c_str());
}

int main()
{
    int t;
    cin>>t;

    for(int in=0;in<t;in++)
    {
        int count=0;
        string a,b;
        cin>>a>>b;
        
        int nod=a.size();
        int bi=i(b);
        for(int j=i(a);j<=i(b);j++)
        {
            stringstream temp;
            temp<<j;
            string cd=temp.str();
            vector<int> vet;
            
            for(int k=nod-1;k>0;k--)
            {
                
                string te=cd.substr(k,nod-k);
                te.append(cd.substr(0,k));
                int tei=i(te);  
                if(tei<=bi && tei>j)
                {
                    vet.push_back(tei);
                }
            }
            
            sort(vet.begin(), vet.end());
            count += unique(vet.begin(), vet.end()) - vet.begin();
        }
        

        cout<<"Case #"<<in+1<<": "<<count<<endl;
        cerr<<"Case #"<<in+1<<": "<<count<<endl;
    }
}
            
