#include<iostream>
using namespace std;
bool pre(char c,char ch[500][500],int j);
int main()
{
    int l,d,n,i,c2=1;
    cin>>l>>d>>n;
    string dict[5010];
    for(i=0;i<d;i++)
      cin>>dict[i];//cout<<dict[i]<<endl;}
    while(n--)
    {
       string s;
       int j,k,m=0,count=0;
       char ch[500][500]={0};
       cin>>s;
       //cout<<s<<endl;
       for(j=0,m=0;s[j];j++,m++)
        {
         k=0;
         if(s[j]=='(')
            {
             j++;
             while(s[j]!=')')
                ch[m][k++]=s[j++];  
            
             }
         else if(s[j]==')') continue;    
        else  ch[m][k]=s[j];
       }
     /* for(i=0;i<l;i++)
        {for(j=0;ch[i][j];j++)  
             cout<<ch[i][j]<<" ";
         cout<<endl;
        } */   
      if(m<l) {cout<<"Case #"<<c2<<": "<<count<<endl;c2++;continue;}  
       for(i=0;i<d;i++)
         {
           for(j=0;j<m;j++)
            if(!pre(dict[i][j],ch,j)) break;
           if(j<m) continue;
           if(j==m) {count++;}
         }
      cout<<"Case #"<<c2<<": "<<count<<endl;c2++;
    }       
     return 0;
}
bool pre(char c,char ch[500][500],int j)
{
     int i;
     for(i=0;ch[j][i];i++)
       if(c==ch[j][i]) return true;
     return false;
}  
