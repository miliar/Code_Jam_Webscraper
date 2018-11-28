#include<iostream>
#include<string.h>

using namespace std;

bool fnd(char ch,string str)
{
        for(int i=0;i<str.size();i++)
        if(str[i]==ch)
        return 1;
        
        return 0;
}

int main()
{
        int i,j,k,d,l,n,c;
        string str,ans;
        
        cin>>l>>d>>n;
        string dict[d];
        string chk[n][l];
        
        for(i=0;i<d;i++)
        cin>>dict[i];
        
        //cout<<"done\n";
        
        for(i=0;i<n;i++)
        {
                cin>>str;
                
                for(k=j=0;j<str.size();j++,k++)
                {
                        if(str[j]=='(')
                        {
                                j++;
                                ans="";
                                while(str[j]!=')')
                                ans+=str[j],j++;
                                
                                chk[i][k]=ans;
                                
                        }
                        
                        else
                        chk[i][k]=str[j];
                        
                        //k++;
                }
                
                //cout<<"next\n";
        }
        
        for(i=0;i<n;i++)
        {
                c=0;
                for(j=0;j<d;j++)
                {
                        for(k=0;k<l;k++)
                        {
                                if(fnd(dict[j][k],chk[i][k]))
                                continue;
                                
                                break;
                        }
                        
                        if(k==l)
                        c++;
                }
                
                
                cout<<"Case #"<<i+1<<": "<<c<<endl;
                
        }
        
        
        return 0;
}
