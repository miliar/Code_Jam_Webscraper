#pragma warning(disable : 4786) 

#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <iostream.h>
#include <assert.h>
#include <algorithm>
using namespace std;


#define BL 1024
char buf[BL];
vector<string> aToken;

struct ttime
{  
  int h;
  int m;

  //ttime(){h=0;m=0;}
  ttime(int a=0, int b=0)
  {
    h = a;
    m = b;
  }

  void add_m( int k)
  {
    h += (m+k)/60;
    m = (m+k)%60;
  }
};

struct tevent
{
  ttime time;
  int event;

  tevent( ttime t, int e)
  {
    time.h = t.h;
    time.m = t.m;
    event  = e;
  }
  	
  bool operator < (tevent& rhs)
  {
    if( time.h < rhs.time.h) return true;
    if( time.h> rhs.time.h) return false;

    if( time.m< rhs.time.m) return true;
    if( time.m>rhs.time.m) return false;

    if( event < rhs.event) return true;
    //if( event > rhs.event) return false;
    return false;
  }

};

vector< tevent > a_event, b_event;

void toknize(char *p, char *del)
{
  aToken.clear();

  char *tok = strtok(p,del);

  if(tok != NULL)
    aToken.push_back( tok );  
  
  while( tok != NULL )
  {
    tok = strtok( 0 , del);

    if(tok != NULL)
      aToken.push_back( tok );
  }
}

void docase( int &na, int &nb)
{
  int tt;
  int sca, scb;

  cin.getline(buf, BL);
  tt = atoi(buf);

  cin.getline(buf, BL);
  toknize( buf, ": \n\r");
  assert(aToken.size() == 2);

  sca = atoi(aToken[0].c_str());
  scb = atoi(aToken[1].c_str());
  int tc = sca+scb;
  vector< pair<ttime,ttime> > ttime_list;

  
  a_event.clear();
  b_event.clear();

  for( int i=0 ; i<tc; i++)
  {
    cin.getline(buf, BL);
    toknize( buf, ": \n\r");
    assert(aToken.size() == 4);

    ttime ts(atoi(aToken[0].c_str()) , atoi(aToken[1].c_str()));
    ttime ta(atoi(aToken[2].c_str()) , atoi(aToken[3].c_str()));
    ta.add_m(tt);

    if( i< sca)
    {
      a_event.push_back( tevent(ts,1) );
      b_event.push_back( tevent(ta,0) ) ;
    }
    else
    {      
      b_event.push_back( tevent(ts,1) ) ;
      a_event.push_back( tevent(ta,0) );
    }
  }

  sort( a_event.begin() , a_event.end());
  sort( b_event.begin() , b_event.end());

  /*
  printf("a\n");
  for( i=0; i<a_event.size() ; i++)
  {
    printf("%d: %d-%d\n", a_event[i].time.h , a_event[i].time.m , a_event[i].event);
  }
  printf("b\n");
  for( i=0; i<a_event.size() ; i++)
  {
    printf("%d: %d-%d\n", b_event[i].time.h , b_event[i].time.m , b_event[i].event);
  }*/

  int ncnt = 0;
  int rcnt = 0;

  for( i=0 ; i<a_event.size() ; i++)
  {
    if(a_event[i].event == 1)
    {
      if(rcnt>0) rcnt--;
      else ncnt++;
    }
    else rcnt++;
  }
  na = ncnt;


  
  ncnt = 0;
  rcnt = 0;

  for( i=0 ; i<b_event.size() ; i++)
  {
    if(b_event[i].event == 1)
    {
      if(rcnt>0) rcnt--;
      else ncnt++;
    }
    else rcnt++;
  }
  nb = ncnt;

}

void main()
{
  int icnt;
  cin.getline(buf, BL);
  icnt = atoi(buf);

  int na;
  int nb;
  for( int i=0 ; i<icnt ; i++)
  {
    docase( na, nb);

    cout <<"Case #" << i+1 <<": " <<na <<" " <<nb <<endl;
    
  }



}