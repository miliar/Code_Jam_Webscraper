#include <iostream>
#include <vector>

using namespace std;

class node {
  public:
    char letter;
    vector<node*> nodes;
    void addword(string word);
    void search(int &counter, string word);
    node* find(char letter);
};

void node::addword(string word){
  if(word.length()){
    // pop first letter off
    char let = word.at(0);
    word = word.substr(1);
    // search vector for letter
    node* vnode = find(let);
    // if letter not found, add node
    if(!vnode){
      node* newnode = new node();
      newnode->letter = let;
      nodes.push_back(newnode);
      // add remainder of word to new node
      newnode->addword(word);
    }
    // else add remainder of word to found node
    else vnode->addword(word);
  }
}

void node::search(int &counter, string word){
  if(word.length()==0) counter++;
  else{
    // pop letter or group of letters
    string group = word.substr(0,1);
    word = word.substr(1);
    if(group=="("){
      group = "";
      string letter = word.substr(0,1);
      word = word.substr(1);
      while(letter!=")"){
	group += letter;
	letter = word.substr(0,1);
	word = word.substr(1);
      }
    }
    // for each letter in the group, search that node (if it exists)
    for(int i=0;i<group.length();i++){
      node* findnode = find(group.at(i));
      if(findnode) findnode->search(counter,word);
    }
  }
}

node* node::find(char letter){
  vector<node*>::iterator vnode = nodes.begin();
  while(vnode!=nodes.end() && (*vnode)->letter != letter) vnode++;
  if(vnode==nodes.end())return NULL;
  return (*vnode);
}

int main(){
  // build graph
  node *root = new node();
  root->letter = '0';
  int L, D, N;
  cin >> L >> D >> N;
  for(int i=0;i<D;i++){
    string word;
    cin >> word;
    root->addword(word);
  }
  for(int i=0;i<N;i++){
    string testcase;
    cin >> testcase;
    int counter = 0;
    root->search(counter, testcase);
    cout << "Case #" << i+1 << ": " << counter << endl;
  }
    
  return 0;
}
