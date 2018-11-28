#include<iostream>
using namespace std;

class word{
public:
  unsigned int value[16];
  static int len;

  word(){
    for(int i = 0; i < len ;i ++){
      value[i] = 0;
    }
 
  }
  static void setlen(int a){
    len = a;
  }
  int setvalue(char a[]);
  int makequery(char a[]);
  int compare(word &x);
  void display();
};

int word::len = 0;

word* dict = NULL;

int word::setvalue(char a[]){

  for(int i = 0; a[i] != 0; i++)
    value[i] = 1 << (a[i] - 'a');

}

int word::makequery(char a[]){

  for(int i = 0, j = 0; a[i] != 0; i++, j++){
    if(a[i] == '('){
      i++;
      while(a[i] != ')'){
	unsigned int temp = 1 << ( a[i] - 'a');
	value[j] = value[j] | temp;
	i++;
      }

    }
    else value[j] = 1 << ( a[i] - 'a');

  }

}

int word::compare(word &query){

  unsigned int val = (value[0] & query.value[0]);
  for(int i = 1; i < len; i++){
    val = (val && (value[i] & query.value[i]) );
  }

  return val;
}

void word::display(){
  for(int i =0 ; i < len; i++)
    cout<< value[i];
  cout<<endl;
}

int main(){

  int wordlen, dictsize, noprob;
  char theword[17];

  //  cout<<sizeof(int)<<endl;
  //  cout<< (1 & 2);

  cin>>wordlen>>dictsize>>noprob;
  dict = new word[dictsize];
  dict[0].setlen(wordlen);

  for(int i = 0; i < dictsize; i++){
    cin>>theword;
    //   dict[i] = new word();

    dict[i].setvalue(theword);
    //    dict[i].display();
  }

  //dictionary made


  char jumbled[500];
  for(int i = 0; i < noprob; i ++) {
    word query;
    cin>>jumbled;
    query.makequery(jumbled);
    //    query.display();
    int pos = 0;
    for(int j = 0; j < dictsize; j++){
      if(dict[j].compare(query))
	pos++;
    }
    
    cout<<"Case #"<<(i+1)<<": "<<pos<<endl;
  }


}
