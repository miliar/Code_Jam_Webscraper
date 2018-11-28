#include<iostream>
#include<cstdio>
#include<cstdlib>

long long groups[4000],nextGroup[2000],weight[2000],chain[2000],ring[2000],sumAll;
int pivotElement,chainSize,ringSize;
int numGroups,numRides,maxCapacity;
bool visited[2000];

void enterData(){
	scanf("%d%d%d",&numRides,&maxCapacity,&numGroups);

//	printf("R=%d X%d N=%d\n",numRides,maxCapacity,numGroups);
	
	int i;	
	for(i=0,sumAll=0;i<numGroups;i++){
		scanf("%lld",(groups+i));
		sumAll+=groups[i];	

//		printf("%lld\n",groups[i]);
	
	}
	
	int max=2*numGroups,j=0;
	
	for(;i<max;i++,j++){
		groups[i]=groups[j];
	}
}

bool decision(){

//	printf("sumAll=%lld maxCapacity=%d\n",sumAll,maxCapacity);

	if(sumAll<=maxCapacity){
		printf("%lld\n",numRides*sumAll);         //case 0
		return false;
	}
	else	return true;
}

void createGraph(){
	long long prevWeight=groups[0];
	int i,previous=0;

	for(i=0;i<numGroups;i++){
		nextGroup[i]=previous;
		weight[i]=prevWeight;
		while(weight[i]+groups[nextGroup[i] + 1] <= maxCapacity){
			nextGroup[i]++;
			weight[i]+=groups[nextGroup[i]];
		}

		previous=nextGroup[i];
		prevWeight=weight[i]-groups[i];

//		printf("i=%d group=%lld next=%lld total=%lld prev=%d prevW=%lld\n",i,groups[i],nextGroup[i],weight[i],previous,prevWeight);

		nextGroup[i]=(nextGroup[i]+1)%numGroups;

//		printf("i=%d group=%lld next=%lld total=%lld prev=%d prevW=%lld\n",i,groups[i],nextGroup[i],weight[i],previous,prevWeight);
	}	
}

void traverseGraph(){
	int i,current=0,k=0;
	for(i=0;i<numGroups;i++){
		visited[i]=false;
	}

	while(visited[ nextGroup[current] ] == false){
		
		visited[current]=true;
		current=nextGroup[ current ];
	}

	pivotElement= nextGroup[current]; 

//	printf("pivotElement=%d\n",pivotElement);
}

void createChainList(){
//	printf("Printing Chain\n");

	chainSize=0;
	int current=0;
	long long currWeight=0;

	while(current != pivotElement){
		currWeight+=weight[current];
		chain[chainSize++]=currWeight;

//		printf("%d %d %lld\n",chainSize-1,current,currWeight);		

		current=nextGroup[current];
	}

/*	for(int i=0;i<chainSize;i++){
		printf("%d %lld\n",i,chain[i]);
	}
*/
}

void createRingList(){
//	printf("Printing Ring\n");

	ringSize=1;
	int current=nextGroup[pivotElement];
	long long currWeight=weight[pivotElement];
	ring[0]=weight[pivotElement];

	while(current != pivotElement){
		currWeight+=weight[current];
		ring[ringSize++]=currWeight;
		current=nextGroup[current];
	}

/*	for(int i=0;i<ringSize;i++){
		printf("%d %lld\n",i,ring[i]);
	}
*/
}

bool decision2(){
	if(numRides<=chainSize){

//		printf("Case 1");

		printf("%lld\n",chain[numRides-1]);		//case 1(a)
		return false;
	}
	else return true;
}

void bringAnswer(){
	long long chances= numRides-chainSize,quotient=chances/ringSize,remaining=chances%ringSize;
	long long answer=0;

//	printf("Case 2\n");

//	printf("chances=%lld quotient=%lld remainder=%lld\n",chances,quotient,remaining);

	if(chainSize>0){
		answer=chain[chainSize-1];
	}

//	printf("%lld\n",answer);
	
	answer+=(quotient)*ring[ringSize-1];
	
//	printf("%lld\n",answer);

	if(remaining>0){
		answer+=ring[remaining-1];
	}

	printf("%lld\n",answer);				//case 1(b)
}

void solveProblem(){
	enterData();
	if (decision()){
		createGraph();
		traverseGraph();
		createChainList();
		createRingList();
		if(decision2()){
			bringAnswer();
		}
	}
}

main(){
	int i,testcases;
	scanf("%d",&testcases);
	for(i=1;i<=testcases;i++){
		printf("Case #%d: ",i);
		solveProblem();	
	}
}
