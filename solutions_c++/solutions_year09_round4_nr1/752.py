#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<vector<int> > M;
int A[41];

int main(){
  int PC;
  cin>>PC;
  for(int pc=1;pc<=PC;pc++){
    int N;
    scanf("%d\n",&N);
    //cout<<"N : "<<N<<endl;
    M.clear();
    for(int i=0;i<N;i++){
      vector<int> temp;
      string t;
      cin>>t;
      for(int j=0;j<N;j++){
	temp.push_back(t[j]=='1');
	//cout<<t[j];
      }
      //cout<<endl;
      M.push_back(temp);
    }

    for(int i=0;i<N;i++){
      int ind=0;
      for(int j=0;j<N;j++){
	if(M[i][j])ind=j;
	//cout<<M[i][j];
      }
      //cout<<endl;
      A[i]=ind;
      //cout<<A[i]<<endl;
    }

    int count=0;
    for(int i=0;i<N;i++){      
      for(int j=i;j<N;j++){
	if(A[j]<=i){
	  int t=j;
	  while(t>i){
	    swap(A[t],A[t-1]);
	    count++;
	    t--;
	  }
	  break;
	}
      }
    }
    printf("Case #%d: %d\n",pc,count);
  }

}
