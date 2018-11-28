#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <queue>
#include <vector>
using namespace std;

typedef struct n{
 n* next[30];
 int ends;
}node;

struct subsel {
  int num;
  char crka;
  node* ch;
};

int opcij;

class compare
{
public:
	bool operator()(subsel &input1, subsel &input2)
	{
		return input1.num>input2.num;
	};
};

int letters,letplus;

void adddword(char *bes, node *curr)
{
  for(int i=0;i<strlen(bes);i++){
    if(curr->next[bes[i]-'a'] == 0){
      node *item = new node;
      curr->next[bes[i]-'a'] = item;
      curr = item;
    } else {
      curr = curr->next[bes[i]-'a'];
    }
  }
  curr->ends = 1;
}

//ni potrebno v nalogi, a uporabno za kakšen začetni debug branja podatkov
int isthere(char *bes, node *curr)
{
  for(int i=0;i<strlen(bes);i++){
    if(curr->next[bes[i] - 'a'] == 0){
      return 0;
    } else {
      cout << bes[i] << endl;
      curr = curr->next[bes[i]-'a'];
    }
  }
  if(curr->ends == 1){
    return 1;
  }else{
    return 0;
  }
}

string cutit(string c){
  string nova;
  bool t=false;
  int i=0;
  while(t==false){
    if(c[i] == ')') t=true;
    i++;
  }
  nova = "";
  for(int j=0;j<c.length()-i;j++)
    nova += c[j+i];
  
  return nova;
}

string cut1(string c){
  string nova;
  nova = "";
  for(int j=0;j<c.length()-1;j++)
    nova += c[j+1];
  
  return nova;
}

void chk(node *curr, string s){
//     cout << s << endl;
    string ss;
	if(s[0] != '('){
// 	  cout << curr->next[2] << endl;
// 	  cout << s[0] << endl;
	  if(curr->next[s[0] - 'a'] != 0){
	    
	    curr = curr->next[s[0] - 'a'];
	    s = cut1(s);
	    
	    if(s.length() == 0){
	      opcij++;
	    } else {
	      // pusn na kju nazaj
		chk(curr, s);
	    }
	  }
	} else {
	    // je opcij vec; k-free
	    for(int j=1;j<s.length();j++){
	      if(s[j] == ')') break;
	      
	      ss = s; 
	     
	      if(curr->next[s[j] - 'a'] != 0){
		ss = cutit(s);
		
		if(ss.length() == 0){
		  opcij++;
		} else {
		    chk(curr->next[s[j] - 'a'],ss);
		}
	      }	      
	    }
	}
	
}

int main()
{
  //create root
  node *root = new node;
  
  char c[20];
  string s;
  int n,l,d,k;

  scanf("%d %d %d",&l,&d,&n);
  for(int i=0;i<d;i++){
    scanf("%s", c);
    adddword(c, root);
  }
 
  
  for(int i=0;i<n;i++){
      //let's check each case
      cin >> s;
      opcij = 0;
      
      chk(root, s);
      
      cout << "Case #"<< i+1 <<": "<< opcij << endl;
     
  }

  return 0;
}