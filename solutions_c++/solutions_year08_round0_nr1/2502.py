#include<iostream>
#include<map>
#include<string>
using namespace std;
main()
{
      int test,cas;
      cin>>test;
      map<string,int> map1;
      cas=1;
      while(test--)
      {
       int n,i,state[101];
       cin>>n;
   
       string a;
       map1.clear();
       memset(&state,0,sizeof(state));
       for(i=0;i<=n;i++)
       {
        fflush(stdin);
        getline(cin,a,'\n');
	if(i==0)
	continue;
        map1.insert(pair<string,int> (a,i));
       }
       int q;
       cin>>q;
       int count=0,answer=0;
       for(i=0;i<=q;i++)
       {
        fflush(stdin);
	getline(cin,a,'\n');
       	if(i==0)
	continue;
	int pst=map1.find(a)->second;
                if(state[pst]==0)
        {
         count++;
         state[pst]=1;
        }
        if(count==n)
        {
         answer++;
         memset(&state,0,sizeof(state));
         state[pst]=1;
         count=1;
        }
       }
       cout<<"Case #"<<cas<<": "<<answer<<endl;
       cas++;
      }
}
