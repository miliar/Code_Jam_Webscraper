#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <cmath>

using namespace std;

#define ORANGE 0
#define BLUE 1

int main(void){
  int T_NumberOfCases,NowCaseNumber;
  int N_NumberOfButtons;
  cin>>T_NumberOfCases;
  for(NowCaseNumber=1;NowCaseNumber<=T_NumberOfCases;NowCaseNumber++){
    cout<<"Case #"<<NowCaseNumber<<": ";
    cin>>N_NumberOfButtons;
    vector<int> R_RobotColor(N_NumberOfButtons);
    vector<int> P_ButtonPosition(N_NumberOfButtons);
    for(int i=0;i<N_NumberOfButtons;i++){
      string temp;
      cin>>temp>>P_ButtonPosition[i];
      if(temp=="O")R_RobotColor[i]=ORANGE;
      else if(temp=="B")R_RobotColor[i]=BLUE;
    }
    vector<int> position(2,1);
    int result=0;
    for(int i=0;i<N_NumberOfButtons;i++){
      int distanceI=abs(P_ButtonPosition[i]-position[R_RobotColor[i]]);
      result+=distanceI+1;
      position[R_RobotColor[i]]=P_ButtonPosition[i];
      for(int j=i+1;j<N_NumberOfButtons;j++){
	if(R_RobotColor[i]!=R_RobotColor[j]){
	  int distanceJ=abs(P_ButtonPosition[j]-position[R_RobotColor[j]]);
	  if(distanceI+1 >= distanceJ){
	    position[R_RobotColor[j]]=P_ButtonPosition[j];
	  }else if(P_ButtonPosition[j] > position[R_RobotColor[j]]){
	    position[R_RobotColor[j]]+=(distanceI+1);
	  }else{
	    position[R_RobotColor[j]]-=(distanceI+1);
	  }
	  break;
	}
      }
    }
    cout<<result<<"\n";
  }
}

