#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main()
{
   freopen("A-small-attempt0.in","r",stdin);
   freopen("A.out","w",stdout);
   
   int N, S, Q, Count=0;
   string strin;
   
   getline(cin,strin);
   sscanf(strin.c_str(),"%d",&N);
   
   for(int i=0;i<N;++i)
   {
      int mini, lastmini;
      
      getline(cin,strin);
      sscanf(strin.c_str(),"%d",&S);
      vector<string> Se(S,"");
      for(int j=0;j<S;++j)
         getline(cin,Se[j]);
      
      getline(cin,strin);
      sscanf(strin.c_str(),"%d",&Q);
      vector<string> Qu(Q,"");
      for(int j=0;j<Q;++j)
         getline(cin,Qu[j]);
      
      vector< vector<int> > Mat(Q, vector<int>(S, 0) );
      
      mini = 0;
      
      for(int j=0;j<S;++j)
         if(Qu[0]==Se[j])
            Mat[0][j] = -1;
      
      for(int j=1;j<Q;++j)
      {
         int newmini = 999999;
         for(int k=0;k<S;++k)
         {
            if(Qu[j]==Se[k])
            {
               Mat[j][k] = -1;
               continue;
            }
            if(Mat[j-1][k] == -1) Mat[j][k] = mini + 1;
            else Mat[j][k] = min(Mat[j-1][k], mini + 1);
            newmini = min(Mat[j][k], newmini);
         }
         mini = newmini;
      }

      ++Count;
      cout << "Case #" << Count << ": " << mini << endl;     
   }
   return 0;   
}
