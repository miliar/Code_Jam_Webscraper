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
char dictionary[5000][15];
int answer;

void read() {

     scanf("%d", &l);
     scanf("%d", &d);
     scanf("%d", &n);
     
     getLine();
     
     char s[l];
     
     for(int i = 0; i < d; i++)
     {
         gets(s);
         for(int j = 0; j < l; j++)
         {
            dictionary[i][j] = s[j];       
         }
     }
     
} 

void process() {
            
    string s = getLine();
    
    string now;
    answer = d;
    
    bool match[d];
    for(int i = 0; i < d; i++)
    {
        match[i] = true;    
    } 
    
    for(int j = 0; j < l; j++)
    {
       if(s[0] == '(')
       {
           int index = s.find_first_of(')');
           now = s.substr(1,index-1);
           s = s.substr(index+1);
       }else
       {
           now = s[0];
           s = s.substr(1);
       }
       
       for(int i = 0; i < d; i++)
       {
           if(match[i] && now.find(dictionary[i][j]) == string::npos)
           {
           match[i] = false;
           answer--;
           } 
       } 
       
    }
    
}


int main() {

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	read();
	//printf("read");
	for(int i = 0; i < n; i++)
    {
	     process();
         printf("Case #%d: %d\n", i+1, answer);
    }
	
}
