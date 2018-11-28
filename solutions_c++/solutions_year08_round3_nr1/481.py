#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef long long LL;

int main(int argc, char *argv[])
{
  int cases, N;

  LL P, K, L, i, temp, presses, key, pos;
  //bool flag;

  cin>>cases;
  for(N=1;N<=cases;N++)
  {
   vector<LL> freq;

   cin>>P>>K>>L;

   LL map[K][P];

   for(i=0;i<L;i++)
   {
    cin>>temp;
    freq.push_back(temp);
   }

   //flag=false;
   presses=0;

   sort(freq.begin(), freq.end());
   reverse(freq.begin(), freq.end());

   i=0;
   for(pos=1;pos<=P&&i<L;pos++)
   {
//cout<<endl<<"Position #"<<pos<<":";
    for(key=0;key<K&&i<L;key++)
    {
//cout<<" "<<freq[i];
     presses+=freq[i++]*pos;
    }
   }

   //if(i==L) flag=true; //all keys have been mapped

   cout<<"Case #"<<N<<": ";
   //if(flag)
    cout<<presses<<endl;
   //else
   // cout<<"Impossible"<<endl;

  }
  cin.get(); cin.get();
  return 0;
}
