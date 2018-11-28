#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <limits>
#include <set>
#include <list>
#include <map>
//#include <multimap>

#define ABSD(a,b) ((a) >= (b)? (a) - (b): (b) - (a))

#define MKPAIR(a,b) ((a) >= (b)? make_pair((a),(b)): make_pair((b),(a)))

using namespace std;

template<typename T>
ostream& operator<<(ostream &out, list<T> const& l)
{
  typename list<T>::const_iterator it = l.begin(), end = l.end();
  
  out << '[';
  if (it != end)
    out << *it++;
  
  for (; it != end; ++it)
  {
    out << ", " << *it;
  }
  
  out << ']';
  
  return out;
}

list<char> compute( map< pair<char, char>, char> const &  combine, 
                    multimap<char, char> const & destroy, string const & a)
{
  map<char, int> destroy_pair;
  
  list<char> r;
  
  //cout << a << endl;
  if (a.size() < 2)
    return list<char>(a.begin(), a.end());
  
  {
    r.push_back(a[0]);
    pair<multimap<char,char>::const_iterator,multimap<char,char>::const_iterator> ret;
    ret = destroy.equal_range(a[0]);

    multimap<char,char>::const_iterator it =ret.first;
    for (;it != ret.second; ++it)
    {
      //cout << "destroy!" << it->second << endl;
      destroy_pair[it->second]++;
    }
  }
  
  
  for (size_t i = 1; i < a.size(); ++i)
  {
    if (a.size())
    {
      map< pair<char, char>, char>::const_iterator comb_it = combine.find(MKPAIR(a[i], r.back()));
      if (comb_it != combine.end())
      {
       //cout << "h2"<< endl;
        
        {
          //destroy_pair.erase(r.back());
          char rem = r.back();
          pair<multimap<char,char>::const_iterator,multimap<char,char>::const_iterator> ret;
          ret = destroy.equal_range(rem);

          multimap<char,char>::const_iterator it =ret.first;
          for (;it != ret.second; ++it)
          {
            //cout << "destroy!" << it->second << endl;
            //destroy_pair.insert(it->second);
            destroy_pair[it->second]--;
          }
        }
        
        r.pop_back();
        r.push_back(comb_it->second);
        continue;
      }
      else if (destroy_pair[a[i]] > 0)
      {
        //cout << "h1"<< endl;
        r.clear();
        destroy_pair.clear();
        continue;
      }
    }
      
    pair<multimap<char,char>::const_iterator,multimap<char,char>::const_iterator> ret;
    ret = destroy.equal_range(a[i]);

    multimap<char,char>::const_iterator it =ret.first;
    for (;it != ret.second; ++it)
    {
      //cout << "destroy!" << it->second << endl;
      //destroy_pair.insert(it->second);
      destroy_pair[it->second]++;
    }
    /*
    map<char, char>::const_iterator destr_it = destroy.find(a[i]);
    if (destr_it != destroy.end())
    {
      destroy_pair.insert(destr_it->second);
    }
    */
    //cout << "h3"<< endl;
    r.push_back(a[i]);
  }
  return r;
}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 1; c <= cases; ++c)
	{
    map< pair<char, char>, char> combine;
    multimap<char, char> destroy;
    
    int C, D, N;
    
    cin >> C;
    for (int i = 0; i < C; ++i)
    {
      string s;
      cin >> s;
      combine[MKPAIR(s[0], s[1])] = s[2];
    }
    
    
    cin >> D;
    for (int i = 0; i < D; ++i)
    {
      string s;
      cin >> s;
      destroy.insert(pair<char,char>(s[0], s[1]));
      destroy.insert(pair<char,char>(s[1], s[0]));
    }
    
    cin >> N;
    string a;
    cin >> a;
    list<char> r = compute(combine, destroy, a);
    
    cout << "Case #" << c << ": ";
    
    cout << r;
		cout << endl;
	}
}
