#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
  int L,D,N,i,c=0;
  cin>>L>>D>>N;
  vector<string> dict(D);
  for(int i=0;i<D;i++)
    cin>>dict[i];
  //  cout<<"dict over\n";
  for(int kk=0;kk<N;kk++)
    {
      c=0;
      string inp,parse;
      cin>>inp;
      parse="";
      vector<string> asd;
      for(i=0;i<inp.size() && inp[i]!='(';i++)
	{parse=inp[i];asd.push_back(parse);}
      /*      if(parse.length()>0)
	{
	  asd.push_back(parse);
	  c+=parse.length();
	  }*/
      parse="";
      while(c<inp.size() && i!=inp.length())
	{      parse="";
	  if(c==inp.length())continue;
	  int s,e;
	  s=inp.find_first_of("(",c);
	  e=inp.find_first_of(")",c);
	  if(s==string::npos){parse=inp[c];asd.push_back(parse);c++;}
	  else{parse=inp.substr(s+1,e-s-1);
	  c=inp.find_first_of(")",c)+1;
	  asd.push_back(parse);}
	}
      //      for(i=0;i<asd.size();i++)   cout<<asd[i]<<endl;
      c=0; int count=0;
      for(i=0;i<D;i++)
	{c=0;
	  char t;
	  for(int j=0;j<dict[i].length();j++)
	    {
	      if(asd[j].find_first_of(dict[i][j])==string::npos){c=1;break;}
	    }
	  if(c==0)count++;
	}
      cout<<"Case #"<<kk+1<<": "<<count<<endl;
    }
  return 0;
    }
