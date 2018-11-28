#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>

using namespace std;
int main()
{
  
   int l,d,n;

    freopen("alien.out","w",stdout);
    freopen("alien.in","r",stdin);

   scanf("%d %d %d",&l,&d,&n);     

  string words[d];
  string pattern;
   for(int i=0;i<d;i++)     
    {
     cin>>words[i];
    }
  

    for(int i=0;i<n;i++) 
     {
       cin>>pattern;
       string allowed[l];

          for(int k=0;k<l;k++)
               allowed[k]="";

//          replace(pattern.begin(),pattern.end(),'(',' ');
//          replace(pattern.begin(),pattern.end(),')',' ');
      
       int j=0;
       int ll=0;
       while(pattern[j]!='\0')
        {
           if(pattern[j]=='(')
            {
              j++;
                while(pattern[j]!=')')
                 {
                   allowed[ll]+=pattern[j];
                   j++;
                 }
              ll++;
              j++;
            }
           else
            {
             allowed[ll++]+=pattern[j];
             j++;
            }
        }
 //          stringstream ss;
 //       ss<<pattern;

        for(int k=0;k<l;k++)     
       {
  //         ss>>allowed[k];
          sort(allowed[k].begin(),allowed[k].end());
      //     cout<<allowed[k]<<endl;
         }

       int ans=0;

           for(int j=0;j<d;j++)
            {
              bool ok=true;
                for(int k=0;k<l;k++)
                 {
                   if(binary_search(allowed[k].begin(),allowed[k].end(),words[j][k])==false)                  
                     ok=false;
                 }
              if(ok)
                ans++;
            }

          printf("Case #%d: %d\n",i+1,ans);
     }

  return 0;
}
