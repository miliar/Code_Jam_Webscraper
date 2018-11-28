// queue::push/pop
#include <iostream>
#include <queue>
#include <conio.h>
#include <fstream>

using namespace std;

int main ()
{

	ifstream in("C-small-attempt1.in");
    ofstream out("C-small.out");
  queue<int> myqueue;
  int r , k , n , cases;
int t;
	in >> cases;

if (cases<1 || cases>50) {
        cout<<"Wrong Number of test cases"; 
        getch();
        exit(0);
        }

	for (int loops = 0 ; loops < cases ; loops++){

	in >> r >> k >> n;
 

if (r<1 || r>1000) {
        cout<<"Wrong inputs for R"; 
        getch();
        exit(0);
        }
else        
if (k<1 || k>100) {
        cout<<"Wrong inputs for k"; 
        getch();
        exit(0);
        }
else
if (n<1 || n>10) {
        cout<<"Wrong inputs for N"; 
        getch();
        exit(0);
        }


  for (int i= 0 ; i<n ; i++){
  
	  in >> t;
	  myqueue.push(t);
  
  }




  int cost = 0;

 

  for (int i=0 ; i<r ; i++)
  {
  int sum = 0;
 //	  cout << "round # " << i+1 << endl;
	  int p=0;
	  while(1){
	  
			p++;
		  if (sum + myqueue.front() >k) break;
		
		  sum += myqueue.front();
		  myqueue.push(myqueue.front());
		  myqueue.pop();
			
		  //cout << sum << endl;
		  if (p>=n) break;
		  //if (n=1) break;

	  
	  }
		cost += sum;

	//	cout <<  " CAse : " << cost << endl;
  
  }
		out <<  "Case #" <<loops+1<< ": "<<cost << endl;
//  getch();
  while (!myqueue.empty()){
        myqueue.pop();
        }
	}

//system("pause");


  return 0;
}
