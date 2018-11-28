#include <iostream>
#include <fstream>
#include <string.h>
#include <list>

using namespace std;

ifstream fin;
ofstream fout;

list<char> runCase();

list<int> checkTestStrInOpposeList(char testChar,char* oppose);
char getPairOppose(int charPos,char* oppose);
char checkTestStrInCombineList(char testChar,char testChar2,char *combine);

int main(int argc, char** argv){
  if(argc != 2){
    cout << argv[0] << " filename" << endl;
  }
  char filename[50];
  strcpy(filename,argv[1]);
  fin.open(strcat(filename,".in"));
  strcpy(filename,argv[1]);
  fout.open(strcat(filename,".out"));

  if(!fin.is_open()){
    cout << "Could not open the file : " << argv[1] << endl;
    return -1;
  }

  int numCase;
  fin >> numCase;
  //cout << "number case : " << numCase << endl;

  int i;
  for(i=0;i<numCase;i++){
    list<char> result=runCase();
    list<char>::iterator iter;
    cout << "Case #" << i+1 << ": [";
    fout << "Case #" << i+1 << ": [";
    int size=result.size();
    int j;
    for(iter=result.begin(),j=0;iter!=result.end();iter++,j++){
      cout << *iter;
      fout << *iter;
      if(j!=size-1){
	cout << ", ";
	fout << ", ";
      }
    }
    cout << "]" << endl;
    fout << "]" << endl;
  }

  fin.close();
  fout.close();
}

list<char> runCase(){
  int C,D,N;

  int i;
  char combine[120];
  char oppose[60];
  char testStr[120];

  char tempStr[5];
  
  list<char> result; 

  combine[0]='\0';
  oppose[0]='\0';

  fin >> C;
  //cout << "combine:" << endl;
  for(i=0;i<C;i++){
    fin >> tempStr;
    //cout << tempStr << endl;
    strcat(combine,tempStr);
  }

  fin >> D;
  //cout << "oppose:" << endl;
  for(i=0;i<D;i++){
    fin >> tempStr;
    //cout << tempStr << endl;
    strcat(oppose,tempStr);
  }

  fin >> N;
  fin >> testStr;
  //cout << "test string : " << testStr << endl;

  int length=strlen(testStr);
  for(i=0;i<length;i++){
    if(result.size() == 0){
      result.push_back(testStr[i]);
    }
    else{
      list<char>::reverse_iterator riter;
      riter=result.rbegin();
      char output;
      output=checkTestStrInCombineList(*riter,testStr[i],combine);
      if(output!='\0'){
	result.pop_back();
	result.push_back(output);
      }
      else{
	list<int> matchOpposeList=checkTestStrInOpposeList(testStr[i],oppose);
	if(matchOpposeList.size()>0){
	  list<int>::iterator iter;
	  list<char>::iterator cit;
	  bool match_oppose=false;
	  for(cit=result.begin();cit!=result.end();cit++){
	    
	    for(iter=matchOpposeList.begin();iter!=matchOpposeList.end();iter++){
	      if(*cit==getPairOppose(*iter,oppose)){
		//cout << "match pair" << endl;
		match_oppose=true;
		break;
	      }
	    }
	    if(match_oppose)
	      break;

	  }
	  if(match_oppose)
	    result.clear();
	  else{
	    result.push_back(testStr[i]);
	  }
	}
	else{
	  result.push_back(testStr[i]);
	}
      }
    }
  }

  return result;
}

list<int> checkTestStrInOpposeList(char testChar,char* oppose){
  list<int> result;
  int size=strlen(oppose);

  int i;
  for(i=0;i<size;i++){
    if(testChar == oppose[i]){
      result.push_back(i);
      //cout << "Match : " << testChar << " at : " << i << endl;
    }
  }
  return result;
}

char getPairOppose(int charPos,char* oppose){
  if(charPos % 2 == 0)
    return oppose[charPos+1];
  else
    return oppose[charPos-1];
}

char checkTestStrInCombineList(char testChar,char testChar2,char *combine){
  char result='\0';
  int size=strlen(combine);
  int i;

  for(i=0;i<size;i+=3){
    if((testChar==combine[i] && testChar2==combine[i+1]) ||
       (testChar2==combine[i] && testChar==combine[i+1]))
      return combine[i+2];
  }

  return result;
}
