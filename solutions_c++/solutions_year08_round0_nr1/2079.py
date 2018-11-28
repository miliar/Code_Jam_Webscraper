#include<iostream>
#include<fstream>

using namespace std;

int N,S,Q;

char SE[150][150],input[150];

int getNumber(const char* s) {
        for(int i=0;i<S;i++)
                if(!strcmp(s,SE[i]))
                        return i;
        return 42; //shut up warnings
}

int main() {
        ifstream fin("input.txt");
        ofstream fout("output.txt");
        fin>>N;
  for(int i=1;i<=N;i++) {
          fin>>S;
          fin.getline(input,140);//read the '\n'
          for(int j=0;j<S;j++)
                  fin.getline(SE[j],140);
          int sol=0,uniq=0;
          bool visited[150];
          fill(visited,visited+S,false);
          fin>>Q;
          fin.getline(input,140);//read the '\n'
          for(int j=0;j<Q;j++) {
                  fin.getline(input,140);
                  if(!visited[getNumber(input)]) {
                          visited[getNumber(input)]=true;
                          uniq++;
                  }
                  if(uniq==S) {
                          sol++;
                          fill(visited,visited+S,false);
                          visited[getNumber(input)]=true;
                          uniq=1;
                  }
          }
          fout<<"Case #"<<i<<": "<<sol<<endl;
  }
        return 0;
}
