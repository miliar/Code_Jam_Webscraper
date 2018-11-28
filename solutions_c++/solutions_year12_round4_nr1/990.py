#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<iterator>
#include<time.h>
#include<iomanip>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll d[60002];
ll l[60002];
ll n;
ll r[60002];

int main()
{
    fstream input,output;
    //input.open("test.in",ios::in); output.open("test.out",ios::out);
    //input.open("A-small-attempt0.in",ios::in); output.open("A-small-0.out",ios::out);
    input.open("A-large.in",ios::in); output.open("A-large-0.out",ios::out);   
    
    int case_id,total_case;
    
    input>>total_case;  
    
    int i,j,k;
    for(case_id=1;case_id<=total_case;case_id++)
    { 
      input>>n;
      for(i=1;i<=n;i++)
      {
          input>>d[i]>>l[i];
          r[i]=-1;
      }
      input>>d[n+1];
      l[n+1]=0;
      r[n+1]=-1;
      d[n+2]=INF;
      //cout<<d[1];
      r[1] = d[1];
      for(i=1;i<=n;i++)
      {
         for(j=i+1;j<=n+1;j++)
         {
        //     cout<<"*";
          //   cout<<d[i]+r[i]<<endl;
            // cout<<d[j]<<endl;
             if(d[i]+r[i]<d[j]) break;
             ll temp = min(l[j], d[j]-d[i]);
             //cout<<temp;
             if(temp>r[j]) 
             {
               //  cout<<"*";
                 r[j]=temp;
             }
             
         }
      }
      
      output<<"Case #"<<case_id<<": ";
    //      output<<ans;
      output<<(r[n+1]==0?"YES":"NO");
      output<<endl;
    }
    cout<<1;
    cin>>case_id;
    return 0;
}
