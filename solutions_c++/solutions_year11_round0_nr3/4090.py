#include <iostream>
#include <vector>
using namespace std;
int max(int a,int b){
  if(a>b)
    return a;
  return b;
}
int main(){
  int cases;
  cin >> cases;
  for(int p=0;p<cases;p++){
    int num;
    cin >> num;
    vector<int> arr;
    int grab;
    for(int i=0;i<num;i++){
      cin >> grab;
      arr.push_back(grab);
    }
    int val=0;
    int tot=(1 << num);
    for(int i=1;i<tot-1;i++){
      int one=0,two=0;
      for(int k=0;k<num;k++){
	if(i & (1 << k))
	  one^=arr[k];
	else
	  two^=arr[k];
      }
      if(one==two){
	int sum=0;
	int sum2=0;
	for(int k=0;k<num;k++)
	  if(i & (1 << k))
	    sum+=arr[k];
	  else
	    sum2+=arr[k];
	if(val<max(sum,sum2))
	  val=max(sum,sum2);
	if(val==14)
	  cout << one << '\t' << two << endl;
      }
    }
    cout << "Case #" << p+1 << ": ";
    if(val>0)
      cout << val;
    else
      cout << "NO";
    cout << endl;
  }
}
