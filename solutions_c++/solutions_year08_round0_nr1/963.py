#include<iostream>
#include<string>
#include<vector>
#include<sstream>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    vector<int> ans;
    vector<string> qrs;
    vector<string> nms;
    int nm,qr;
    string s;
    for(int i=0;i<tc;i++)
    {
            cin>>nm;
            getline(cin,s);
            for(int j=0;j<nm;j++)
            {
                    getline(cin,s);
                    nms.push_back(s);
            }
            cin>>qr;
            if(qr==0)
            {
               ans.push_back(0);
               continue;
            }
            getline(cin,s);
            for(int j=0;j<qr;j++)
            {
                    getline(cin,s);
                    qrs.push_back(s);
            }
            int a=0;
            while(qrs.size()!=0)
            {
                int maxqr=-1;                                
                for(int j=0;j<nms.size();j++)
                {
                    for(int k=0;k<qrs.size();k++)
                    {
                        if(nms[j]==qrs[k])
                        {
                           if(k>maxqr)
                                    maxqr=k;
                           break;
                        }
                        if(k==qrs.size()-1)
                           maxqr=qrs.size(); 
                    }
                }
                if(maxqr!=qrs.size())
                {
                   qrs.erase(qrs.begin(),qrs.begin()+maxqr);
                   a++;
                }
                else
                    break;
            }  
            ans.push_back(a);
            nms.erase(nms.begin(),nms.end());
            qrs.erase(qrs.begin(),qrs.end());
    }
    for(int i=0;i<tc;i++)
            cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
    return 0;
}                                                             
