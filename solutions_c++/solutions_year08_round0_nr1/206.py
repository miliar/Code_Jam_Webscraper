#include<iostream>
#include<vector>
#include<string>
#include <sstream>
using namespace std;
int main()
{
    int N,S,Q,i,j,k,curr,tempcurr;
    vector <string> se;
    vector <string> qu;
    vector <int> count(100);
    int c,flag;
    string temp;
    cin>>N;
    for(i=0;i<N;i++)
    {
                    se.clear();
                    qu.clear();
                    cin>>S;
                    getline(std::cin,temp);
                    for(j=0;j<S;j++)
                    {
                                    getline(std::cin,temp);
                                    se.push_back(temp);
                                    //cout<<se[j]<<j;
                    }
                    //cout<<"here";
                    cin>>Q;
                    getline(std::cin,temp);
                    for(j=0;j<Q;j++)
                    {
                                    getline(std::cin,temp);
                                    qu.push_back(temp);
                    }
                    j=0;
                    c=0;
                    curr=-1;
                    while(j<Q)
                    {
                              for(k=0;k<S;k++)
                              {
                                                  count[k]=0;
                              }
                              flag=1;
                              while(flag==1&&j<Q)
                              {
                                        for(k=0;k<S;k++)
                                        {
                                            if(qu[j].compare(se[k])==0)//found a search engine
                                            {
                                                    count[k]=1;
                                                    tempcurr=k;
                                                    break;                                  
                                            }            
                                        }
                                        flag=0;
                                        for(k=0;k<S;k++)
                                        {
                                                 if(count[k]==0)
                                                 {
                                                                flag++;
                                                 }
                                        }
                                        if(flag==0)
                                            curr=tempcurr;
                                        else
                                        {
                                                j++;
                                                flag=1;
                                        }
                              }
                              
                              //cout<<"j="<<j<<"c=";
                              if(flag==0)c++;
                    }
    cout<<"Case #"<<i+1<<": "<<c<<"\n";
    }
    //system("PAUSE");
    return 1;
}
