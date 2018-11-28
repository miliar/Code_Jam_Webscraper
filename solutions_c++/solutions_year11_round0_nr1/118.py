#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
string LS,RS;
int n;
map<pair<int,int>,int> opt;
int rank[2000000];
int prevPL[2000000];
int prevPR[2000000];
int findit(int p1,int p2)
{
  if(p1==0 && p2==0)
    return 0;
  if(p1==0)
    return p2;
  if(p2==0)
    return p1;
  if(opt.find(make_pair(p1,p2))!=opt.end())
    return opt[make_pair(p1,p2)];
  
  //printf("%d %d\n",p1,p2);
  //printf("%c %c\n",LS[p1],RS[p2]);
  int retv=10000000;
  if(LS[p1]=='M' && RS[p2]=='M')
    {
      int p1p=prevPL[p1];
      int p2p=prevPR[p2];
      
      int d=min(p1-prevPL[p1],p2-prevPR[p2]);
      retv=min(retv,findit(p1-d,p2-d)+d);
    }
  if(LS[p1]=='P')
    {
      int lp=-1;
      int lrank=rank[p1*2];
      int rrank=-1;
      for(int j=p2;j>=1;j--)
	if(RS[j]=='P')
	  {
	    rrank=rank[j*2+1];
	    break;
	  }
      //printf("ranks %d %d\n",lrank,rrank);
      if(lrank>rrank)
	{
	  if(RS[p2]!='M')
	    retv=min(retv,findit(p1-1,p2)+1);
	  else
	    retv=min(retv,findit(p1-1,p2-1)+1);
	}
      else
	{
	  if(RS[p2]!='P')
	    retv=min(retv,findit(p1,prevPR[p2])+p2-prevPR[p2]);
	}
    }
  if(RS[p2]=='P')
    {
      int rrank=rank[p2*2+1];
      int lrank=-1;
      for(int j=p1;j>=1;j--)
	if(LS[j]=='P')
	  {
	    lrank=rank[j*2];
	    break;
	  }
      //printf("ranks %d %d\n",lrank,rrank);
      //
      if(rrank>lrank)
	{
	  if(LS[p1]!='M')
	    retv=min(retv,findit(p1,p2-1)+1);
	  else
	    retv=min(retv,findit(p1-1,p2-1)+1);
	}
      else
	{
	  if(LS[p1]!='P')
	    retv=min(retv,findit(prevPL[p1],p2)+p1-prevPL[p1]);
	}
      
    }
  opt[make_pair(p1,p2)]=retv;
  return retv;

}
int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      cin>>n;
      LS=RS="";
      vector <int> Left,Right;
      vector <int> rankleft,rankright;
      for(int i=1;i<=n;i++)
	{
	  string R;
	  int id;
	  cin>>R;
	  
	  cin>>id;
	  
	  if(R=="O")
	    {
	      Left.push_back(id);
	      rankleft.push_back(i);
	    }
	  else
	    {
	      Right.push_back(id);
	      rankright.push_back(i);
	    }
	}
	     
	  int pos=1;
	  for(int i=0;i<Left.size();i++)
	    {
	      if(Left[i]!=pos)
		{
		  for(int j=min(Left[i],pos)+1;j<=max(Left[i],pos);j++)
		    LS+="M";
		}
	      LS+="P";
	      rank[LS.size()*2]=rankleft[i];
	      pos=Left[i];
	      
	    }
	  pos=1;
	  for(int i=0;i<Right.size();i++)
	    {
	      if(Right[i]!=pos)
		for(int j=min(Right[i],pos)+1;j<=max(Right[i],pos);j++)
		  RS+="M";
	      RS+="P";
	      rank[RS.size()*2+1]=rankright[i];
	      pos=Right[i];
	    }
	  
	  
	
      
	  //cout << LS << endl;
	  //cout << RS << endl;
	      
	  LS="S"+LS;
	  RS="S"+RS;
	  prevPL[0]=0;
	  prevPR[0]=0;
	  for(int i=1;i<LS.size();i++)
	    {
	      if(LS[i]=='P')
		prevPL[i]=i;
	      else
		prevPL[i]=prevPL[i-1];
	    }
	  for(int i=1;i<RS.size();i++)
	    {
	      if(RS[i]=='P')
		prevPR[i]=i;
	      else
		prevPR[i]=prevPR[i-1];
	    }
	  opt.clear();

	  printf("Case #%d: %d\n",t,findit(LS.size()-1,RS.size()-1));

	  

    }

}
