#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int abs(int i){
   return (i<0)?-i:i;
}

int main(int argc, char** argv){
   string infileName = argv[1];
   string outfileName = argv[2];
   ifstream inputFile(infileName.c_str(),ios::in);
   ofstream outFile(outfileName.c_str(),ios::out);
   
   int T;
   inputFile >> T;
   int N;
   
   for(int j = 0; j < T ; ++j){
      inputFile >> N;
      int color;
      string color_temp;
      int position = 0;
      
      int last_color = -1;
      int last_pos[2] = {1,1};
      int step = 0;
      int buffer = 0;
      for(int i = 0; i < N; ++i){
         inputFile >> color_temp >> position;
         color = (color_temp == "B")?1:0;
         int diff = abs(position - last_pos[color]);
         if(color != last_color){
            if(buffer > diff){
               step += 1;
               buffer = 1;
            }else{
               step += diff + 1 - buffer;
               buffer = diff + 1 - buffer;
            }
         }else{
            buffer += diff + 1;
            step += diff + 1;
         }
         last_color = color;
         last_pos[color] = position;
      }
//      cout<<"Case #"<<j+1<<": "<<step;
      outFile << "Case #"<<j+1<<": "<<step<<endl;
//      if(j != T-1) {
//         cout<<endl;   
//      }
   }
}
