#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;

// queue node structure
struct QNode {
  int value;
  QNode *next;
};

class Queue {

private:
  QNode *head, *tail;

public:
  int no_of_elements;
  Queue () {
    head = NULL;
    tail = NULL;
    no_of_elements = 0;
  }
  int push (int val);
  int getHead ();
  int pop ();
  ~Queue();
};

int Queue::push (int val) {
  // if queue is empty
  if (this->head == NULL) {
    QNode* temp = new QNode;
    temp->value = val;
    temp->next  = NULL;
    this->head = this->tail = temp;
    this->no_of_elements++;
    return val;
  } else {
    QNode* temp = new QNode;
    temp->value = val;
    temp->next  = NULL;
    tail->next = temp;
    tail = temp;
    this->no_of_elements++;
    return val;
  }

  return -1;
}

int Queue::getHead () {
  if (this->head != NULL) {
    return this->head->value;
  } else {
    return -1;
  }
}

int Queue::pop () {
  // if queue is empty
  if (this->head != NULL) {
    int value = head->value;
    QNode *temp = head->next;
    delete head;
    head = temp;
    this->no_of_elements--;
    return value;
  } else {
    return -1;
  }
}

// Destructor

Queue::~Queue() {
  if (no_of_elements != 0) {
    QNode *node = head;
    while (node != this->tail) {
      QNode *temp = node->next;
      delete node;
      node = temp;
    }
    delete node;
  }
}

int main (int argc, char*argv[]) {
  ifstream input  (argv[1]);
  ofstream output ("theme_park_output.txt");

  // Get the number of test cases
  string line;
  getline (input, line);
  int no_of_test_cases = atoi(line.c_str());
  int test_case_index = 0;

  // For all the test cases
  while (test_case_index++ < no_of_test_cases) {
    Queue queue, tempQueue;
    getline (input, line);
    long rides_per_day = atoi(strtok (const_cast<char *>(line.c_str()), " "));
    long max_ride_size = atoi(strtok (NULL, " "));
    long no_of_groups  = atoi(strtok (NULL, " "));
    long cost_of_ride  = 0;
    //    output << "R "<< rides_per_day << " k "<< max_ride_size << " G " << no_of_groups << endl;

    // initialize the queue with groups
    getline (input, line);
    int members_in_grp = atoi(strtok (const_cast<char *>(line.c_str()), " "));
    queue.push (members_in_grp);
    //output << members_in_grp << " ";
    for (int grp_index=0; grp_index<no_of_groups-1; grp_index++) {
      members_in_grp = atoi(strtok (NULL, " "));
      queue.push (members_in_grp);
      //output << members_in_grp << " ";
    }
    //    output << endl;
    // for all possible rides
    for (long index=0; index<rides_per_day; index++) {
      long ppl_in_ride = 0;
      while ( ((ppl_in_ride+queue.getHead()) <= max_ride_size) && (queue.no_of_elements != 0)) {
	int head = queue.pop();
	ppl_in_ride += head;
	tempQueue.push(head);
	//output << head << " "; 
      }
      cost_of_ride += ppl_in_ride;
      //output << "#" << ppl_in_ride << " ";


      // push the elements poped back to the queue
      while (tempQueue.no_of_elements != 0) {
	queue.push(tempQueue.pop());
      }
    }
    output << "Case #" << test_case_index << ": " << cost_of_ride << endl;
  }

  return 0;
}
