#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>

using namespace std;



class event
{
  public:
  //0:real arrival, 1:departure
  //0:A, 1:B
    int time,type,place;     
    bool operator< (const event & rhs) const;

};

    
    bool event::operator< (const event & rhs) const
    {
      return (time<rhs.time||(time==rhs.time&&type<rhs.type)||
        (time==rhs.time&&type==rhs.type&&place<rhs.place));
    }; 

int main()
{
 int n;
 cin>>n;

 for(int i=0;i<n;i++)
 {
  cout<<"Case #"<<i+1<<": ";         
  int t;
  cin>>t;
  
  int cura,curb,needa,needb;
  cura=0;
  curb=0; 
  needa=0;
  needb=0;
  int na,nb;
  cin>>na>>nb;
  string s1,s2;
  event e1,e2;
  vector<event> events;
  
  for(int j=0;j<na;j++)
  {
    cin>>s1>>s2;
    e1.time=(s1[4]-'0')+10*(s1[3]-'0')+60*(s1[1]-'0')+600*(s1[0]-'0');
    e1.type=1;
    e1.place=0;

    e2.time=(s2[4]-'0')+10*(s2[3]-'0')+60*(s2[1]-'0')+600*(s2[0]-'0')+t;
    e2.type=0;
    e2.place=1;
    
    events.push_back(e1);
    events.push_back(e2);
  }   
  
  for(int j=0;j<nb;j++)
  {
    cin>>s1>>s2;
    e1.time=(s1[4]-'0')+10*(s1[3]-'0')+60*(s1[1]-'0')+600*(s1[0]-'0');
    e1.type=1;
    e1.place=1;

    e2.time=(s2[4]-'0')+10*(s2[3]-'0')+60*(s2[1]-'0')+600*(s2[0]-'0')+t;
    e2.type=0;
    e2.place=0;  
    
    events.push_back(e1);
    events.push_back(e2);
  }
  sort(events.begin(),events.end());
  
  for(int j=0;j<events.size();j++)
  {
    if(events[j].type==0)
    {  
      if(events[j].place==0)
        cura++;
      else
       curb++;                        
    }
    else 
      if(events[j].place==0)
      { 
        if(cura>0)
         cura--;
        else needa++;
      }
      else
      { 
        if(curb>0)
         curb--;
        else needb++;
      }                
  }
  cout<<needa<<" "<<needb<<endl;  
 }       
}
