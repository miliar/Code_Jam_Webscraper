#include <iostream>
//#include <stdio.h>

using namespace std;

unsigned long spaceG[1000];
unsigned long k;
int N;
int index;

__int64 getOnetime(){
	__int64 result = 0;
	int init = index;
	
	while(true){
		if(result+spaceG[index] > k){
			break;
		}
		result += spaceG[index];
		index++;
		if(index == N)
			index = 0;

		if(init == index)
			break;
	}
	return result;
}


int main(){
	freopen("C-small-attempt0.in.txt","r",stdin);
	int T;
	unsigned long R;
	
	__int64 result;
	FILE *file = fopen("C-small-attempt0.out.txt","w");

//	printf("%I64d\n",result);

	cin>>T;

	for(int i = 1 ; i <= T ; i++){
		cin>>R>>k>>N;
		for(int j = 0 ; j < N ; j++){
			cin>>spaceG[j];
		}
		index = 0;
		result = 0;
		for(int l = 0 ; l < R ; l++){
			result += getOnetime();
		}
		fprintf(file,"Case #%d: ",i);
		fprintf(file,"%I64d\n",result);
	}

	return 0;
}

