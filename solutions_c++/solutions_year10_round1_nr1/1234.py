#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

void split(vector<string>& vs, string& s, char c)
{
 for(int i = 0; i < s.size();)
 {
  string ss;

  int j = s.find(c, i);

  if (j - 1 < i)
  {
   ss = s.substr(i, s.size() - i);

   vs.push_back(ss);

   break;
  }

  ss = s.substr(i, j - i);

  i = j + 1;

  vs.push_back(ss);
 }
};

void rotate(vector<string>& vs)
{
 vector<string>::iterator iter = vs.begin();

  while(iter!=vs.end())
  {
   string& s = *iter;

   string ns;

   int i = 0;

   for(; i < s.size(); i++)
   {
    if(s[i]=='R'||s[i]=='B')
    {
     ns += s[i];
    }
   }

   int span = s.size() -  ns.size();

   string ps;

   int k = 0;

   while(k<span)
   {
    ps+=".";
    k++;
   }

   ns = ps + ns;

   *iter = ns;

   iter++;
  }
};

int calc(vector<string>& vs, int k)
{
 bool findb = false;
 bool findr = false;
 string bb;
 string rr;
 int i = 0;
 while(i<k)
 {
  bb += "B";
  rr += "R";
  i++;
 }

   vector<string>::iterator iter = vs.begin();

  while(iter!=vs.end())
  {
   string& ss = *iter;

  //cout<<ss<<endl;
  if(!findb)
  {
   int l = ss.find(bb, 0);
   if (l>0)
   {
     findb = true;
   }
  }
  if(!findr)
  {
    int l = ss.find(rr, 0);
   if (l>0)
   {
     findr = true;
   }
  }

   iter++;
  }

 for(int j = 0; j < vs.size(); j++)
 {
  for(int t = 0; t < vs.size() && vs.size()-t>=bb.size();t++)
  {

   //cout<<vs[t][j]<<endl;
   if(!findb && vs[t][j] == 'B')
   {
      string ts;
      int tt = t;
      while(tt-t<bb.size())
      {
       ts += vs[tt][j];
       tt++;
      }
      if(ts == bb)
      {
       findb = true;
      }
   }
   if(!findr && vs[t][j] == 'R')
   {
      string ts;
      int tt = t;
      while(tt-t<rr.size())
      {
       ts += vs[tt][j];
       tt++;
      }
      if(ts == rr)
      {
       findr = true;
      }
   }//if
  }//for
 }//for


 for(int n = vs.size()-1; n>=0;n--)
 {
  for(int m = vs.size()-1;m>=0;m--)
  {
   if(vs[n][m] == '.')
   {
      continue;
   }
   if(!findb && vs[n][m] == 'B')
   {
    if(!findb &&
     n + 1 >= bb.size() &&
      vs.size() - m >= bb.size() &&
       vs[n-1][m+1] == 'B')
    {
     int nn = n;
     int mm = m;
     string mns;
     int cc = 0;
     while(cc<bb.size())
     {
      mns+=vs[nn--][mm++];
      //cout<<"****************"<<endl;
      cc++;
     }
     if(mns == bb)
     {
      findb = true;
     }//if
    }//if
    if(!findb && vs.size() - n >> bb.size() && vs.size() - m >= bb.size() && vs[n+1][m+1] == 'B')
    {
     int nn = n;
     int mm = m;
     string mns;
     int cc = 0;
     while(cc<bb.size())
     {
      mns+=vs[nn++][mm++];
           // cout<<"****************"<<endl;
      cc++;
     }
     if(mns == bb)
     {
      findb = true;
     }//if
    }//if
   }
   if(!findr && vs[n][m] == 'R')
   {
     if(!findr && n + 1>= rr.size() && vs.size() - m >= rr.size() && vs[n-1][m+1] == 'R')
    {
     int nn = n;
     int mm = m;
     string mns;
     int cc = 0;
     while(cc<rr.size())
     {
      mns+=vs[nn--][mm++];
           cout<<"****************"<<endl;
      cc++;
     }
     if(mns == rr)
     {
      findr = true;
     }//if
    }//if
    if(!findr && vs.size() - n >= rr.size() && vs.size() - m >= rr.size() && vs[n+1][m+1] == 'R')
    {
     int nn = n;
     int mm = m;
     string mns;
     int cc = 0;
     while(cc<rr.size())
     {
      mns+=vs[nn++][mm++];
       cout<<"****************"<<endl;
      cc++;
     }
     if(mns == rr)
     {
      findr = true;
     }//if
    }//if
   }
  }
 }

 if(!findb&&!findr)
 {
  return 0;
 }
 if(findb&&findr)
 {
  return 3;
 }
 if(findb)
 {
  return 1;
 }
 if(findr)
 {
  return 2;
 }
};
     /*
int main(int argc, char *argv[])
{
 int i;

 vector<string> vs;

 vs.push_back(".......");
 vs.push_back(".......");
 vs.push_back(".......");
 vs.push_back("...R...");
 vs.push_back("...BB..");
 vs.push_back("..BRB..");
 vs.push_back(".RRBR..");

 rotate(vs);

  vector<string>::iterator iter = vs.begin();

  while(iter!=vs.end())
  {
   cout<<*iter<<endl;

   iter++;
  }

  int re = calc(vs, 2);

  cout << re << endl;

  cin >> i;
}  */

int main(int argc, char *argv[])
{
 int tst;

 ifstream input("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\R1\\1\\input.in");

 ofstream output("C:\\Users\\randysheriff\\Desktop\\GoogleJam\\R1\\1\\output.out");

 int count;

 int n ,k;

 input >> count;

 int i = 0;

 while(i < count)
 {
  i++;

  input >> n;

  input >> k;

  cout << k <<endl;
  vector<string> vs;

  int ln = 0;

  while(ln < n)
  {
   string s;

   input >> s;

   vs.push_back(s);

   ln++;
  }

  rotate(vs);

  int re = calc(vs, k);

  output << "Case #" << i << ": ";

  if(re == 0)
  {
   output << "Neither";
  }
  else if(re == 1)
  {
   output << "Blue";
  }
  else if(re == 2)
  {
   output << "Red";
  }
  else
  {
   output << "Both";
  }

  output << endl;

  if(i ==2 )
  {
  vector<string>::iterator iter = vs.begin();

  while(iter!=vs.end())
  {
   cout<<*iter<<endl;

   iter++;
  }
   }
  cout<<"---------------------------------------"<<endl;
 }
 cin >>tst;
}

         /*
int main(int argc, char *argv[])
{
  int i;

  string s = "adsf fasdf asdfa";

  vector<string> vs;

  split(vs, s, ' ');

  vector<string>::iterator iter = vs.begin();

  while(iter!=vs.end())
  {
   cout<<*iter<<endl;
   iter++;
  }

  cin >> i;

  return 0;
}       */
