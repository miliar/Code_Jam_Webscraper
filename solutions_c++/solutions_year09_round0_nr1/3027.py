#include<iostream>
#include<vector>
#include<cassert>
using namespace std;
int N,L,D;
string dict[5005];

bool comp(string &word,vector<string> letters)
{

  for(int i=0;i<L;i++)
    if(letters[i].find(word[i])==string::npos)return false;
  
  return true;
}

int main(){
  
  cin>>L>>D>>N;
  for(int i=0;i<D;i++)cin>>dict[i];

  for(int k=1;k<=N;k++){
    string pattern;
    cin>>pattern;

    vector<string> letters;

    for(int i=0;i<pattern.size();i++){
      if(pattern[i]=='('){
	int strt=i;
	while(pattern[i]!=')')i++;
	letters.push_back(pattern.substr(strt,i-strt+1));
      }
      else {
	string temp="";
	temp+=pattern[i];
	letters.push_back(temp);
      }
    }

    assert(letters.size()==L);
    int ans=0;
    for(int i=0;i<D;i++)
      if(comp(dict[i],letters))ans++;
    

    cout<<"Case #"<<k<<": "<<ans<<endl;
  }
  
}
