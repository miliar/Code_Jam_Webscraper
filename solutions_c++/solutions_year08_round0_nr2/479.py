#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int N,n=0;
  cin >>N;
  while(n++<N){
    int T,NA,NB;
    cin>>T>>NA>>NB;
    string tmp;
    int time;
    vector<int> AA,AL,BA,BL; //A/B Arrive/Leave
    for (int i=0;i<NA;i++){
      cin >> tmp;
      time = 0;
      time = tmp[0]-'0';
      time = time*10+tmp[1]-'0';
      time = time*6+tmp[3]-'0';
      time = time*10+tmp[4]-'0';
      AA.push_back(2*time+1);
      cin >> tmp;
      time = 0;
      time = tmp[0]-'0';
      time = time*10+tmp[1]-'0';
      time = time*6+tmp[3]-'0';
      time = time*10+tmp[4]-'0';
      BA.push_back(2*(time+T));
    }
    for (int i=0;i<NB;i++){
      cin >> tmp;
      time = 0;
      time = tmp[0]-'0';
      time = time*10+tmp[1]-'0';
      time = time*6+tmp[3]-'0';
      time = time*10+tmp[4]-'0';
      BA.push_back(2*time+1);
      cin >> tmp;
      time = 0;
      time = tmp[0]-'0';
      time = time*10+tmp[1]-'0';
      time = time*6+tmp[3]-'0';
      time = time*10+tmp[4]-'0';
      AA.push_back(2*(time+T));
    }
    sort(AA.begin(),AA.end());
    sort(BA.begin(),BA.end());
    int curA=0,maxA=0,curB=0,maxB=0;
    for (int j=0;j<AA.size();j++){
      //      cout<<AA[j]<<endl;;
      //      cout<<AA[j]/120<<':'<<(AA[j]%120)/2<<endl;
      if (AA[j]&1)
	curA++;
      else
	curA--;
      if (maxA<curA)
	maxA=curA;
    }
    for (int j=0;j<BA.size();j++){
      if (BA[j]&1)
	curB++;
      else
	curB--;
      if (maxB<curB)
	maxB=curB;
    }
    cout<<"Case #"<<n<<": "<<maxA<<" "<<maxB<<endl;
  }
}





