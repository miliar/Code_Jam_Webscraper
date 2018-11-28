#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int t,n,flag,flag1,found,f,g,c,d,pt,i,j,s,w=1;
    char c1[37][4],d1[29][3],n1[102],ch,z[102];
     vector<char> v;
    cin>>t;
    while(t)
    {
            cin>>c;
            //cout<<c;
           v.clear();
           // v.clear();
            
            for(i=0;i<c;i++)
            {
                            cin>>c1[i];
            }
            cin>>d;
          //  cout<<d;
            for(i=0;i<d;i++)
            {
                            cin>>d1[i];
            }
            cin>>n;
            cin>>n1;
            //cout<<n1<<endl;
            for(int q=0;q<n;q++)
            {
                            flag=0;
                            flag1=0;
                            found=0;
                           // f1=0;
                            f=0;
                            g=0;
                            s=0;
                            ch=n1[q];
                            //cout<<;
                            if(v.size()==0)
                            v.push_back(ch);
                            
                            else
                            {
                                for(i=0;i<c;i++)
                                {
                                                for(j=0;j<2;j++)
                                                {
                                                                if(c1[i][j]==ch)
                                                                {
                                                                               f=1;
                                                                if(j==1)
                                                                {
                                                                        if(c1[i][0]==v.back())
                                                                        flag=1;
                                                                        pt=i;
                                                                        break;
                                                                }
                                                                else
                                                                    {
                                                                        if(c1[i][1]==v.back())
                                                                        flag=1;
                                                                        pt=i;
                                                                        break;
                                                                    }
                                                                }
                                                }
                                                f=0;
                                
                                                if(flag==1)
                                                break;
                                }
                                if(flag==1)
                                {
                                           v.pop_back();
                                           v.push_back(c1[pt][2]);
                                }
                                else
                                {
                                    for(i=0;i<d;i++)
                                    {
                                                    for(j=0;j<2;j++)
                                                    {
                                                                    if(ch==d1[i][j])
                                                                    {
                                                                                    flag1=1;
                                                                                    if(j==1)
                                                                                    {z[s]=d1[i][0];
                                                                                    s++;
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        z[s]=d1[i][1];
                                                                                        s++;
                                                                                    }
                                                                    }
                                                    }
                                    }
                                    if(flag1==1)
                                    {
                                    for(i=0;i<s;i++)
                                    {
                                                    for(j=0;j<v.size();j++)
                                                    {
                                                                           if(z[i]==v[j])
                                                                           {
                                                                                         found=1;
                                                                                         v.clear();
                                                                           }
                                                    }
                                    }
                                    }
                                }//cout<<"flags"<<flag<<found<<endl;
                                if(flag==0 && found==0)
                                v.push_back(ch);
                            }
                             
            }
            cout<<"Case #"<<w<<": [";
            for(i=0;i<v.size();i++)
            {
            if(i!=(v.size()-1))
            cout<<v[i]<<", ";
            else
            {cout<<v[i];
            }
            }
            cout<<"]";
            cout<<endl;
            t--;
            w++;
    }
            return 0;
}
                                                            
                            
                            
            
            
            
