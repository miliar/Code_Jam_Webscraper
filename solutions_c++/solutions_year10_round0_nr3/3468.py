#include <iostream>
#include <fstream>
#include <string>
//#include <iomanip>
//#include <queue>

using namespace std;

const int EMPTY = -6969;
// the queue class begins here
class queue{
private:
	int q_front ;  // index of front of the queue
	int max_capacity ; // max_capacity for the queue
	int q_length ;  // length (or number of elements in queue)
	long * q ;      // the array the queue is stored in
	bool full(void)const{return (this->q_length == this->max_capacity);}
public:
	bool empty(void)const{return (this->q_length == 0) ;}
	queue(void){  // constructor when no max_capacity is specified
		this->q_front = 0 ;
		this->q_length = 0 ;
		this->max_capacity = max_capacity ; // use global max_capacity
		q = new long[this->max_capacity] ;
		clear() ;  // set every element to EMPTY constant
	}
	queue(int max_capacity){  // constructor with max_capacity
		if(this->max_capacity <= 0) this->max_capacity = max_capacity ;
		this->q_front = 0 ;
		this->q_length = 0;
		this->max_capacity = max_capacity ; // use client's max_capacity
		q = new long[this->max_capacity] ;
		clear() ;  // set every element to EMPTY constant
	}
	~queue(void){delete this->q ;}
	int length(void)const{return (this->q_length) ; } // get queue's length
	bool enqueue(long x){ // append element to back of queue
		if(empty()) this->q_front = 0 ;
		if(full()) return false ;
		int end = this->q_front + this->q_length ;
		if(end >= this->max_capacity)
			end = end % this->max_capacity ;
		this->q[end] = x ;
		this->q_length++ ;
		return true ;
	}
	long dequeue(void){ // retrieve first element from queue, remove it
		if(empty()) return EMPTY ;
		long temp = this->q[this->q_front] ;
		this->q[this->q_front] = EMPTY ;
		this->q_front++ ;
		if(this->q_front >= this->max_capacity)
			this->q_front = this->q_front % this->max_capacity ;
		this->q_length-- ;
		return temp ;
	}
	void clear(void){  // clear queue
		this->q_length = 0 ;
		for(int i = 0 ; i < this->max_capacity ; i++)
			this->q[i] = EMPTY ;
	}
	void print(void){ // print queue's contents
		cout << "Top of List is Top Priority" << endl ;
		cout << "---------------------------" << endl ;
		cout << "Front:" << this->q_front << endl ;
		cout << "Length:" << this->q_length << endl ;
		cout << "Max Capacity:" << this->max_capacity << endl ;
		if(empty()) {cout << "Empty Queue!" << endl ; return ;}
		int counter = 1 ;
		int end = this->q_front + this->q_length ;
		if(end >= this->max_capacity)
			end = end % this->max_capacity ;
		for(int i = this->q_front ; counter <= this->q_length; i++, counter++){
			if(i >= max_capacity)
				i = 0 ;
			cout << "Data " << counter << ".) " << this->q[i] << endl ;
		}
	}
	long next(void){
			return this->q[q_front];
	}
}; // end of queue class

int main() {

	ifstream file ("in");
	if (file.is_open()){
		long numCases;
		file >> numCases;

		// Run each Case
		unsigned long runs, pass, group;
		int numGroups, temp;
		unsigned long long money, ppl;
		for (int cCase = 1; cCase <=numCases; cCase++){
			money = 0;
			file >> runs;
			file >> pass;
			file >> numGroups;
			queue q(numGroups);
			queue tempQ(numGroups);
			//Put groups in queue
			for (int i=0; i<numGroups; i++){
				file >> group;
				q.enqueue(group);
			}
			//q.print();

			// Runs for each Run
			for (unsigned int i = 0; i < runs; i++){
				ppl = 0;
				while ((ppl + q.next()) <= pass){
					temp = q.dequeue();
					ppl += temp;
					tempQ.enqueue(temp);
				}
				//tempQ.print();
				money +=ppl;
				//cout << "M: " << money << endl;
				while(!tempQ.empty()){
					q.enqueue(tempQ.dequeue());
				}
			}

			 cout << "Case #" << cCase << ": " << money << endl;
			 //cCase = numCases;
		}
	} else {
		cout << "Error opening file" << endl;
	}
	file.close();
	return 0;
}
