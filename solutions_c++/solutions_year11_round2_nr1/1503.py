#include<iostream>
#include<cstdlib>
#include<string>
#include<list>

using namespace std;
/*
void(int matrix[100][],int N,double rpi[]){
  double wp[100],owp[100],oowp[100];
  for (int i=0;i<N;i++){
    wp[i]
  }

}
*/
int main(){
  int T,N,play[100];
  char in;
  cin>>T;
  double rpi,wp[100],owp[100],oowp[100];
  int matrix[100][100],nocount;
  double sum;
  for (int kk=0;kk<T;kk++){
    cin>>N;
    for (int j=0;j<N;j++){
      //wp[j]=0;
      play[j]=0;
      sum=0.0;
      for (int k=0;k<N;k++){
	cin>>in;
	//cout<<in<<endl;
	if (in=='.') matrix[j][k]=-1;
	else {
	  matrix[j][k]=in-'0';
	  //cout<<matrix[j][k]<<endl;
	  play[j]++;
	  if (in=='1') sum++;
	}
	//wp[j]=sum/play[j];
      }
      wp[j]=sum/play[j];
    }
    //cout<<wp[0]<<endl;
    for (int i=0;i<N;i++){
      sum=0;nocount=i; 
      for (int j=0;j<N;j++){
	if (j!=i && matrix[i][j]!=-1) sum+=(wp[j]*play[j]-matrix[j][i])/(play[j]-1);
      }
      owp[i]=sum/play[i];
    }
    //cout<<owp[0]<<endl;
    for (int i=0;i<N;i++){
      sum=0;
      for(int j=0;j<N;j++){
	if (matrix[i][j]!=-1) sum+=owp[j];
      }
      oowp[i]=sum/play[i];
    }
    //cout<<oowp[0]<<endl;
    //compute(matrix,N,rpi);
    cout<<"Case #"<<kk+1<<":"<<endl;
    for (int j=0;j<N;j++){
      rpi=(0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
      cout<<(float)rpi<<endl;
    }
  }

  return 0;
}
