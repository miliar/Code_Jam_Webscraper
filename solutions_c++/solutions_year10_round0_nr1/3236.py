#include <stdio.h>
#include <iostream>


using namespace std;


int main(int argc,char **argv){
  
	unsigned long Clicks[30];
  int T;
	int N;
	long K=0;
	bool state;
  long nClick;	
	//compute Clics array
	Clicks[0]=1;
  for(int i=1;i<30;i++){
    Clicks[i]=Clicks[i-1]*2 + 1;
//		cout << "Clicks[" << i << "]=" << Clicks[i] << endl;   
	}
	
	//Red Number of test cases
	scanf("%d",&T);

	for(int i = 0;i<T;i++){

		//read N,K
		scanf("%d %ld",&N,&K);
    
		nClick = Clicks[N-1];
    state = false;
		while(K>0){
			K -= (state?1:nClick);
			state = !state;
		};

		if(state && K==0)
		  state = true;
		else
			state = false;

		
    printf("Case #%d: %s\n",i+1,state?"ON":"OFF");
	}

  return 0;
}
