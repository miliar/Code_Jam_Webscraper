#include<iostream>
#include<vector>

using namespace std;

int main(){
  int T,R,k,N;
  cin>>T;
  for(int t = 1;t<=T;t++){
    cin>>R>>k>>N;
    vector<int> groups(N);
    for (int n=0;n<N;n++){
      cin>>groups[n];
    }
    vector<int> started(N,-1);
    vector<long long> incomes(N,0);
    started[0] = 0;
    long long income=0;
    int position=0;
    int newpos;
    int cursum;
    long long totgroups=0;
    for (int i=0;i<N;i++){
      totgroups+=groups[i];
    }
    if (totgroups<=k)
      income = totgroups*R;
    else{
      for (int i=0;i<R;i++){
	for (cursum=0,newpos=position;;newpos = (newpos+1)%N){
	  if (cursum+groups[newpos]>k){
	    income+=cursum;
	    if (started[newpos]==-1){
	      started[newpos] = i+1;
	      incomes[newpos] = income;
	    }
	    else{
	      int jump = i+1-started[newpos];
	      long long indiff = income - incomes[newpos];
	      long long times = (R-i-1)/jump;
	      income += times*indiff;
	      i+= times * jump;
	      for (int j=0;j<N;j++){
		started[j] = -1;
	      }
	    }
	    position = newpos;
	    break;
	  }
	  else{
	    cursum+=groups[newpos];
	  }
	}
	//	cout<<i<<" "<<income<<endl;
      }
    }
    cout<<"Case #"<<t<<": "<<income<<endl;
  }
}
	       
