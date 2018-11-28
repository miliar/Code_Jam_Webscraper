#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class myStack{
public:
   void init(int N){
      _data = new int[N];
      _top = 0;
   }
   
   void push(int i){
      _data[_top++] = i;
   }
   
   void pop(){
      if(_top != 0) _top--;
   }
   
   int top(){
      if(_top != 0) return _data[_top-1];
      else return 0;
   }
   
   void clear(){
      _top = 0;
   }
   
   void print(ofstream* outFile){
      for (int i = 0; i < _top-1; i += 1)
      {
         cout << char(_data[i])<<", ";
         *outFile << char(_data[i])<<", ";
      }
      if(_top > 0) cout << char(_data[_top-1]);
      if(_top > 0) *outFile << char(_data[_top-1]);
   }
   
   int find(int k){
      for (unsigned int i = 0; i < _top; i += 1)
      {
         if(k == _data[i]) return i+1;
      }
      return 0;
   }
private:
   int _top;
   int* _data;
};


int checkCombine(int a,int b,char** combine, int C){
   for (unsigned int i = 0; i < C; i += 1)
   {
      if(a == combine[i][0] && b == combine[i][1] || 
         a == combine[i][1] && b == combine[i][0] ){
         return combine[i][2];   
      }
   }
   return 0;
}
int checkOpposed(int a,char** opposed, int D){
   for (unsigned int i = 0; i < D; i += 1)
   {
      if(a == opposed[i][0]) return opposed[i][1];
      else if(a == opposed[i][1]) return opposed[i][0];
      else return 0;
   }
}



int main (int argc, char const* argv[])
{
   ifstream inFile(argv[1],ios::in);
   ofstream outFile(argv[2],ios::out);
   
   int T;
   inFile >> T;
   
   for (unsigned int i = 0; i < T; i += 1)
   {
      cout << "Case #"<< i+1 << ": [";
      outFile << "Case #"<< i+1 << ": [";
      int C;
      int D;
      int N;
      inFile >> C;
      char** combine = new char*[C];
      for (unsigned int j = 0; j < C; j += 1)
      {
         combine[j] = new char[3];
         inFile >> combine[j];
      }
      inFile >> D;
      char** opposed = new char*[D];
      for (unsigned int j = 0; j < D; j += 1)
      {
         opposed[j] = new char[2];
         inFile >> opposed[j];
      }
      inFile >> N;
      char* input = new char[N];
      inFile >> input;
      
      myStack m;
      m.init(N);
      for (unsigned int j = 0; j < N; j += 1)
      {
         if(checkCombine(input[j],m.top(),combine,C)){
            char temp = checkCombine(input[j],m.top(),combine,C);
            m.pop();
            m.push(temp);
         }else if(checkOpposed(input[j],opposed,D)){
            char temp = checkOpposed(input[j],opposed,D);
            if(m.find(temp)) {
               m.clear();
            }else{
               m.push(input[j]);
            }
         }else{
            m.push(input[j]);
         }
      }
      m.print(&outFile);
      cout<<"]"<<endl;
      outFile<<"]"<<endl;
   }
}

      
