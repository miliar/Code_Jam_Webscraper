#include <stdio.h>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;


priority_queue< pair< pair<int,int>, bool> > TimeTable;	// departure time, arrive time, is from A?
priority_queue< pair<int,bool> > freeTrain;



int T,A,B;
int availTrains[2];

int main(){

	int d;
	scanf("%d",&d);
	for (int dd=1; dd<=d; ++dd){

		scanf("%d%d%d",&T,&A,&B); scanf("\n");
		while (!freeTrain.empty()) freeTrain.pop();
		while (!TimeTable.empty()) TimeTable.pop();
		
		char semic;
		for (int a=0; a<A; ++a){
			//char str1[4],str2[4];
			//scanf("%[^:]s",str1); scanf(":"); scanf("%s",str2); scanf("\n");
			int m,h,tt1,tt2;
			cin>>h>>semic>>m; tt1=60*h+m;
			cin>>h>>semic>>m; tt2=60*h+m;
			TimeTable.push(make_pair( make_pair(-tt1,-tt2),true));
		}
		for (int b=0; b<B; ++b){
			char str1[4],str2[4];
			int m,h,tt1,tt2;
			cin>>h>>semic>>m; tt1=60*h+m;
			cin>>h>>semic>>m; tt2=60*h+m;
			TimeTable.push(make_pair( make_pair(-tt1,-tt2),false));
		}



		int result[2]; result[0]=result[1]=0;
		availTrains[0]=availTrains[1]=0;
		while (!TimeTable.empty()){
			int dep = TimeTable.top().first.first;
			int arr = TimeTable.top().first.second;
			bool isA = TimeTable.top().second;
			TimeTable.pop();
			
			while (!freeTrain.empty() && freeTrain.top().first>=dep){
				++availTrains[freeTrain.top().second];
				freeTrain.pop();
			}

			if (availTrains[isA]==0){
				++availTrains[isA];
				++result[isA];
			}

		
			--availTrains[isA];
			freeTrain.push( make_pair(arr-T,!isA) );
		}
		printf("Case #%d: %d %d\n",dd,result[1],result[0]);
	}


	return 0;
}

