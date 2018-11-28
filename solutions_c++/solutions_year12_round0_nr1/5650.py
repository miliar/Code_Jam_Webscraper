#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <fstream>


using namespace std;

void translate()
{
  map<char, char> dict;
  dict['a'] = 'y';
  dict['o'] = 'e';
  dict['z'] = 'q'; 
  string s[3];
  string t[3];
  s[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  s[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  s[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  t[0] = "our language is impossible to understand";
  t[1] = "there are twenty six factorial possibilities";
  t[2] = "so it is okay if you want to just give up";

  int a[26] = {0};
  int b[26] = {0};
  a[0] = 1;
  a['o'-'a'] = 1;
  a['z'-'a'] = 1;
  b['y'-'a'] = 1;
  b['e'-'a'] = 1;
  b['q'-'a'] = 1;
  
  for (int i=0; i < 3; i++)
  {
	  int si = s[i].size();
	  for (int j=0; j < si; j++)
	  {
         dict[s[i][j]] = t[i][j];
		 a[s[i][j]-'a'] = 1;
		 b[t[i][j]-'a'] = 1;
	  }
  }
  int ma = -1; 
  int mb = -1;
  for (int i=0; i < 26; i++)
  {
	  if (a[i] == 0)
		  ma = i;
	  if (b[i] == 0)
		  mb = i;
  }
  if (ma >=0 && mb >=0)
	  dict['a'+ma] = 'a' + mb;

  ifstream infile("A-small-attempt4.in");
  string str;
  getline (infile, str);
  istringstream buffer(str);
  int value;
  buffer >> value;
  ofstream outfile("result.txt");
  for (int i=0; i < value; i++)
  {
	  getline(infile, str);
	  string res;
	  for (unsigned int j=0; j < str.size(); j++) 
		  res += dict[str[j]];
	  outfile << "Case #" << i+1 <<": " << res << endl;
	  res.clear();
  }

}

int main()
{ 
	translate();
	return 0;
}