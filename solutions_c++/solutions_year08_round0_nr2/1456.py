//#include<process.h>
#include<iostream>
//#include<conio.h>
#include<stdlib.h>
#include <stdio.h>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

#define TRIPS 150


class Hour{
	public:
	int hours;
	int minutes;
	Hour();
	Hour(int, int);
	int Greater(Hour);
	int Greater(Hour, int);
	int Equals(Hour);
	friend Hour Copy(Hour);
};

int Hour::Equals(Hour h){

	return ((hours == h.hours) && (minutes == h.minutes));
}

Hour Copy(Hour h){
	Hour res(h.hours, h.minutes);
	return res;
}

Hour::Hour(int h, int m){

	hours = h;
	minutes = m;

}

int Hour::Greater(Hour h, int offset){

int offset_h, offset_min, min, hou;

	offset_h = offset / 60;
	offset_min = offset % 60;
	min = (offset_min + minutes) % 60;
	hou = (offset_min + minutes) / 60 + offset_h + hours;

	if (hou > h.hours){
		return 1;

	}
	else
	if (hou < h.hours){
		return 0;
	}
	else
	if (min > h.minutes){
		return 1;
	}
	else
		return 0;

}

int Hour::Greater(Hour time){

	if(hours > time.hours){
		return 1;
	}
	else
	if(hours < time.hours){
		return 0;
		
	}
	else{
		if(minutes > time.minutes){
			return 1;
		}
		else
			return 0;
			

	}
	

}


int Partition(int low, int high, Hour *arr[TRIPS]);
void Quick_sort(int low, int high, Hour *arr[TRIPS]);
void Init(Hour *arr[TRIPS], int size);


int main()
{
int *a,n,low,high,i, N, big, small, a_trips, b_trips, trains_a, trains_b, arr_index, dep_index, T;
//Hour *a_arr, *a_dep, *b_arr, *b_dep;
Hour  *ad[TRIPS], *ba[TRIPS], *bd[TRIPS], *aa[TRIPS];
/* 
 * aa - arrivals at a, ad - departures from a
 * ba - arrivals AT b, ad - departures from b
 * */
string line;
ifstream f("B-large.in");
ofstream fout("B-large.out");

cout << "pocz " << endl;

Init(aa, TRIPS);
Init(ad, TRIPS);
Init(ba, TRIPS);
Init(bd, TRIPS);

cout << "po init" << endl;


if (f.is_open()){
	cout << "is open" << endl;	
	getline(f, line);
	cout << line.c_str() << endl;
	sscanf(line.c_str(), "%d", &N);
	cout << N << endl;
	for(big = 1; big <= N; big++)
	{	//cout << "tutaj" << endl;
		getline(f, line);
		sscanf(line.c_str(), "%d", &T);
		getline(f, line);
		sscanf(line.c_str(), "%d %d", &a_trips, &b_trips);
		//cout << "trips " << a_trips << " " << b_trips << endl;
		/*a_dep = new Hour[a_trips];
		a_arr = new Hour[b_trips];
		b_dep = new Hour[b_trips];
		b_arr = new Hour[a_trips];
		*/
		/* a trips */
		for(small = 0; small < a_trips; small++){
			getline(f, line);
		//	cout << line.c_str() << endl;
			sscanf(line.c_str(), "%d:%d %d:%d", &(ad[small]->hours), &(ad[small]->minutes), &(ba[small]->hours), &(ba[small]->minutes));

		}/* for small */
		
		/* b trips */
		for(small = 0; small < b_trips; small++){
			getline(f, line);
			sscanf(line.c_str(), "%d:%d %d:%d", &(bd[small]->hours), &(bd[small]->minutes), &(aa[small]->hours), &(aa[small]->minutes));

		}/* for small */
		high = a_trips - 1;
		low = 0;
		//cout << "przed qsort" << endl;
		Quick_sort(low, high , ad);
		//cout << "qsort 2" << endl;
		Quick_sort(low, high , ba);
		//cout << "qsort 3" << endl;

		high = b_trips - 1;
		Quick_sort(low, high , bd);
		//cout << "qsort 4" << endl;

		Quick_sort(low, high , aa);
		/*cout << big << "UWAGA aa ";
		for (i = 0; i < b_trips; i++){
			cout << aa[i]->hours << ":" << aa[i]->minutes << " ";
		}
		cout << endl;
		cout << big << "UWAGA ad ";
		for (i = 0; i < a_trips; i++){
			cout << ad[i]->hours << ":" << ad[i]->minutes << " ";
		}
		cout << endl;
		cout << big<< " UWAGA ba ";
		for (i = 0; i < a_trips; i++){
			cout << ba[i]->hours << ":" << ba[i]->minutes << " ";
		}
		cout << endl;
		cout << big << " UWAGA bd ";
		for (i = 0; i < b_trips; i++){
			cout << bd[i]->hours << ":" << bd[i]->minutes << " ";
		}
		cout << endl;
		*/
		/* counting trains */
		trains_a = 0; trains_b = 0;
		arr_index = 0; dep_index = 0;
		while (a_trips > 0){
			if (b_trips == 0){
				trains_a = a_trips;
				break;
			}
			if (aa[arr_index]->Greater(*(ad[dep_index]), T)){
				trains_a ++;
				dep_index++;
			}
			else {
				arr_index++;
				dep_index++;
			}
			if (dep_index >= a_trips)
				break;
			if (arr_index >= b_trips){
				
				trains_a += a_trips  - dep_index;
				break;
			}


		}
		dep_index = 0; arr_index = 0;
		while (b_trips > 0){
			if (a_trips == 0) {
				trains_b = b_trips;
				break;
			}
			if (ba[arr_index]->Greater(*(bd[dep_index]), T)){
				trains_b ++;
				dep_index++;
			}
			else {
				arr_index++;
				dep_index++;
			}
			if (dep_index >= b_trips)
				break;
			if (arr_index >= a_trips){
				
				trains_b += b_trips  - dep_index;
				break;
			}


		}


		fout << "Case #" << big << ": " << trains_a << " " << trains_b << endl;
	}/* for big */
	fout << flush;
	fout.close();

}else{
	cout << "Nie mozna otworzyc pliku" << endl;
}


//getch();

return 0;
}

