#include <iostream>
#include <list>

using namespace std;

class Node{
  public:	
    char str[200]; 
    list<Node*> child;	
  
    Node(){
        str[0] = 0;	    
    }
};

Node* root;
int ans;
char delims[] = "/";
char token[200][200];
int len;


void build(Node* n, int pos, bool add){
    if(pos >= len)
        return;	    
    Node* tmp = new Node();
    strcpy(tmp->str, token[pos]);    

    n->child.push_back(tmp);
    if(add)
        ans++;	    
   //  cout << "pos:" << pos << " " << token[pos] << " ans:" << ans << '\n'; 
    
    build(tmp, pos+1, add);
}

void check(Node* n, int pos, bool add){

    bool have = false;

   // cout << "str:" << n->str << " size:" << n->child.size() << '\n'; 

    for(list<Node*>::iterator it = n->child.begin(); it != n->child.end(); it++){
//cout << "it:" << (*it)->str << " token:" << token[pos] << '\n';  
       if(strcmp((*it)->str,token[pos])==0){
            check(*it, pos+1, add);
	    have = true;
	} 
    }

    if(!have)
        build(n, pos, add);	    
}



void split(char* str){
     char *result = NULL;
     result = strtok( str, delims );
     len = 0;
     while( result != NULL ) {
       //  token[len++] = result;
	 strcpy(token[len++], result);
         result = strtok(NULL, delims);
     }
   
  /*   for(int i =0 ; i < len; i++)
         cout << i << ":" << token[i] << '\n';	     
*/
}


int main(){

    int T, cases;
    cin >> T;
    cases = T;
    while(T--){
        root = new Node(); 
    
        int a,b;
        cin >> a >> b;

	ans = 0;
	char s[1000];
	for(int i = 0; i < a; i++){
	    cin >> s;
            split(s);	    
	    check(root, 0, false);
	}

	for(int j = 0; j < b; j++){
	    cin >> s;
	    split(s);
            check(root, 0, true);
	}

        cout << "Case #" << (cases - T) << ": " << ans << '\n';	
    }

}
