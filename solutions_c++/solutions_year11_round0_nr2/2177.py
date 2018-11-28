#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <cmath>
#include <deque>

using namespace std;

int main(void){
  int T_NumberOfCases,NowCaseNumber;
  cin>>T_NumberOfCases;
  for(NowCaseNumber=1;NowCaseNumber<=T_NumberOfCases;NowCaseNumber++){
    cout<<"Case #"<<NowCaseNumber<<": ";
    int C_combine;
    cin>>C_combine;
    vector<string> combine(C_combine);
    for(int i=0;i<C_combine;i++)cin>>combine[i];
    int D_opposed;
    cin>>D_opposed;
    vector<string> opposed(D_opposed);
    for(int i=0;i<D_opposed;i++)cin>>opposed[i];
    int N_characters;
    cin>>N_characters;
    string series;
    cin>>series;
    string result;
    result.push_back(series[0]);
    int flag[26];
    for(int i=0;i<26;i++)flag[i]=0;
    flag[series[0]-'A']++;
    for(int i=1;i<N_characters;i++){
      result.push_back(series[i]);
      flag[series[i]-'A']++;
      for(int j=0;j<C_combine;j++){
	int rs=result.size();
	if(rs<2)break;
	if((result[rs-2]==combine[j][0] && result[rs-1]==combine[j][1])
	   || (result[rs-2]==combine[j][1] && result[rs-1]==combine[j][0])){
	  result.erase(rs-2);
	  flag[combine[j][0]-'A']--;
	  flag[combine[j][1]-'A']--;
	  result.push_back(combine[j][2]);
	  flag[combine[j][2]-'A']++;
	  break;
	}
      }
      for(int j=0;j<D_opposed;j++){
	int rs=result.size();
	if(rs<2)break;
	if(flag[opposed[j][0]-'A']>0 && flag[opposed[j][1]-'A']>0){
	  result.clear();
	  for(int k=0;k<26;k++)flag[k]=0;
	  break;
	}
      }
    }
    cout<<"[";
    for(int i=0;i<result.size();i++){
      cout<<result[i];
      if(i!=result.size()-1)cout<<", ";
    }
    cout<<"]\n";
  }
}

