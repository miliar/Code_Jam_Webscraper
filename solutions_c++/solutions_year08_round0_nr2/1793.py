#include <iostream>
#include <vector>

using namespace std;


struct t{
  int start,end;
  char station;
};

bool operator<(const t&t1,const t&t2)
{
  if(t1.start!=t2.start)
    return t1.start<t2.start;
  
  return t1.end<=t2.end;
}

int convert(const string&s)
{
  int ret=0;

  for(int i=0;i<s.size();++i)
    {
      if(i!=2)
	{
	  ret*=10;
	  ret+=s[i]-'0';
	}
    }

  return ret;
}

int main()
{

  int casenum;
  
  cin>>casenum;
  

  int caseno = 0;

  while(casenum--){
    int turnaround;
    cin>>turnaround;
    
    int na,nb;
    cin>>na>>nb;

    string s,e;

    vector<t>tasks;

    while(na--)
      {
	cin>>s>>e;
	t temp;
	temp.start=convert(s);
	temp.end=convert(e);
	temp.station='A';
	//	cerr<<'A'<<temp.start<<','<<temp.end<<endl;
	tasks.push_back(temp);
      }

    while(nb--)
      {
	cin>>s>>e;
	t temp;
	temp.start=convert(s);
	temp.end=convert(e);
	temp.station='B';
	//	cerr<<'B'<<temp.start<<','<<temp.end<<endl;
	tasks.push_back(temp);
      }

    sort(tasks.begin(),tasks.end());

    vector<int>availA,availB;

    int usedA,usedB;
    usedA=usedB=0;
    
    for(int i=0;i<tasks.size();++i)
      {
	bool allocated = false;
	

	if(tasks[i].station=='A')
	  {

	    vector<int>::iterator j;

	    for(j=availA.begin();j!=availA.end();++j)
	      {
		if(*j<=tasks[i].start)
		  {
		    availA.erase(j);
		    allocated = true;
		    break;
		  }
	      }
	    
	    if(!allocated)
	      {
		usedA++;
	      }

	    availB.push_back(tasks[i].end+turnaround);
	  }
	else
	  {
	    vector<int>::iterator j;
	    for(j=availB.begin();j!=availB.end();++j)
	      {
		if(*j<=tasks[i].start)
		  {
		    availB.erase(j);
		    allocated=true;
		    break;
		  }
	      }

	    if(!allocated)
	      {
		usedB++;
	      }

	    availA.push_back(tasks[i].end+turnaround);
	    
	  }
      }



    
    cout<<"Case #"<<++caseno<<": "<<usedA<<" "<<usedB<<endl;
    




  }// outmost while

  return 0;
}
