#include<iostream>


using namespace std;

int combine( char c1, char c2, char bp[][3], int c){

  for(int i=0; i < c ; i++){
    if( (bp[i][0] == c1 && bp[i][1] == c2) || (bp[i][0] == c2 && bp[i][1] == c1) )
      return i;
  }

  return -1;
}

int opposed(char *cos, int len, char op [][2], int d){

  if(!d) return 0;

  char c1, c2=cos[len-1];

  for(int i=0; i<len-1 ; i++){
    c1 = cos[i];
    for(int j=0; j<d; j++)
      if( (op[j][0] == c1 && op[j][1] == c2) || (op[j][0] == c2 && op[j][1] == c1))
        return 1; 
  }
  return 0;
}

int main(){

  int t,c,d,n;
  int i,j;
  char ch1, ch2, ch3;
  char bp[37][3];
  char op[29][2];
  char seq[200];
  int res,k;

  cin >> t;
  j=0;
  while(j++ < t){
    cin >> c;
    for(i=0;i<c;i++){
      cin>>ch1>>ch2>>ch3;
      bp[i][0] = ch1;
      bp[i][1] = ch2;
      bp[i][2] = ch3;
    }
    cin >> d;

    for(i=0;i<d;i++){
      cin>>ch1>>ch2;
      op[i][0] = ch1;
      op[i][1] = ch2;
    }

    cin>>n>> seq;

    char cos[n];
    int len=0;

    for(i=0;i<n;i++){

      ch1 = seq[i];
      cos[len++] = ch1;

      if(len>1){
        res = combine(cos[len-2], cos[len-1], bp, c); 
        if(res>=0){
          cos[len-2] = bp[res][2];
          len = len-1;
        }

        if(len >1 && (res == -1) && opposed(cos, len, op, d))
          len=0;
      }
    }

    cout<<"Case #"<<j<<": [";

    for(i=0;i<len;i++){
      cout<<cos[i];
      if(i != len-1 ) cout<<", "; 
    }
    cout<<"]"<<endl;
  }
  return 0;
}



