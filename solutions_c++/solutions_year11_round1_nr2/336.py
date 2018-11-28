#include <iostream>


using namespace std;

int main()
{
  int N;
  cin>>N;
  for (int i=1;i<=N;i++)
  {
    int n,m;
    cin>>n>>m;
    string d[n],l[m];
    for (int j=0;j<n;j++)
      cin>>d[j];
    for (int j=0;j<m;j++)
      cin>>l[j];
    
    int z=99999;
    
    
    cout<<"Case #"<<i<<":";
    
    for (int i=0;i<m;i++)
    {
      //l[i] current list
      z=-1;string gg;
      for (int j=0;j<n;j++)
      {
        //d[j] chosen word
        string ans=d[j];
        string cur="";
        int cz=0;
        for (int k=0;k<ans.size();k++)
          cur+=" ";//cout<<cur<<endl;

        
        for (int k=0;k<26;k++)
          for (int u=0;u<n;u++)
          {
            //l[i][k] chosen char
            bool g=0,h=1;
            if (ans.size()!=d[u].size())
              continue;
            for (int o=0;o<ans.size();o++)
            {
              char x=d[u][o];
              if (l[i][k]==x)
                g=1;
              for (int e=0;e<k;e++)
                if (cur[o]==' '&&x==l[i][e])
                  h=0;
              if (x!=cur[o]&&cur[o]!=' ')
                h=0;
            }
           // cout<<l[i][k]<<' '<<g<<' '<<h<<endl;
            if (g&&h)
            {
              bool x=0;
              for (int o=0;o<ans.size();o++)
                if (ans[o]==l[i][k])
                {
                  x=1;
                  cur[o]=ans[o];
                }
              if (x==0)
              {
                
                cz++;
              }
              u=99999;
              if (ans==cur)
              {
                k=99;
                //cout<<d[j]<<' '<<cz<<endl;
                if (cz>z)
                {
                  z=cz;
                  gg=d[j];
                }
              }
            }
        //    cout<<cz<<endl;
          }//end for u
        
      }//end for j
      //cout<<z<<' '<<gg<<endl;
      cout<<' '<<gg;
    }//end for i
    cout<<endl;
    
  }
  return 0;
}

