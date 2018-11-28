#include<iostream>
using namespace std;
#include<algorithm>
#include<cstring>
int main(){
  int kase, i, k,T,D,len;
  //int arr[10][20];
  char arr[25],arr2[25];
  scanf("%d\n",&T);
  for(kase=1;kase<=T;kase++){
	scanf("%[0-9]\n",arr);
	strcpy(arr2,arr);
	len = strlen(arr);
	next_permutation(arr,arr+len);
	if(strcmp(arr, arr2)>0)
	  cout<<"Case #"<<kase<<": "<<arr<<endl;
	else{
	  sprintf(arr,"0%s",arr2);
	  next_permutation(arr,arr+len+1);
	  cout<<"Case #"<<kase<<": "<<arr<<endl;
	}
  }
  return 0;
}

	
  