#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
  }



int l;
int d;
int n;

char dict[5000][15];
bool pattern[15][26];

int answer;

void read() {

     scanf("%d", &l);
     scanf("%d", &d);
     scanf("%d", &n);     
     getLine(); // SE LIGUE
      
     for(int i = 0; i < d; i++)
     {
             string s = getLine();
          
             for(int j = 0; j < l; j++)
             {
                    dict[i][j] = s[j];
             }           
     } 
}
 

int InsertPattern(string s) {
     memset(pattern,false,390);
     
     int sSize = s.size();
     
     int L = 0;
     
     for(int i= 0; i < sSize; i++)
      {
              if(s[i] == '('){
                      i++;
                      while(s[i] != ')')                    
                      {
                              pattern[L][s[i] - 'a'] = true;                              
                              i++;
                      }
                      //i++;                      
              }
              else{
                   pattern[L][s[i] - 'a'] = true;                   
              }              
              L++;
      } 
}

void CountMatchs(){
    answer = d;

    for(int i = 0; i < d; i++)
    {
         for(int j = 0; j < l; j++)
         {
              if( pattern[j][dict[i][j] - 'a'] == false)
              {
                    answer--;
                    break;
              }   
         }       
    }
}

void process() {            
    InsertPattern(getLine());    
    CountMatchs();     
}


int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	read();
	//printf("read");
	for(int i = 0; i < n; i++)
    {
	     process();
         printf("Case #%d: %d\n", i + 1, answer);
    }
	
}
