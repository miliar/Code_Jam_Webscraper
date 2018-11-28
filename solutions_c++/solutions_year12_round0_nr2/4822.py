#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

bool gr_func (int i,int j) { return (i>j); }

int main(){
  int n,i,t,s,p,glers,count,spare,lag;
  vector<int> googlers, champs;
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  cin>>t;
  while(t--){
    //cout<<"CASE :"<<endl;
    googlers.clear();
    lag=0;
    spare=0;
    count=0;

    cin>>n; //googlers
    cin>>s; //surprise
    cin>>p; //threshold

    for(i=0;i<n;i++){
      cin>>glers;
      googlers.push_back(glers);
    }

    sort(googlers.begin(),googlers.end(), gr_func);

    //cout<<"Highest:"<<googlers[0]<<endl;

    for(i=0;i<n;i++){
      //googlers[i] /= 3;
      if(googlers[i] >= p*3){
        count++;
        //cout<<"-> :"<<googlers[i]<<endl;
      }
      else if(googlers[i] == 0){
        continue;
      }
      else{
        lag = p-(int)(googlers[i]/3);
        spare = googlers[i]-(int)(googlers[i]/3)*3;
        //cout<<googlers[i]<<" Lag :"<<lag<<" Spare: "<<spare<<endl;
        if(lag<=2){
          if(lag==1 && (spare == 1 || spare == 2)){
            count++;
            //cout<<"-> :"<<googlers[i]<<endl;
          }
          else if (s!=0 && ((lag == 2 && spare == 2) || (lag == 1 && spare == 0))){
            count++;
            s--;
            //cout<<"*-> :"<<googlers[i]<<endl;
          }
        }
      }
    }

    champs.push_back(count);
  }

  for(i=0;i<champs.size();i++){
    cout<<"Case #"<<i+1<<": "<<champs[i]<<endl;
  }
  fclose(stdin);
  fclose(stdout);

  return 0;
}
