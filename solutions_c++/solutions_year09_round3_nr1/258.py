#include<iostream>
using namespace std;
#include<cstring>
long long hap(long long n, long long b){
  
  long long sum = 0,tmp;
  while(n >= b){
	//cout<<n<< " ";
	for(tmp=b;(n/tmp) >=b;tmp = b*tmp);
	sum += (n/tmp)*(n/tmp);
	n = n - tmp * (n/tmp);
	
	//cout<<sum<<" ";
  }
  return (sum + n*n);
 }
int main(){
  int kase, T,i,k,baseMax,ctr, arrIndex,baseMin,base,len;
  long long sum;
  char str[62];
  int flag[36], arr[36];
  scanf("%d\n",&T);
  for(kase=1;kase<=T;kase++){
	scanf("%[0-9a-z]\n",str);
	//cout<<str<<endl;
	len =strlen(str);
	for(k=0;k<36;k++){
	  arr[k] = -1;
	  flag[k] = 0;
	}
	//baseMax= '0', baseMin='z';
	for(k=0;k<len;k++){
	  /*if(str[k] > baseMax)
		baseMax = str[k];
	  if(str[k] < baseMin)
		baseMin = str[k];
	  */
	  if(str[k] >= 'a')
		flag[10 + str[k] - 'a'] = 1;
	  else
		flag[str[k] - '0'] =1;
	}
	for(k=0,base=0;k<36;k++)
	  base += flag[k];
	if(base == 1)
	  base=2;
	//cout<<"base="<<base<<endl;
	
	if(str[0] >= 'a')
	  arr[10+str[0] - 'a'] = 1;
	else
	  arr[str[0] - '0'] =1;
	for(k=1;k<len && str[k]==str[0];k++);
	
	if(k!=len){
	  if(str[k] >= 'a')
		arr[10+str[k] - 'a'] = 0;
	  else
		arr[str[k] - '0'] =0;
	}
	  
	for(i=k+1,ctr=2;i<len;i++){
	  if(str[i] >= 'a')
		arrIndex = 10+str[i] - 'a';
	  else
		arrIndex = str[i] - '0';
	  if(arr[arrIndex] == (-1)){
		arr[arrIndex] = ctr++;
	  }
	}
	/*
	for(k=0;k<36;k++)
	  if(arr[k] !=-1)
		cout<<k<<":"<<arr[k]<<" ";
	cout<<endl;
	*/
	//base = baseMax - baseMin + 1;
	//cout<<base<<endl;
	for(k=0,sum=0;k<len;k++)
	  if(str[k] >='a')
		sum = sum*base + arr[10 + str[k]-'a'];
	  else
		sum = sum*base + arr[str[k] - '0'];
	cout<<"Case #"<<kase<<": "<<sum<<endl;
  }
  return 0;
}
