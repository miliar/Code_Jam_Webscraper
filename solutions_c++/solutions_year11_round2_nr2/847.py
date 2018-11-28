
//Problem B. Revenge of the Hot Dogs

#include <iostream>

using namespace std;

int n;
int c,d;
int p[200],v[200];
int bmin,bmax; //times 2

int valid(int t){ //given min time=t/2
	int ret=1;
	int i,j,k;
	double rightmost;
	double delta=0.001;
	rightmost=p[0]-t/2.0-d;
	for (i=0;i<c;i++){
		if (rightmost+d+delta<p[i]-t/2.0){
			rightmost=(p[i]-t/2.0)+(v[i]-1)*d;
		} else if (rightmost+v[i]*d>p[i]+t/2.0+delta){
			return 0;
		} else {
			rightmost=rightmost+v[i]*d;
		}
	}
	return ret;
}

double compute(){
	int i,j,k;
	bmin=0;
	k=0;
	for (i=0;i<c;i++) if (k<v[i]) k=v[i];
	bmin=(k-1)*d-1;
	k=0;
	for (i=0;i<c;i++) k+=v[i];
	bmax=k*d+1;	

	//sort
	  int temp;
	  for (i=c;i>=1;i--){
		  for (j=0;j<i-1;j++){
			  if (p[j+1]<p[j]){
				  temp=p[j+1];
				  p[j+1]=p[j];
				  p[j]=temp;
				  temp=v[j+1];
				  v[j+1]=v[j];
				  v[j]=temp;
			  }
          }
	  }
	
	int mid;
	int localmin=bmax;
	while (bmin+1<bmax){
		mid=(bmin+bmax)/2;
		int result=valid(mid);
		//printf("try %d:%d\n",mid,result);
		if (result){
			localmin=mid;
			bmax=mid;
		} else {
			bmin=mid;
		}
	}

	return localmin/2.0;
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>c>>d;
		for (j=0;j<c;j++){
			cin>>p[j]>>v[j];
		}
		cout<<"Case #"<<(i+1)<<": "<<compute()<<endl;
	}
}
