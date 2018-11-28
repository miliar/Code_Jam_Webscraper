#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <sstream>
using namespace std;

vector<string> add(vector<string> myvector, string s)
{
  vector<string> ret;
  for(int i=0;i<s.size();i++)
    {
      if(myvector.size()==0) {
	string temp;
	temp+=s[i];
	ret.push_back(temp);
      }

      else {
	for(int j=0;j<myvector.size();j++)
	  {
	    ret.push_back(myvector[j]+s[i]);
	  }
      }
    }
  return ret;
}
      

int compare(vector<string> vec, int level, string word, set<string> words) {
  int sum=0;
  if(level+1==vec.size()) {
    for(int i=0;i<vec[level].length();i++)
      if(words.count(word+vec[level][i])>0) sum++;
    return sum;
  }
  for(int i =0;i<vec[level].length();i++)
    sum+=compare(vec,level+1,word+vec[level][i],words);
  return sum;
}

int main(){
 int L,D,N;
 cin >> L >> D >> N;
 // cout << L << " " << D << " " << N << endl;
 vector<string> words;
 string temp;
 while(D--) {
   cin >> temp;
   words.push_back(temp);
 }


 vector<string> patterns;
 while(N--) {
   cin >> temp;
   patterns.push_back(temp);
 }
 
 for(int i=0;i<patterns.size(); i++) {
   vector<string> possible;
   vector<string> subs;

   //   cout << "The pattern is: " << patterns[i] << endl;
   possible.clear();
   for(int j=0;j<patterns[i].length();j++) {
     if(patterns[i][j]==')') {
       continue;
     }
     if(patterns[i][j]!='(') {
       //       cout << patterns[i][j] << endl;
       string temp3;
       temp3+=patterns[i][j];
       subs.push_back(temp3);
       //possible = add(possible,temp3);
     }
     else if (patterns[i][j]=='(') {
       j++;
       string temp2;
       while(j<patterns[i].length() && patterns[i][j]!=')' && patterns[i][j]!='(') {
	 
	 temp2+=patterns[i][j];
	 //	 cout << patterns[i][j] << "*" << endl;
         j++;
       }
       //       cout << "**" << temp2 << endl;
       subs.push_back(temp2);
       //       possible = add(possible, temp2);

     }

   }
   int sum=0;
   /*for(int t=0;t<possible.size();t++) {
     if(words.count(possible[t])>0) sum++;
     }*/
   for(int mo = 0; mo<words.size(); mo++)
     {
       int ps=0;
       for(int a=0;a<L;a++)
	 {
	   if(subs[a].find(words[mo][a])!=string::npos) ps++;
	 }
       if(ps==L) sum++;
     }

   //   sum = compare(subs, 0, "",words);
   cout << "Case #" << i+1 << ": " << sum <<  endl;


 }


 return 0;
 }

