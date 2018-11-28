#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int note;
	cin>>note;
        for(int caseno=1;caseno<=note;caseno++)
	{
      int nc,no,ns;
      cin>>nc;
      char comb[309][309];
      char s,d,r;
       for(int i=0;i<309;i++)
	      for(int j=0;j<309;j++)
		      comb[i][j]=-1;
     
      for(int i=1;i<=nc;i++)
      {
	      cin>>s>>d>>r;
	      comb[s][d]=r;
	      comb[d][s]=r;
      }
      bool oppos[309][309];
      for(int i=0;i<309;i++)
	      for(int j=0;j<309;j++)
		      oppos[i][j]=false;
      cin>>no;
      for(int i=1;i<=no;i++)
      {
             cin>>s>>d;
	     oppos[s][d]=1;
	     oppos[d][s]=1;
      }
      vector<char> list;
      cin>>ns;
      for(int i=1;i<=ns;i++)
      {
//	      cout<<"QUEUE: ";
//	      for(int j=0;j<list.size();j++)
//		      cout<<list[j]<<" ";
//			      cout<<endl;
          cin>>s;
	  list.push_back(s);
here:
	  if(list.size()>=2)
	  {
              char e1=list[list.size()-1],e2=list[list.size()-2];
	      if(comb[e1][e2]!=-1)
	      {
		      list.pop_back();
		      list.pop_back();
//		      cout<<"ADDED \n"<<comb[e1][e2];
		      list.push_back(comb[e1][e2]);
//		      	      cout<<"QUEUE: ";
//	      for(int j=0;j<list.size();j++)
//		      cout<<list[j]<<" ";
//			      cout<<endl;
        goto here;
	      }
	      for(int j=list.size()-2;j>=0;j--)
		      if(oppos[list[list.size()-1]][list[j]]==1)
		      {list.clear();
//			      cout<<" CLEARED \n";
			      goto here;}
	  }
      }
      cout<<"Case #"<<caseno<<": [";
      for(int i=0;i<list.size();i++)
	      if(i!=list.size()-1)
	      cout<<list[i]<<", ";
	      else
		      cout<<list[i];
      cout<<"]"<<endl;
}
}
