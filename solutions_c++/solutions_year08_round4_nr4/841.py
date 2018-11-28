#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> P;

int main()
{
   freopen("D-small-attempt0.in","r",stdin);
   freopen("test.out","w",stdout);
   int N;
   cin>>N;
   for(int tc=1;tc<=N;tc++) {
      int k;
      cin>>k;
      string S;
      cin>>S;
      int size=S.size();

      P.clear();

      int ret=(1<<30);

      for(int i=0;i<k;i++) {
         P.push_back(i);
      }
      do {
         //string temp=S;
         string res="";
         for(int i=0;i<size;i+=k) {
            string cur="";
            for(int j=i;j<i+k;j++) cur+=S[j];
            string str(k,' ');
            for(int a=0;a<k;a++) {
               str[a]=cur[P[a]];
            }
            res+=str;


         }
         int count=1;
         //char prev=res[0];
         for(int i=1;i<res.size();i++) {
            if(res[i]==res[i-1]) {
               continue;
            }
            else count++;
         }

         ret=min(count,ret);
      }while(next_permutation(P.begin(),P.end()));

      cout<<"Case #"<<tc<<": "<<ret<<endl;

   }
   return 0;
}

