#include <iostream>
//#include <algorithm>
// for using dynamic array
//#include <vector>
//#include <cmath>
//#include <cstdio>
#include <string>
// using stl
#include <stack>
//#include <queue>
#include <set>
#include <map>
//#include <string.h>
//#include <cassert>

using namespace std;
typedef pair<char,char> PCC;
 typedef map<PCC,char> M;


int main() {
   int test_cases;
   cin>>test_cases;

  for(int alpha=1;alpha<=test_cases;alpha++) //takes input
   {
      int c,N,D;
      char answer[200];
      int topOfStack=0;
      M combination;
      map<char,char> opposite;
      
      cin>>c;
      
      char temp[10];
      for(int i=0;i<c;i++) { // invoke the elements
         cin>>temp;
         combination[make_pair(temp[0],temp[1])]=temp[2];
         combination[make_pair(temp[1],temp[0])]=temp[2];
      }
      
      
     cin>>D;   // specify pairs of base that are opposed to each other
      
     for(int i=0;i<D;i++) {
         cin>>temp;
         opposite[temp[0]]=temp[1];
         opposite[temp[1]]=temp[0];
      }
 
    
      cin>>N;
      
      char ch;
      for(int i=0;i<N;i++) {
         cin>>ch;
         int opposite_check=0;
     
         if(topOfStack==0) {
         answer[topOfStack++] = ch;
         continue;
         }
        
         else {
            
            if(combination[make_pair(ch,answer[topOfStack-1])]) {
            topOfStack--;
            answer[topOfStack] = combination[make_pair(ch,answer[topOfStack])];
            topOfStack++;
            continue;
            }
            
            else {
                  for(int i=0;i<topOfStack;i++) {
                        if(opposite[ch]==answer[i]) {
                        topOfStack=0;
                        opposite_check=1;
                        break;
                        }            
                   }            
            }
            
            if(opposite_check)
            continue;
            else        
            answer[topOfStack++] = ch;
            
         }      
      }

      //to print the answer
      cout<<"Case #"<<alpha<<": [";
      for(int i=0;i<topOfStack;i++) {
         if(i<topOfStack-1)
         cout<<answer[i]<<" ,";
         else
         cout<<answer[i];
      }
     	cout<<"]"<<endl;

   
   }
   return 0;
}

