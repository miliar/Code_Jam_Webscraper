#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> c;

char findinc(char a,char b)
{
       for(int i=0;i<c.size();i++)
       {
               if(c[i][0]==a&&c[i][1]==b)
                  return c[i][2];
       }
       
       return '\0';
}



int main()
{
    int T,totalcase;
    cin>>T;
    totalcase = T;
    while(T)
    {
            c.clear();
            vector<string> o;
            string t;
            string seq,res;
            int C,D,N;
            
            cin>>C;
            for(int i=0;i<C;i++)
            {
                    cin>>t;
                    c.push_back(t);
                    char k=t[0];
                    t[0]=t[1];
                    t[1]=k;
                    c.push_back(t);
            }
            
            sort (c.begin(),c.end());
            
            cin>>D;
            for(int i=0;i<D;i++)
            {
                    cin>>t;
                    o.push_back(t);
                    char k=t[0];
                    t[0]=t[1];
                    t[1]=k;
                    o.push_back(t);
            }
            sort (o.begin(),o.end());

            cin>>N;
            cin>>seq;
            
            res.push_back(seq[0]);
            
            //cout<<res<<"--"<<seq<<"%%%%%"<<endl;
            for(int i =1,j=0;i<N;i++)
            {
                    char combine = findinc(res[j],seq[i]);
                    if(combine!='\0')
                    {
                                   res[j]= combine;
                    }
                    else
                    {
                        res.push_back(seq[i]);
                        j++;
                    }
                    
                    for(int m=0;m<o.size();m++)
                    {
                            int done =0;
                            if(o[m][0]==res[j])
                            {
                                 for(int k=j-1;k>=0;k--)
                                 {
                                         if(res[k]==o[m][1])
                                         {
                                                        //res.erase(k,j-k+1);
                                                        //j=k-1;
                                                        res.clear();
                                                        if(i+1<seq.length())
                                                        {
                                                         res.push_back(seq[i+1]);
                                                         i++;
                                                         j=0;
                                                        }
                                                        done=1;
                                                        break;    
                                         }
                                 }
                            }
                            if(done==1)
                                       break;
                            
                    }
            }
            
            cout<<"Case #"<<(totalcase+1-T)<<": [";
            for(int i=0;i<res.length();i++)
            {
                    cout<<res[i];
                    if(i!=res.length()-1)
                    cout<<", ";
            }
            cout<<"]"<<endl;

            T--;
    }
}
