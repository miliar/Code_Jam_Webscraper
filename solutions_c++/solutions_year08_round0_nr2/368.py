#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void sort( char arr[][100], int size)
{
 	for (int i=1; i<size; i++){
		for(int j=0; j<i; j++){
			if(strcmp(arr[i], arr[j])<0){
				char tmp[100];
				strcpy(tmp, arr[i]);
				strcpy(arr[i], arr[j]);
				strcpy(arr[j], tmp);
			}
				
		}
	}
}

int find_first(int start[][100],int good[][100], int & arrnum, int N[])
{
	int res=-1;
	int min=24*60;
	for(int arrays=0; arrays<2; arrays++){
		for(int i=0; i<N[arrays]; i++){
			if(start[arrays][i]<min && good[arrays][i]==1){
				min=	start[arrays][i];
				arrnum=arrays;
				res = i;
			}
		}
	}
	 return res;
}
int find(int time, int start[][100], int good[][100],int arrnum, int N)
{
	int res=-1;
	int min=time+24*60;
		for(int i=0; i<N ;i++){
			if(start[arrnum][i]>=time && start[arrnum][i]<min && good[arrnum][i]==1){
				min=	start[arrnum][i];
				res = i;
			}
		}
	//out<<"find: arr="<<arrnum<<" res="<<res<<" time="<<time<<"\n";
	 return res;
}

int main () {
	//string line;
	int cases;
	cin >> cases;
	int good[2][100];
	int start_tm[2][100];
	int end_tm[2][100];
	for (int j=1; j<=cases; j++){
		int turnaround ;
		
		cin >> turnaround; cin.get();
		int N[2];
		cin >> N[0]>> N[1];cin.get();
		for(int i=0; i<N[0]; i++){
			int hr1, hr2, m1, m2;
			cin>>hr1; cin.get(); cin>>m1; cin.get();cin>>hr2;cin.get();cin>>m2;
//cout << hr1<<" " <<m2;
			start_tm[0][i] = hr1*60+m1;
			end_tm[0][i] = hr2*60+m2+turnaround;
			good[0][i]=1;
		}
		for(int i=0; i<N[1]; i++){
			int hr1, hr2, m1, m2;
			cin>>hr1; cin.get(); cin>>m1; cin.get();cin>>hr2;cin.get();cin>>m2;
			start_tm[1][i] = hr1*60+m1;
			end_tm[1][i] = hr2*60+m2+turnaround;
			good[1][i]=1;
		}
		int first;
		int curr_arr=0;
		first=find_first(start_tm,good,curr_arr, N);
		int left_from = curr_arr;
		//cout<<"first"<<curr_arr<<"/"<<first<<"\n";
		int Trains[2] ; Trains[0]=0; Trains[1]=0;
		while(first>=0){
			good[curr_arr][first]=0;
			int next=first;
			do{
				 next=find(end_tm[curr_arr][next],start_tm,good, 1-curr_arr, N[1-curr_arr]);
				if(next>=0){ 
					curr_arr = 1-curr_arr;
					good[curr_arr][next]=0;
				}
			}while(next>=0);
			Trains[left_from]++;
		first=find_first(start_tm,good,curr_arr, N);
		//cout<<"first"<<curr_arr<<"/"<<first<<"\n";
			left_from=curr_arr;
		}
		cout<<"Case #"<<j<<": "<<Trains[0]<<" "<<Trains[1]<<"\n";
	}
}