/*Function for partitioning the array*/

int Partition(int low, int high, Hour *arr[TRIPS])
{ int i/*,itr*/;
  Hour *pivot, *high_vac, *low_vac;
  /*Hour pivot = Hour(0, 0);
  Hour high_vac = Hour(0, 0);
  Hour low_vac = Hour(0, 0);*/
  pivot = arr[low];
  if ((high > low)&&(high - low <= 1) && (arr[high]->Equals(*pivot))){
      return low;
  }
  while(high>low){ 
  	high_vac = arr[high];

  	while((*high_vac).Greater(*pivot)|| high_vac->Equals(*pivot))
  	{
    		if(high<=low) break;
    		high--;
   		high_vac = arr[high];
  	}

  	arr[low] = high_vac;
	low_vac = arr[low];
	while((*pivot).Greater(*low_vac))
  	{
    		if(high<=low) break;
		low++;
	    	low_vac = arr[low];
  	}
  	arr[high] = low_vac;

  }/* while high > low */
  arr[low] = pivot;
  return low;
}

void Quick_sort(int low, int high, Hour* arr[TRIPS])
{
  int Piv_index,i;
  //cout<< "qsort "<<low << " " << high << endl;
  if(low<high)
  {
   Piv_index=Partition(low, high, arr);
  // cout << "po partition" << endl;
   Quick_sort(low, Piv_index-1, arr);
   Quick_sort(Piv_index+1, high, arr);
  }
}
void Init(Hour *arr[TRIPS], int size){
int i;
	//cout << "init" << endl;
	for(i = 0; i < size; i++){
		arr[i] = new Hour(0, 0);
//		cout << i << endl;


	}

}
