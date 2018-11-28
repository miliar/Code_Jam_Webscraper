#include<string>
#include<vector>
#include<iostream>
#include<iomanip>
#include<map>
#include<set>
#include<functional>
#include<fstream>
using namespace std;
int mark[1000][1000];
int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int t;
    cin>>t;
    //for(int i=0;i<Ys.size();i++)cout<<i+1<<" "<<Ys[i]<<endl;
    for(int p=1;p<=t;p++)
    {            
            int n,k;
            int i,j;
            cin>>n>>k;
            vector<string> mark(n);
            for(i=0;i<n;i++)
            {
               cin>>mark[i];
               //cout<<mark[i]<<endl;
            }
            for(i=0;i<n;i++)
            {
               string tem;
               for(int k=0;k<n;k++)
               {
                  tem=tem+'.';
               }
               int m=n-1;
               for(j=n-1;j>=0;j--)
               {
                  if(mark[i][j]!='.'){tem[m]=mark[i][j];m--;}
               }
               mark[i]=tem;
               //cout<<tem<<endl;
            }
            string fr="";
            string fb="";
            for(i=0;i<k;i++)
            {
               fr+='R';
               fb+='B';
            }
            //cout<<fr<<endl;
            //cout<<fb<<endl;
            vector<string> markv;
            vector<string> markd1;
            vector<string> markd2;
            //markd1;
            for(i=0;i<n;i++)
            {
               string tem;
               for(j=0;j<=i;j++)
               {
                  tem+=mark[j][i-j];
               }
               markd1.push_back(tem);
               //cout<<tem<<endl;
            }
            for(i=0;i<n;i++)
            {
               string tem;
               for(j=0;j<=i;j++)
               {
                  tem+=mark[n-1-j][n-1-i+j];
               }
               markd1.push_back(tem);//cout<<tem<<endl;
            }
            //markd2
            for(i=0;i<n;i++)
            {
               string tem;
               for(j=0;j<=i;j++)
               {
                  tem+=mark[n-1-j][i-j];
               }
               markd2.push_back(tem);//cout<<tem<<endl;
            }
            for(i=0;i<n;i++)
            {
               string tem;
               for(j=0;j<=i;j++)
               {
                  tem+=mark[j][n-1-i+j];
               }
               markd2.push_back(tem);//cout<<tem<<endl;
            }
            //markv
            for(i=0;i<n;i++)
            {
               string tem;
               for(j=0;j<n;j++)
               {
                  tem+=mark[j][i];
               }
               markv.push_back(tem);//cout<<tem<<endl;
            }
            bool findr=false;
            bool findb=false;
            
            for(i=0;i<mark.size();i++)
            {
               if(mark[i].find(fr)!=string::npos){findr=true;}
               if(mark[i].find(fb)!=string::npos){findb=true;}
            }
            for(i=0;i<markv.size();i++)
            {
               if(markv[i].find(fr)!=string::npos){findr=true;}
               if(markv[i].find(fb)!=string::npos){findb=true;}
            }
            for(i=0;i<markd1.size();i++)
            {
               if(markd1[i].find(fr)!=string::npos){findr=true;}
               if(markd1[i].find(fb)!=string::npos){findb=true;}
            }
            for(i=0;i<markd2.size();i++)
            {
               if(markd2[i].find(fr)!=string::npos){findr=true;}
               if(markd2[i].find(fb)!=string::npos){findb=true;}
            }
            if(findr==false && findb==false){cout<<"Case #"<<p<<": "<<"Neither";}
            if(findb==true && findr==false){cout<<"Case #"<<p<<": "<<"Blue";}
            if(findr==true && findb==false){cout<<"Case #"<<p<<": "<<"Red";}
            if(findb==true && findr==true){cout<<"Case #"<<p<<": "<<"Both";}
            cout<<endl;
    }
}
