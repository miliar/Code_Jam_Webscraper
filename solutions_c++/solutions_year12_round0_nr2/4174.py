#include<iostream>
#include<vector>

using namespace std;
int main(){
  int t_cases,score,best,greater_n=0,total_surprise,n,s,p;
  cin >> t_cases;
  vector <int> surprise_chance;
  for(int i=1; i<=t_cases; i++){
    cout << "Case #" <<i<<": ";
    cin >> n;
    cin >> s;
    cin >> p;
    surprise_chance.resize(n);
    greater_n=0;
    for(int j=1; j<=n; j++){
      cin >> score;
      surprise_chance[j-1]=0;
      if(score==0){
	if(p==0)
	  greater_n++;
      }
      else if(score==1){
	if(p<=1)
	  greater_n++;
      }
      else if(score%3==0){
	if(score/3 >= p){
	  greater_n++;
	  surprise_chance[j-1]=0;
	}
	else if((score/3+1)==p){
	  surprise_chance[j-1]=1;
	}
	else {
	  surprise_chance[j-1]=0;
	}
      }
      else if(score%3==1){
	if((score/3)+1>=p){
	  greater_n++;
	}
	surprise_chance[j-1]=0;
      }
      else if(score%3==2){
	if((score/3)+1>=p){
	  greater_n++;
	  surprise_chance[j-1]=0;
	}
	else if((score/3)+2==p){
	  surprise_chance[j-1]=1;
	}
	else {
	  surprise_chance[j-1]=0;
	}
      }
    }
    total_surprise = 0;
    for(int j=1; j<=n; j++){
      total_surprise+=surprise_chance[j-1];
    }
    if(total_surprise<=s){
      greater_n+=total_surprise;
    }
    else if(s<total_surprise){
      greater_n+=s;
    }
    cout << greater_n << endl;
  }
  return 0;
}
