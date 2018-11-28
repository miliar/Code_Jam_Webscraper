#include <iostream>
using namespace std;

int partition( int n, int input[], int group1[], int length1,
                int group2[], int length2 ,int &max){
  if( n==0 ){
    int sum1 = 0, sum2 = 0, sum3=0, sum4=0;
    for( int i=0; i<length1; i++ ){
         sum1=sum1^group1[i];
         sum4 += group1[i];
    }
    for( int i=0; i<length2; i++ ){
         sum2 = sum2^group2[i];
         sum3+=group2[i];
    }
    if( sum1==sum2 && sum1>0 ){
     /*   cout << "Group 1: ";
      for( int i=0; i<length1; i++ ) cout << group1[i] << ' ';
      cout << endl;
      cout << "Group 2: ";
      for( int i=0; i<length2; i++ ) cout << group2[i] << ' ';
      cout << endl;*/
      if (sum4>max)
          max=sum1;
      if (sum3>max)
          max=sum3;
      //cout<<sum2<<endl;
      //cout<<max<<endl;
      return true;
    }
  }
  else{
    int current = input[n-1];
    group1[length1] = current;
    length1++;
    partition( n-1, input, group1, length1, group2, length2 , max);
    group1[length1-1] = 0; 
    length1--;
    group2[length2] = current;
    length2++;
    partition( n-1, input, group1, length1, group2, length2 , max);
    return true;
  }
}

int main(){
  int n, max=-1,t,length1, length2;
  cin>>t;
  for (int z=0;z<t;z++){
      cin >> n;
      int input[1100];
      for( int i=0; i<n; i++ )
           cin >> input[i];
      int group1[1100], group2[1100];
      max=-1;
      length1 = 0;
      length2 = 0;
      partition( n, input, group1, length1, group2, length2 , max);
      if( max==-1 )
          printf("Case #%d: NO\n", z+1);
      else
          printf("Case #%d: %d\n",z+1, max);
  }
  return 0;
}
        
