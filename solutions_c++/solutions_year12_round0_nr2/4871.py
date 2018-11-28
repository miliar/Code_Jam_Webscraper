#include <iostream>
#include <vector>
using namespace std;

int iSolution(int N,int S,int p,vector<int>& t)
{
	int iTotScore, iAnswer(0);
	//float fAvgScore;
	
	while (!t.empty()){
	  iTotScore = t.back();
	  //fAvgScore = (float) iTotScore/3;
	  //cout<<"fAvgScore :"<<fAvgScore<<" ";
	  if(iTotScore>=3){
		  if( (float)(iTotScore + 2)/3 >= p){
			iAnswer++;
		  } else{
			  if( (float)(iTotScore + 4)/3 >= p && S>0) {
				S--;
				iAnswer++;
			  }
		  }
	  } else { //separate algo if iTotScore<3
		  switch(iTotScore){
			  case 0: if(p==0) iAnswer++; break;
			  case 1: if(p<=1) iAnswer++; break;
			  case 2: if(p==1) iAnswer++; if(p==2 && S>0){iAnswer++; S--;} break;
		  }
	  }

	  t.pop_back();
	}
 return iAnswer;
}

int main()
{
	int T,N,S,p,temp;
	cin>>T;

	for(int i=1; i<=T; i++){
		cin>>N>>S>>p;
		vector<int> t;
		for(int j=0; j<N; j++){
			cin>>temp;
			t.push_back(temp);
		}
		cout << "Case #"<<i<<": "<<iSolution(N,S,p,t)<<endl;

	}
	return 0;
}
