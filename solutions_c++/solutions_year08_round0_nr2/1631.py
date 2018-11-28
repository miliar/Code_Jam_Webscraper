// trains

#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <sstream>
#define max 100
using namespace std;

//na - no of trips from a to b
//nb - no of trips from b to a
enum timings{ departure, available};
enum city{ citya, cityb};
int a,b;
typedef struct event{

	timings t;
	city c;
	int time;

};

bool myfunction (event e1, event e2) {
	if (e1.time == e2.time)
		return (e2.t < e1.t);
	return (e1.time < e2.time); 
}

int NA,NB;
vector <event> event_vector;
int needed[max];
int avail[max];

	
void read()
{
	event ee;
	event_vector.clear();
	int turn_around;
	string l1,l2;
	cin >> turn_around;
	//cout << " turn around " << turn_around << endl;
	cin >> NA >> NB;
	//cout << NA << " " << NB << endl;
	//getline(cin, NB);
	getline(cin , l1);
	for(int k = 0; k < NA; k++)
	{
		
		city c;
		timings t;
		string s1, s2;
		int dep1, dep2, arr1, arr2;
		char cc;
		getline(cin, l1);
		istringstream ss(l1);
		ss >> s1 >> s2;
		istringstream ss1(s1);
		istringstream ss2(s2);
		ss1 >> dep1 >> cc >> dep2;
		
		ee.time = 60*dep1 + dep2;  
		ee.t = departure; 
		ee.c = citya; 
		event_vector.push_back(ee);
		ss2 >> arr1 >> cc >> arr2;
		
		ee.time = 60*arr1 + arr2+turn_around; 
		ee.t = available; 
		ee.c = cityb; 
		event_vector.push_back(ee);
	}
	
	for(int k = 0; k < NB; k++)
	{
		
		city c;
		timings t;
		string  s1, s2;http://mail.google.com/mail/?shva=1#inbox
		int dep1, dep2, arr1, arr2;
		char cc;
		getline(cin, l2);
		istringstream ss(l2);
		ss >> s1 >> s2;
		istringstream ss1(s1);
		istringstream ss2(s2);
		ss1 >> dep1 >> cc >> dep2;
		
		ee.time = 60*dep1 + dep2; 
		ee.t = departure; 
		ee.c = cityb; 
		event_vector.push_back(ee);
		ss2 >> arr1 >> cc >> arr2;
		
		ee.time = 60*arr1 + arr2+turn_around;  
		ee.t = available; 
		ee.c = citya;
		event_vector.push_back(ee);

	}
	

}
void print()
{
	return ;

}



void solution()
{
	//event ee;
	a = 0; b = 1;
	needed[a] = needed[b] = 0;
	avail[a] = avail[b] = 0;
	//sort the vector in increasing order of the time
	sort(event_vector.begin(), event_vector.end(), myfunction);
	for(int k = 0; k < event_vector.size(); k++)
	{
		int tt = event_vector[k].time;
		if (event_vector[k].t == available)
		{
			avail[event_vector[k].c]++;
			//cout << "avaiable time " << (tt/60) << ":" << (tt%60) << endl;
		}
		else
		{
			event_vector[k].t = departure;
			//cout << " departure time " << (tt/60) << ":" << (tt%60) << endl;
			if( avail[event_vector[k].c] > 0){
				
				avail[event_vector[k].c]--;
				//cout << " city " << event_vector[k].c << endl;
				//cout << " available " << avail[event_vector[k].c] << endl;
			}
			else
			{ needed[event_vector[k].c]++;
			   //cout << " needed " << needed[event_vector[k].c] << endl;
			  }
		}
		//cout <<
	}

	
	return ;

}
void process()
{
	int test;
	cin >> test;
	for(int k = 1; k <= test; k++)
	{
		read();
		solution();
		cout << "Case #" << k << ": " << needed[a] << " " << needed[b] << endl;
	}
	return ;

}

int main()
{
	process();
	return 0;
}
