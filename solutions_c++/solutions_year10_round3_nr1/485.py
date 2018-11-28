#include<iostream>
#include<vector>
#include <utility>

using namespace std;

int main()
{
     freopen("out.txt","w",stdout);
   freopen("A-large.in", "r", stdin);
 int T;
 cin>>T;
// cout<<T<<endl;
 for(int I=1;I<=T;I++)
 {
         int N;
         cin>>N;
      //   cout<<N<<endl;
         vector<pair<int,int> >vp;
         for(int i=0;i<N;i++)
         {
                 int A,B;
                 cin>>A>>B;
                 
                 vp.push_back(make_pair(A,B));
         }
         
         int cnt=0;
         for(int i=0;i<vp.size();i++)
         {
                 for(int j=0;j<vp.size();j++)
                 {
                      //   cout<<vp[i].first<<" "<<vp[j].first <<" "<< vp[i].second <<" "<< vp[j].second<<endl;
                         if(i==j)
                         {
                                 continue;
                         }
                         
                         if(vp[i].first>vp[j].first && vp[i].second > vp[j].second)
                         {
                                 continue;
                         }
                         if(vp[i].first<vp[j].first && vp[i].second < vp[j].second)
                         {
                                  continue;
                         }
                         
                         cnt++;
                 }
         }
         if(cnt>0)cnt/=2;
         cout<<"Case #"<<I<<": "<<cnt<<endl;
 }
    
 //system("pause");
 return 0;   
}
