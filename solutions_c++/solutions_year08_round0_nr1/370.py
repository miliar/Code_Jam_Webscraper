#include<iostream>
#include<fstream>
#include<string>
#define MAXNAME 105
#define MAXWORD 105


using namespace std;

string searchEngineName[MAXNAME];
int searchEngineNum=0;
bool used[MAXNAME];


int getIndex(string name){
  for(int eng=0;eng<searchEngineNum;eng++)
    if(name.compare(searchEngineName[eng])==0)
      return eng;
  cout<<"Error, no match for '"+name+"'"<<endl;
  return -1;
}

bool allUsed(){
  for(int i=0;i<searchEngineNum;i++)
    if(!used[i])
      return false;
  return true;
}

int main(int argc, char* argv[]){
  ifstream fin (argv[1]);
  ofstream fout (argv[2]);
  int numcases;
  fin>>numcases;
  char temp[MAXWORD];
  for(int thisCase=1;thisCase<=numcases;thisCase++){
    fin>>searchEngineNum;
    fin.getline(temp,MAXWORD);
   
    for(int i=0;i<searchEngineNum;i++){
      fin.getline(temp,MAXWORD);
      searchEngineName[i]=string(temp);
      //cout<<i<<": "<<searchEngineName[i]<<endl;
      used[i]=false;
    }
    int swCount=0, numQueries=0;
    fin>>numQueries;
    fin.getline(temp,MAXWORD);
   
    int engNum;
    string name;
    for(int i=0;i<numQueries;i++){
      fin.getline(temp,MAXWORD);
      name=string(temp);
      //cout<<"query "<<i<<": "<<name<<endl;
      engNum=getIndex(name);
      used[engNum]=true;
      if(allUsed()){
	//cout<<"All used! Query "<<i<<endl;
	swCount++;
	for(int j=0;j<searchEngineNum;j++)
	  used[j]=false;
	used[engNum]=true;
      }
    }
    fout<<"Case #"<<thisCase<<": "<<swCount<<endl;
  }
  return 0;
}
