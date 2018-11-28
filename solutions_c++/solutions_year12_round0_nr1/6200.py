#include<iostream>
#include<fstream>
#include<string>
#include<map>
using namespace std;

int main()
{
      string map = "yhesocvxduiglbkrztnwjpfmaq";
      ifstream fin("input.txt");
      ofstream fout("output.txt");
      int n;
      fin>>n;
      string s;
      getline(fin,s);
      for (int ii=0;ii<n;ii++)
      {
	    getline(fin,s);
	    string result = "";
	    for (int i=0;i<s.length();i++)
	    {
		  if (s[i] == ' ') result += ' ';
		  else result += map[s[i]-'a'];
	    }
	    fout<<"Case #"<<ii+1<<": "<<result<<endl;
      }
}
