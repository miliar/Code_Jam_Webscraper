
#include <iostream>

using namespace std;

int hw[100];
int n;
int step[100];

int cost(int a, int b){
	return 1+abs(hw[a]-hw[b]);
}

void addnext(int p){
	int i;
	for (i=p+1;i<n;i++){
		if (hw[i]/1000==hw[p]/1000){
			step[i]=step[p]+cost(p,i);
			break;
		}
	}
	if (p+1<n){
		if (hw[p+1]/1000!=hw[p]/1000){
			if (step[p+1]<step[p]+1){
				step[p+1]=step[p]+1;
			}
		}
	}
}

int compute(){
	int i,j;
	//memset(step,0,100*sizeof(int));
	for (i=0;i<n;i++){
		step[i]=hw[i]%1000;
	}
	for (i=0;i<n;i++){
		addnext(i);
	}
	//for (i=0;i<n;i++){
	//	printf("%d ",step[i]);
	//}
	//printf("\n");
	return step[n-1];
}

int main(){
	int t;
	int i,j;
	char hallway;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n;
		for (j=0;j<n;j++){
			cin>>hallway;
			cin>>hw[j];
			if (hallway=='B') hw[j]+=1000;
		}
		cout<<"Case #"<<(i+1)<<": "<<compute()<<endl;
	}
}
