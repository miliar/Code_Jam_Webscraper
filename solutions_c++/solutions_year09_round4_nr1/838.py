#include<iostream>
using namespace std;
int main(){
  int T,N,kase,i,m,tmp,ctr,k,min;
  long long arr[40];
  scanf("%d\n",&T);
  char num[60];
  for(kase=1;kase<=T;kase++){
	 scanf("%d\n",&N);
	 for(i=0;i<N;i++){
	   scanf("%s\n",num);
	  // cout<<num<<endl;
	   for(m=N-1,arr[i]=0;m>=0;m--)
		 if(num[m] == '1'){
		   arr[i] = m;
		   break;
		 }
		 //arr[i] += ((num[m]-'0')<<(N-m-1));
	  // cout<<arr[i]<<", ";
	 }
	 //cout<<endl;
	 for(i=0,ctr=0;i<N;i++){
	   for(m=i;m<N;m++){
		 if(arr[m] <= i)
		   break;
	   }
	   //if(min < arr[min])
	   for(k=m;k>i;k--){
		   tmp = arr[k];
		   arr[k] =arr[k-1];
		   arr[k-1] =tmp;
		   ctr++;
		}
		
	   
	 }
	 cout<<"Case #"<<kase<<": "<<ctr<<endl;
  }
  return 0;
}

	  