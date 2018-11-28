#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <set>
using namespace std;

int main()
{
  int t;
  cin>>t;
  
  for(int i=1; i<=t; i++)
  {

    int c;
    cin>>c;
    map< pair<char,char>, char> combs;
    string aux;
    for(int j=0; j<c;j++)
    {
	cin>>aux;
	combs[make_pair(aux[0],aux[1])]=aux[2];
	combs[make_pair(aux[1],aux[0])]=aux[2];
    }
    
    int d;
    cin>>d;
    
    set<pair<char,char> > ops;
    for(int j=0; j<d;j++)
    {
	cin>>aux;
	ops.insert(make_pair(aux[0],aux[1]));
        ops.insert(make_pair(aux[1],aux[0]));
    }
    
    int n;
    cin>>n;
    string query;
    cin>>query;
    string resp="";
    for(int j=0; j<n; j++)
    {
      //cout<<"actu "<<resp<<endl;  
      if(resp.length()==0) 
	  resp+=query[j];
	else
	{
	  if(combs.count(make_pair(resp[resp.length()-1],query[j])))
	  {
	      //cout<<"entra1"<<endl;
	      //cout<<"cambia con "<<combs[make_pair(resp[j-1],query[j])]<<endl;
	      //cout<<"antes "<<resp<<" "<<j<<endl;
	      resp[resp.length()-1]=combs[make_pair(resp[resp.length()-1],query[j])];
	      //cout<<"despues "<<resp<<endl;
	      continue;
	  }
	  else if(combs.count(make_pair(query[j],resp[resp.length()-1])))
	  {
	      //cout<<"entra2"<<endl;
	      //cout<<"cambia con "<<combs[make_pair(query[j],resp[j-1])]<<endl;
	      //cout<<"antes "<<resp<<" "<<resp[j-1]<<endl;
	      resp[resp.length()-1]=combs[make_pair(query[j],resp[resp.length()-1])];
	      //cout<<"se convierte en "<<resp<<endl;
	      continue;
	  }
	  else 
	  {
	      //cout<<"entra3"<<endl;
	      int pos=-1;
	      for(int k=resp.length()-1; k>=0; k--)
	      {
		if(ops.count(make_pair(resp[k],query[j])) || 
		   ops.count(make_pair(query[j],resp[k])))
		{
		    pos=k;
		    break;
		}
	      }
	      //cout<<"pos "<<pos<<endl;
	      if(pos!=-1) 
	      {
		//resp=resp.substr(0,pos);
	        resp="";
	        continue;
	      }
	   }
	   //cout<<"entra4"<<endl;
	   resp+=query[j];
	}
	
    }
    
    cout<<"Case #"<<i<<": [";
    for(int j=0; j<resp.length(); j++)
      if(j==0) cout<<resp[j];
      else cout<<", "<<resp[j];
    cout<<']'<<endl;
    //cout<<resp<<endl;
  }
  
  return 0;
}