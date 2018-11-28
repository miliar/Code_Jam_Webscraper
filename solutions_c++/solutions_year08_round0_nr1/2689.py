#include<iostream>
#include<string>
using namespace std;
class searchengine{
	public:
	char name[100];
	int value;
	
	searchengine(){
		value = -1;
	}
};


int getMax(int *array, int length){
	//cout<<"\nfn called";
	int max = array[0];
	for(int j=1; j<length; j++){
		if(max < array[j])
			max= array[j];
	}
	return max;
}

int main(){
	//Input
	int probCtr,Counter=0;
	scanf("%d\n",&probCtr);
	
	while(Counter++ < probCtr){
	int S,Q,i,k;
	scanf("%d\n",&S);
	searchengine engine[100];
		
	for( i=0 ; i<S ; i++)
	{
		gets(engine[i].name);
		scanf("\n");
	}
	/*
	for( i=0 ; i<S ; i++)
		printf("%s\n",engine[i].name);*/
	//cout<<"\nEngines Over\n";
	scanf("%d\n",&Q);
	char query[1000][100];
	for(i=0 ; i<Q ; i++)
	{
		gets(query[i]);
		scanf("\n");
	}
	/*
	for( i=0 ; i<Q ; i++)
		printf("%s\n",query[i]);*/
	//cout<<"\nQueries Over\n";
	//Initialization of solmatrix
	int sol[100][1000];
	for(i=0;i<Q;i++)
		for(k=0;k<S;k++)
			sol[i][k] = -1;
	
	//cout<<"\nInitialization over\n";
	//Filling SolMatrix
	for(i=0 ; i<Q ; i++){
		for(k=0; strcmp(query[i],engine[k].name) ; k++);
		int eng = k;
		for(k = engine[eng].value+1; k <= i ; k++){
			sol[k][eng] = i;
		}
		engine[eng].value = i;
	}
	
	for(i=0; i<Q ; i++){
		//cout<<"\n";
		for(k=0; k<S; k++){
			if(sol[i][k] == -1)
				sol[i][k] = Q;
			//cout<<sol[i][k]<<" ";
		}
	}
	
	//Calculating ans
	
	int ans = 0;
	for(int max= getMax(sol[0],S) ; max<Q; max=getMax(sol[max],S),ans++);
	cout<<"Case #"<<Counter<<": "<<ans<<"\n"; 
	}
	return 0;
}
