#include <fstream>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <map>
using namespace std;

bool valid_s (const string& s)
{
  for (const char* p=s.c_str(); *p != 0; ++p)
    if (!isalnum(*p) && *p!=' ')
      return false;
  
  return true;
}

int calc_swth(map<string, bool> s, vector<string> q)
{
  int count = 0;
  for (vector<string>::const_iterator iter=q.begin(); iter!=q.end(); ++iter)
  {
    map<string, bool>::iterator si=s.find(*iter);
    if (si != s.end())
    {
      si->second=false;

      map<string, bool>::iterator mi=s.begin();
      for (; mi!=s.end(); ++mi)
        if (mi->second)
          break;

      if (mi == s.end())
      {
        ++count;
        
        mi=s.begin();
        for (; mi!=s.end(); ++mi)
          if (mi!=si)
            mi->second=true;
      }
    }
  }
  return count;
}

int main (int argc, char* argv[])
{
  map<string, bool> s;
  vector<string> q;
  vector<int> r;

  if (argc < 2) {cout<<"Usage: <task name> <input file>"<<endl; return -1;}

  ifstream inFile;
  inFile.open(argv[1]);
  if (!inFile) {
    cerr << "Unable to open file datafile.txt";
    return 1;   // call system to stop
  }

  inFile>>skipws;

  int n=0;
  inFile>>n;
  if (n<0||n>20) {
    cerr<<"Invalid number of test cases: "<<n<<", aborting..."<<endl;
    return 2;
  }

  for (int i=0; i<n; ++i) {
    // get number of engines
    int ns=0;
    inFile>>ns;
    if (ns<2||ns>100) {
      cerr<<"Invalid number of engines: "<<ns<<", aborting..."<<endl;
      return 3;
    }
    
    // get engines
    char tmp[100];
    memset(tmp, 0, sizeof(tmp));
    inFile.getline(tmp, 100); //escape new line
    for (int j=0; j<ns; ++j) {
      inFile.getline(tmp, 100);
      if (!valid_s(tmp))
      {
        cerr<<"Invalid engines: "<<tmp<<", aborting..."<<endl;
        return 6; //inFile.getline(tmp, 100);
      }

      s[tmp]=true;
    }

    // get number of queries
    int nq=0;
    inFile>>nq;
    if (nq<0||nq>1000) {
      cerr<<"Invalid number of queries: "<<nq<<", aborting..."<<endl;
      return 4;
    }
    
    // get queries
    inFile.getline(tmp, 100); //escape new line
    for (int j=0; j<nq; ++j)
    {
      inFile.getline(tmp, 100);
      string ts(tmp);
      map<string, bool>::iterator si=s.find(ts);
      if (!valid_s(ts) || si==s.end())
      {
        cerr<<"Invalid queries: "<<ts<<", aborting..."<<endl;
        return 5;
        //inFile.getline(tmp, 100);
        //ts = tmp;
        //si=s.find(ts);
      }
      q.push_back(ts);
    }

    r.push_back(calc_swth(s, q));

    s.clear();
    q.clear();
  }

  int i=1;
  for (vector<int>::const_iterator iter=r.begin(); iter!=r.end(); ++iter, ++i)
  {
    cout<<"Case #"<<i<<": ";
    cout<<*iter<<endl;
  }
  return 0;
}


