#include <iostream>
#include <string>

using namespace std;
int M,N,R,C;
char picture[50][50];

int main(){
  int case_num,case_max,i,j,k;
  int ans;
  cin >> case_max;
  for(case_num =0;case_num < case_max; case_num++){
    cout << "Case #" << case_num+1 << ":"<<endl;
    cin >> R >>C;
    for(i=0;i<R;i++){
      for(j=0;j<C;j++){
	cin >> picture[i][j];
	//cout <<  picture[i][j];
      }
      //cout << endl;
    }
    for(i=0;i<R;i++){
      for(j=0;j<C;j++){
	if(picture[i][j]=='#'){
	  if(i+1==R || j+1==C){
	    cout << "Impossible"<<endl;
	    goto IMP;
	  }else if(picture[i][j+1]=='#' && picture[i+1][j]=='#'&& picture[i][j+1]=='#' ){
	    picture[i][j]='/';
	    picture[i][j+1]='\\';
	    picture[i+1][j]='\\';
	    picture[i+1][j+1]='/';
	  }
	}
      }
    }
    
    for(i=0;i<R;i++){
      for(j=0;j<C;j++){
	cout<<picture[i][j];
      }
      cout << endl;
    }
  IMP:
    k=1;;
  }
  
  
  return 0;
}
