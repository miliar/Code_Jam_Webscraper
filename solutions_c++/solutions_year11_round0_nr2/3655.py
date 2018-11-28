#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

#define MAX_STR_LEN 110
#define MAX_ARR_LEN 110


/* ifstream InitIO (const char *filename) {
  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;
  ofstream out(strcat(filename, ".out"));
  if (!out.is_open()) cout<<"OH NO"<<endl;
} */

typedef struct Oppose {
  char b;
  char a;
};

typedef struct Combine {
  char a;
  char b;
  char c;
};

class B{
  public:
    Oppose opp[MAX_ARR_LEN];
    Combine com[MAX_ARR_LEN];
    char que[MAX_ARR_LEN];
    char end[MAX_ARR_LEN];
    int resultnum;
    int no, nc, num;
    
    char DoCom (char a, char b) {
      if (!a) return b;
      for (int i=0;i<nc;i++)
        if (com[i].a==a&&com[i].b==b||com[i].a==b&&com[i].b==a)
          return com[i].c;
      return 0;
    }

    bool DoOpp (char a, int dex) {
      for (int i=0;i<dex;i++)
        for (int j=0; j<no; j++)
          if (opp[j].a==a&&opp[j].b==end[i]||opp[j].a==end[i]&&opp[j].b==a)
            return 0;
    return 1;
    }

    void Invoke () {
      char *ptend=end;
      char *ptque=que;
      char next;
      (*ptend)=(*ptque);
      ptque++;
      for (int i=1; i<num; i++, ptque++) {
        next=DoCom(*ptend,*ptque);
        if (next)
          (*ptend)=next;
        else {
          ptend++;
          (*ptend)=(*ptque);
        }
        if (!DoOpp(*ptend,ptend-end)) {
          ptend=end;
          (*ptend)=0;
        }
      }
      if (ptend==end&&!(*ptend))
        resultnum=0;
      else {
        (*(ptend+1))=0;
        resultnum=ptend-end+1;
      }
    }
    

    void Parse (ifstream &in) {
      char garbage;
      in>>nc;
      //cout<<endl<<nc<<endl;
      for (int i=0; i<nc; i++) {
        in.get(garbage);
        in.get(com[i].a);
        //cout<<com[i].a;
        in.get(com[i].b);
        //cout<<com[i].b;
        in.get(com[i].c);
        //cout<<com[i].c;
      }
      in>>no;
      //cout<<endl<<no<<endl;
      for (int i=0; i<no; i++) {
        //cout<<i<<" "<<no<<endl;
        in.get(garbage);
        in.get(opp[i].a);
        //cout<<opp[i].a;
        in.get(opp[i].b);
        //cout<<opp[i].b;
      }
      in>>num;
      in>>que;
      //cout<<endl<<num<<" "<<que<<endl<<endl;
    }
    
    void Output (ofstream &out) {
      //Parse(in);
      //Invoke();
      if (resultnum) {
      out<<"["<<end[0];
      for (int i=1; i<resultnum; i++) {
        out<<", "<<end[i];
      }
      out<<"]"<<endl;
      }
      else out<<"[]"<<endl;
    }
};

int main() {
  char filename[MAX_STR_LEN];
  cin>>filename;
  
  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;
  
  
  
  int many;
  in>>many;
  B b1[many+1];
  //int result[many+1];
  for (int i=1; i<=many; i++){
    (b1[i]).Parse(in);
    (b1[i]).Invoke();
  //  result[i]=a1.Run();
  //  cout<<result;
  //  cout<<"Case #"<<i<<": "<<result<<endl;
  }

  cin>>filename;
  ofstream out(filename);
  if (!out.is_open()) cout<<"OH NO"<<endl;
  for (int i=1; i<=many; i++) {
    out<<"Case #"<<i<<": ";
    (b1[i]).Output(out);
    //cout<<b1[i].nc<<b1[i].no<<b1[i].que<<endl;
    //out<<endl;
  }
  system("pause");
}
