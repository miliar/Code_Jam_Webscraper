
#pragma warning(disable : 4786) 

#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <iostream.h>
#include <assert.h>

using namespace std;

#define BL 1024

vector<string> slist;
vector<string> qlist;

char buf[BL];

int qidlist[1001];
int expmap[1001][101];
int calllist[1001];

int count_switch(int qnum)
{
  if(calllist[qnum]!=-1) return calllist[qnum];

  int min_call = 100000;
  for(int i=0 ; i<slist.size() ; i++)
  {
    if( (expmap[qnum][i] + qnum) >= qlist.size() )
    {
      calllist[qnum] = 0;
      return 0;
    }
    else if(expmap[qnum][i] == 0) continue;
    else
    {
      int call = count_switch(expmap[qnum][i] + qnum)+1;
      
      if(min_call > call )
      {
        min_call = call;
      }
    }
  }
  
  assert(min_call < qlist.size());

  calllist[qnum] = min_call;
  return calllist[qnum];
}

void makemap()
{
  map<string, int> simap;
  map<string, int>::iterator si_it;
  for(int i=0 ; i<slist.size() ; i++)
  {
    simap.insert( make_pair( slist[i], i) );
  }

  for( i=0 ; i<qlist.size() ; i++)
  {
    si_it = simap.find(qlist[i]);
    assert(si_it != simap.end());

    qidlist[i] = si_it->second;
  }

  int j , k;
  for(i=0 ; i<qlist.size(); i++ )
  {  
    for( j=0 ; j< slist.size() ; j++)
    {
      if( i!=0  && expmap[i-1][j]>0 )
      {
        if(expmap[i-1][j] == 100000)
          expmap[i][j] = 100000;
        else
          expmap[i][j] = expmap[i-1][j]-1;
      }
      else
      {
        for ( k = i ; k<qlist.size() ; k++)
        {
          if( qidlist[k] == j )
          {
            expmap[i][j] = k-i;
            break;
          }
          expmap[i][j] = 100000;
        }
      }
    }
  }

  /*
  printf("-------------------------\n");
  for( i=0 ; i<qlist.size() ; i++)
  {
    printf("%6d:", i);
    for( j=0 ; j<slist.size() ; j++)
    {
      printf("%6d", expmap[i][j]);

    }
    printf("\n");
  }*/

}

void docase()
{  
  int scnt;
  int qcnt , i;

  cin.getline(buf, BL);
  scnt = atoi(buf);
  
  slist.clear();    
  qlist.clear();
  
  for(i=0 ; i<scnt ; i++ )
  {
    cin.getline( buf, BL);      
    slist.push_back(buf);      
  }

  cin.getline(buf, BL);
  qcnt = atoi(buf);

  for( i=0 ; i<qcnt ; i++)
  {
    cin.getline(buf , BL);
    qlist.push_back(buf);
  }

  makemap();
}

void main()
{
  int icnt;

  cin.getline(buf, BL);
  icnt = atoi(buf);

  int i;
  for(i=0 ; i<icnt; i++)
  {     
    docase();
    
    memset(calllist , -1, sizeof(int) *1000);
    cout << "Case #" << i+1 << ": " << count_switch(0) << endl;
  }

}
