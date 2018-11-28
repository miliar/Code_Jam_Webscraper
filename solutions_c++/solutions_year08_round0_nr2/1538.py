#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct{
	char StartStation;
	char StopStation;
	long StartTime;
	long StopTime;
}Train;

bool sort_(Train E1, Train E2){
	return E1.StartTime < E2.StartTime;
}

int main(){
	FILE* in = fopen("B.in","r");
	FILE* out = fopen("B.out","w");
	int TestCase = 0;
	fscanf(in, "%d\n", &TestCase);
	for(int TestNumber = 0; TestNumber < TestCase; TestNumber++)
	{	
		int TrainA = 0, TrainB = 0;
		long Turnaround_time = 0;
		fscanf(in, "%d\n", &Turnaround_time);
		fscanf(in, "%d %d\n", &TrainA, &TrainB);
		vector <Train> T;
		int Answer1 = 0, Answer2 = 0;
		for(int n = 0; n < TrainA; n++)
		{	
			Train *C = new (Train);
			C->StartStation = 'A';
			C->StopStation = 'B';
			int H,M;
			fscanf(in, "%d:%d ", &H, &M);
			C->StartTime = H * 60 + M;
			fscanf(in, "%d:%d\n", &H, &M);
			C->StopTime = H * 60 + M + Turnaround_time;			
			T.push_back(*C);
		}
		for(int n = 0; n < TrainB; n++)
		{	
			Train *C = new (Train);
			C->StartStation = 'B';
			C->StopStation = 'A';
			int H,M;
			fscanf(in, "%d:%d ", &H, &M);
			C->StartTime = H * 60 + M;
			fscanf(in, "%d:%d\n", &H, &M);
			C->StopTime = H * 60 + M + Turnaround_time;			
			T.push_back(*C);
		}
		sort(T.begin(),T.end(),sort_);
		vector <Train> Ans;
		/*for(int Time = 0; Time < 1440; Time++)*/
		

		
		while(!T.empty()){
			vector<Train>::iterator iter;
			if(T.begin()->StartStation == 'A'){
				for(iter = Ans.begin(); iter != Ans.end(); iter++){
					if ((iter->StopStation == 'A') && (iter->StopTime <= T.begin()->StartTime)){
						iter->StopStation = 'B';
						iter->StopTime = T.begin()->StopTime;
						break;
					}
				}
			}else{
				for(iter = Ans.begin(); iter != Ans.end(); iter++){
					if ((iter->StopStation == 'B') && (iter->StopTime <= T.begin()->StartTime)){
						iter->StopStation = 'A';
						iter->StopTime = T.begin()->StopTime;
						break;
					}
				}
			}
			if (iter == Ans.end()){
				Train* Temp = new (Train);
				Temp->StartStation = T[0].StartStation;
				Temp->StartTime = T[0].StartTime;
				Temp->StopStation = T[0].StopStation;
				Temp->StopTime = T[0].StopTime;
				Ans.push_back(*Temp);
			}
			T.erase(T.begin());
		}

		for(vector<Train>::iterator iter = Ans.begin(); iter != Ans.end(); iter++){
			if(iter->StartStation == 'A')
				 Answer1++;
			else Answer2++;
		}
		fprintf(out, "Case #%d: %d %d\n", TestNumber+1, Answer1, Answer2);
	}
	return 0;
}
