#include <iostream>

using namespace std;

main(){
  int t;
  cin >> t;
  for(int tc=0;tc<t;tc++){
    int r, c;
    cin >> r >> c;
    int cnt=0;
    char data[50][50];
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
	cin >> data[i][j];
	if(data[i][j]=='#') cnt++;
      }
    }
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
	if(data[i][j]=='#'){
	  if(j>=c-1) continue;
	  if(i>=r-1) continue;
	  if(data[i][j+1]=='#' && data[i+1][j+1]=='#' && data[i+1][j]=='#'){
	    data[i][j]='/';
	    data[i][j+1]='\\';
	    data[i+1][j]='\\';
	    data[i+1][j+1]='/';
	    cnt-=4;
	  }
	}
      }
    }
    cout << "Case #" << tc+1 << ":" << endl;
   if(cnt!=0){
     cout << "Impossible" << endl;
   }else{
     for(int i=0;i<r;i++){
       for(int j=0;j<c;j++){
	 cout << data[i][j];
       }
       cout << endl;
     }
   }
  }
  return 0;
}
