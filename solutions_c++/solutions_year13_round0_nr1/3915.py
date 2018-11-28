#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime>
#include <climits>  
#include <fstream>  

using namespace std;

string data[5];

int diagD(char x, int posy, int posx, int &contx , int &conty){
   contx = x == 'X' ? contx+1 : (x=='T') ? contx+1 : contx;
   conty = x == 'O' ? conty+1 : (x=='T') ? conty+1 : conty;
   if(posy>3)
      return abs(contx-conty);
   if((x!=data[posy][posx] && x !='T' && data[posy][posx]!='T') || x =='.')
      return 0;
  
   return diagD(data[posy][posx], posy+1, posx+1, contx,conty);
}

int diagI(char x, int posy, int posx, int &contx , int &conty){
   contx = x == 'X' ? contx+1 : (x=='T') ? contx+1 : contx;
   conty = x == 'O' ? conty+1 : (x=='T') ? conty+1 : conty;
   if(posy>3)
      return abs(contx-conty);
   if((x!=data[posy][posx] && x !='T' && data[posy][posx]!='T') || x =='.')
      return 0;
   
   return diagI(data[posy][posx], posy+1, posx-1, contx,conty);
}

int col(char x, int posy, int posx, int &contx , int &conty){
   contx = x == 'X' ? contx+1 : (x=='T') ? contx+1 : contx;
   conty = x == 'O' ? conty+1 : (x=='T') ? conty+1 : conty;
   if(posx>3)
      return abs(contx-conty);
   if((x!=data[posy][posx] && x !='T' && data[posy][posx]!='T') || x =='.')
      return 0;
   
   return col(data[posy][posx], posy, posx+1, contx,conty);
}

int row(char x, int posy, int posx, int &contx , int &conty){
   contx = x == 'X' ? contx+1 : (x=='T') ? contx+1 : contx;
   conty = x == 'O' ? conty+1 : (x=='T') ? conty+1 : conty;
   if(posy>3)
      return abs(contx-conty);
   if((x!=data[posy][posx] && x !='T' && data[posy][posx]!='T') || x =='.')
      return 0;
   
  
   
   return row(data[posy][posx], posy+1, posx, contx,conty); 
}

int check(){
    int x=0, y=0;
    diagD(data[0][0], 1, 1, x,y);
    if(x==4 || y ==4)
       return x == 4 ? 1 : 2;
    
    x=0;
    y=0;
    diagI(data[0][3], 1, 2, x,y);
    if(x==4 || y ==4)
       return x == 4 ? 1 : 2;
    
    for(int j =0; j<4; j++){
       x=0;
       y=0;     
       col(data[j][0], j, 1, x,y);
       if(x==4 || y ==4)
          return x == 4 ? 1 : 2;
    }
    x=0;
    y=0;
    for(int j =0; j<4; j++){
       x=0;
       y=0;
       row(data[0][j], 1, j, x,y);     
       if(x==4 || y ==4)
          return x == 4 ? 1 : 2;
    }
    
    int cont =0;
    for(int i =0; i<4; i++)
       for(int j =0; j<4; j++){
          if(data[i][j]!='.')
             cont++;
       }
    
    return cont ==16 ? 0 : 3;
}

int main()
{
    ifstream in("entrada.in", ios::in);
    ofstream out("salida.out", ios::out);
    
    int num;
    string arr[] = {"Draw","X won","O won","Game has not completed"};
    string tmp;
    in>>num;    
    for(int i=0; i<num; i++){
       for(int j=0; j<4; j++){
          in>>tmp;
          data[j] = tmp;
       }
       out<<"Case #"<<(i+1)<<": "<<arr[check()]<<endl;
    }
    
}
