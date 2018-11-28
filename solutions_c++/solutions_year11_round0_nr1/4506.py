#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
using namespace std;

typedef struct{
  vector< pair< char,int > > vpci;
  int idxo;
  int idxb;
  int idxall;
}seq;

void performseq(seq &sq)
{
  cout << sq.idxo << " - " << sq.idxb << endl;
  for(int i=0;i<sq.vpci.size();++i)
  {
    cout << sq.vpci[i].first << "-" << sq.vpci[i].second << " : ";
  }
  cout << endl;
}

void setnextidx(seq &sq,char r)
{
  if (r=='O')
  {
    bool found=false;
	int i;
	for(i=sq.idxo+1;i<sq.vpci.size() && !found;++i)
	{
	  if (sq.vpci[i].first==r)
	  {
	    found=true;
		sq.idxo=i;
	  }
	}
  }
  else if (r=='B')
  {
    bool found=false;
	int i;
	for(i=sq.idxb+1;i<sq.vpci.size() && !found;++i)
	{
	  if (sq.vpci[i].first==r)
	  {
	    found=true;
		sq.idxb=i;
	  }
	} 
  }
}

bool isthereway(seq &sq,char r)
{
  seq tempsq=sq;
  if (r=='O')
  {
    setnextidx(tempsq,r);
	if (sq.idxo==tempsq.idxo)
	{
	  return false;
	}
	else
	{
	  return true;
	}
  }
  if (r=='B')
  {
    setnextidx(tempsq,r);
	if (sq.idxb==tempsq.idxb)
	{
	  return false;
	}
	else
	{
	  return true;
	} 
  }
}

typedef struct{
  int now;
  int next;
  bool status;
}halfstate;

typedef struct{
  halfstate o;
  halfstate b;
}state;

void initstate(state &s,seq &sq)
{
  s.o.now=1;
  s.b.now=1;
  seq tempsq=sq;
  setnextidx(tempsq,'O');
  setnextidx(tempsq,'B');
  
  if (tempsq.idxo!=-1)
  {
    s.o.next=tempsq.vpci[tempsq.idxo].second;
  }
  else
  {
    s.o.next=-1;
  }
  if (tempsq.idxb!=-1)
  {
    s.b.next=tempsq.vpci[tempsq.idxb].second;
  }
  else
  {
    s.b.next=-1;
  }
  
  if (sq.vpci[sq.idxall].first=='O')
  {
    s.o.status=true;
	s.b.status=false;
  }
  if (sq.vpci[sq.idxall].first=='B')
  {
    s.o.status=false;
	s.b.status=true;
  }
  
}

void performstate(state &s,seq &sq)
{
  cout << "idxall : " << sq.idxall << endl;
  cout << "O" << s.o.now << " (O" << s.o.next << " , " << s.o.status << ")";
  cout << "     B" << s.b.now << " (B" << s.b.next << " , " << s.b.status << ")" << endl;
}

void nextstate(state &s,seq &sq)
{
//
  if (s.o.status)
  {
    if (s.o.now<s.o.next)
	{
	  s.o.now++;
	}
	else if (s.o.now>s.o.next)
	{
	  s.o.now--;
	}
	else if (s.o.now==s.o.next)
	{
	  sq.idxall++;
	  setnextidx(sq,'O');
	  // cout << "tes\n";
	  if (sq.idxo!=-1)
	  {
	    // cout << "tes1\n";
	    cout << sq.vpci[sq.idxo].second << " - " << s.o.next << endl;
	    if (sq.vpci[sq.idxo].second!=s.o.next)
		{
		  // cout << "tes2\n";
		  s.o.next=sq.vpci[sq.idxo].second;
		}
		else  
		{
		  // cout << "tes3\n";
		  s.o.status=false;
		}
	  }
	}
	
	if (s.b.now<s.b.next)
	{
	  s.b.now++;
	}
	else if (s.b.now>s.b.next)
	{
	  s.b.now--;
	}
	else if (s.b.now==s.b.next)
	{
	}
	
	if (sq.idxall<sq.vpci.size())
	{
	if (sq.vpci[sq.idxall].first=='O')
	{
	  s.o.status=true;
	  s.b.status=false;
	}
	if (sq.vpci[sq.idxall].first=='B')
	{
	  s.o.status=false;
	  s.b.status=true;
	}
	}
	else
	{
	  s.o.status=false;
	  s.b.status=false;
	}
	
	return;
  }
//

//
  if (s.b.status)
  {
    if (s.b.now<s.b.next)
	{
	  s.b.now++;
	}
	else if (s.b.now>s.b.next)
	{
	  s.b.now--;
	}
	else if (s.b.now==s.b.next)
	{
	  sq.idxall++;
	  setnextidx(sq,'B');
	  // cout << "tes\n";
	  if (sq.idxb!=-1)
	  {
	    if (sq.vpci[sq.idxb].second!=s.b.next)
		{
		  s.b.next=sq.vpci[sq.idxb].second;
		}
		else  
		{
		  s.b.status=false;
		}
	  }
	}
	
	if (s.o.now<s.o.next)
	{
	  s.o.now++;
	}
	else if (s.o.now>s.o.next)
	{
	  s.o.now--;
	}
	else if (s.o.now==s.o.next)
	{
	}
	
	if (sq.idxall<sq.vpci.size())
	{
	if (sq.vpci[sq.idxall].first=='O')
	{
	  s.o.status=true;
	  s.b.status=false;
	}
	if (sq.vpci[sq.idxall].first=='B')
	{
	  s.o.status=false;
	  s.b.status=true;
	}
	}
	else
	{
	  s.o.status=false;
	  s.b.status=false;
	}
	
	return;
  }
//

}

void solveone(seq &rseq,int &tpath)
{
  rseq.idxo=-1;
  rseq.idxb=-1;
  rseq.idxall=0;
  // performseq(rseq);
  state s;
  initstate(s,rseq);
  setnextidx(rseq,'O');
  setnextidx(rseq,'B');
  // performseq(rseq);
  // performstate(s,rseq);
  // cout << "////////\n";
  while (!( (s.o.status==false) && (s.b.status==false)))
  {
    nextstate(s,rseq);
    // performseq(rseq);
    // performstate(s,rseq);
	tpath++;
	// cout << "total : "  << tpath << endl;
  }
  
}

int main()
{

  ifstream fin;
  fin.open("A-large.in");
  
  ofstream fout;
  fout.open("A-large.out");
  
  int i,j,total;//1 = T = 20
  fin >> total;
  for(i=0;i<total;++i)
  {
    seq rseq;
    // rseq.idxo=-1;
    // rseq.idxb=-1;
	// rseq.idxall=0;
    int tone;
	fin >> tone;
	for(j=0;j<tone;++j)
	{
	  char r;
	  fin >> r;
	  int b;
	  fin >> b;
	  pair< char,int > pci;
	  pci.first=r;
	  pci.second=b;
	  rseq.vpci.push_back(pci);
	}
	int t=0;
	
	solveone(rseq,t);
	// cout << "total : " << t << endl;
	fout << "Case #" << i+1 << ": " << t << endl;
	// break;
  }
  
  fin.close();
  fout.close();
  return 0;
}
