#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

ifstream fin("a-small.in");
ofstream fout("a-small.out");

int count[300];
int duiying[100];
int output[100];
long long getans(string s) {
  set<char> set1;
	memset(count,0,sizeof count);
	memset(duiying,0,sizeof duiying);
	for (int i = 0; i < s.size(); i++)
	  set1.insert(s[i]);
  
  int b=set1.size();
  if (b==1) b=2;
  duiying[1]=s[0];
  set1.clear();
  set1.insert(s[0]);
  for (int i = 1; i < s.size(); i++)
    if (set1.find(s[i])==set1.end()) {
    	int ind = 0;
    	for (ind = 0; ind < b;ind++)
    	  if (duiying[ind]==0) 
    	    break;
	    duiying[ind]=s[i];
	    set1.insert(s[i]);
    }
  long long ans=0;
  for (int i = 0; i < s.size(); i++) {
    int ind=0;
    for (ind = 0; ind < b; ind++)
      if (duiying[ind]==s[i])
        break;
    ans = ans * b + ind;
  }
  return ans;
}
	


int main() {
	int ncase;
	fin>>ncase;
	for (int curcase=1; curcase<=ncase;curcase++) {
		string n;
		fin>>n;
		long long ans = getans(n);
		fout<<"Case #"<<curcase<<": "<<ans<<endl;
	}
	return 0;
}
		
		

