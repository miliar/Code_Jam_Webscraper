#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

#define pii pair<int,int>
#define piii pair<int,pii>

int main()
{
   freopen("B-small-attempt5.in","r",stdin);
   //freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);

   int N, NA, NB, t, Count=0;
   
   string strin;
   
   getline(cin,strin);
   sscanf(strin.c_str(),"%d",&N);
   
   for(int i=0;i<N;++i)
   {
      getline(cin,strin);
      sscanf(strin.c_str(),"%d",&t);

      getline(cin,strin);
      sscanf(strin.c_str(),"%d %d",&NA,&NB);
      
      int cA = 0, cB = 0;
      vector<piii> T(NA+NB);
      vector<bool> u(NA+NB,true);
      //vector<pii> B(NA+NB,pii(0,-1));
      //vector<pii> TA(NA), TB(NB);
      //vector<bool> uA(NA,true), uB(NB,true);

      for(int j=0;j<NA;++j)
      {
         int a,b,c,d;
         getline(cin,strin);
         sscanf(strin.c_str(),"%2d:%2d %2d:%2d",&a,&b,&c,&d);
         T[j] = piii(60*a+b,pii(60*c+d,0));
      }

      for(int j=0;j<NB;++j)
      {
         int a,b,c,d;
         getline(cin,strin);
         sscanf(strin.c_str(),"%2d:%2d %2d:%2d",&a,&b,&c,&d);
         T[NA+j] = piii(60*a+b,pii(60*c+d,1));
      }
      
      sort(T.begin(),T.end());

      //cA = cB = 0;
      while(true)
      {
         vector<pii> B(NA+NB,pii(0,-1));
         for(int j=NA+NB-2;j>=0;--j)
         {
            if(!u[j]) continue;
            for(int k=j+1;k<NA+NB;++k)
            {
               if(!u[k]) continue;
               if((T[j].second.first+t<=T[k].first) && (T[k].second.second!=T[j].second.second))
               {
                  if(B[k].first+1>B[j].first)
                  {
                     B[j] = pii(B[k].first+1,k);
                  }
               }
            }
         }
         int maxi = -1, pos;
         for(int j=0;j<NA+NB;++j)
         {
            if(!u[j]) continue;
            if(B[j].first>maxi)
            {
               maxi = B[j].first;
               pos = j;
            }
         }
         if(maxi==0 || maxi==-1) break;
         if(T[pos].second.second==0) ++cA; else ++cB;
         while(pos!=-1){
            u[pos]=false;
            pos=B[pos].second;
            }
         //cout << "--" << endl;
         //for(int j=0;j<NA+NB;++j)
         //{
         //   cout << T[j].first << " " << T[j].second.first << " " << B[j].first << " " << B[j].second << endl;
         //}
      }
      for(int j=0;j<NA+NB;++j)
      {
         if(u[j])
         {
            if(T[j].second.second==0) ++cA; else ++cB;
         }
      }
      ++Count;
      cout << "Case #" << Count << ": " << cA << " " << cB << endl;
   }
   
   return 0;
}
