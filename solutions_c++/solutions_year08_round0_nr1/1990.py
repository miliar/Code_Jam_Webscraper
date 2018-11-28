#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

struct engcheck {
string name;
char found;
};

int main (int argc, char* argv[])
{
//  cout << argc << endl;
//  cout << argv[1] << endl;

  ifstream fin (argv[1]);
  string l;

  if (fin.is_open())
  {
    getline(fin, l);
    istringstream buf(l);
    int samples;
    buf >> samples;
//    cout << "number of samples = " << samples << endl;

    for (int j=0; j < samples; j++)
    {
//      cout << " !!!!!!! Case " << j << endl;
      int result = 0;

      getline(fin, l);
      int engine;
      istringstream buf1(l);
      buf1 >> engine;
//      cout << "number of engines = " << engine << endl;
      vector<string> eng;

      for (int i=0; i < engine; i++)
      {
        getline(fin, l);
//        cout << l << endl;
        eng.push_back(l);
      }

      getline(fin, l);
      int query;
      istringstream buf2(l);
      buf2 >> query;
//      cout << "number of queries = " << query << endl;
      vector<string> que;

      for (int i=0; i < query; i++)
      {
        getline(fin, l);
//        cout << l << endl;
        que.push_back(l);
      }

      // processing
      int counter = 0;
      vector<string> eng2(eng);
      while (que.size() > 0)
      {
        int k=0; 
        while (k < eng2.size())
        {
          // found a match
          if (que.front().compare(eng2.at(k)) == 0)
          {
            if (eng2.size() == 1)
            {
//            cout << "switch" << endl;
              counter = counter + 1;        
            // copy engine
//            cout << "******** reload *******" << endl;
              eng2.clear();
              for (int m=0; m < eng.size(); m++)
                eng2.push_back(eng.at(m));
              k = 0;
            }
            else
            {
//          cout << "erase " << que.front() << " " << eng2.at(k) << " at " << k << " total size = " << eng2.size() << endl;
              eng2.erase(eng2.begin()+k);
              k = 0;
              if (que.size() == 1)
                break;
              else
                que.erase(que.begin());
            }
          }
          else 
            k++;
/*
      cout << " -- engines --" << endl;
      cout << "engine size = " << eng2.size() << " ";
      for (int i=0; i < eng2.size(); i++)
        cout << eng2.at(i) << "  ";
      cout << endl;
      cout << " ** queries **" << endl;
      cout << "query size = " << que.size() << " ";
      for (int i=0; i < que.size(); i++)
        cout << que.at(i) << "  ";
      cout << endl;
*/
        }
//cout << "remove query " << que.front() << endl;
        que.erase(que.begin());
      
      }
      // output
      cout << "Case #" << j+1 << ": " << counter << endl;

/*
      cout << " -- engines --" << endl;
      for (int i=0; i < eng.size(); i++)
        cout << eng.at(i) << endl;
      cout << " -- queries --" << endl;
      for (int i=0; i < que.size(); i++)
        cout << que.at(i) << endl;
*/
    }

    fin.close();
  }

  return 0;
}
