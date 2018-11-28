#include <iostream>
#include <fstream>
#include <vector>


using namespace std; 

int main(int argc, char* argv[])
{
  std::ifstream input(argv[1]);
  int cases;
  input>> cases;
  for(int iter=1; iter<=cases; iter++)
  {
    int answer = 0;
    int elemcnt = 0;
    input >> elemcnt;
    int* pos=new int[elemcnt];
    char* seq = new char[elemcnt];
    int* opos = new int[elemcnt];
    int* bpos = new int[elemcnt];
    for(int i=0; i<elemcnt; i++)
         { opos[i]=0; bpos[i]=0;}
    int oidx=0; 
    int bidx=0; 
    for(int i=0; i<elemcnt; i++)
    {
       input>> seq[i];
       input>> pos[i];
       if(seq[i] == 'O') 
         opos[oidx++]=pos[i]; 
       else
         bpos[bidx++] = pos[i];
    } 

    int op=1;
    int bp=1;
    int idx=0;
    oidx=0; 
    bidx=0;
    int nexto=opos[oidx];
    int nextb=bpos[bidx];
 
    while(idx < elemcnt)
    {
//       cout << "element cnt =" <<elemcnt<<" idx="<<idx << " op="<<op<<" bp ="<<bp<<endl;
       if(seq[idx] == 'O')
       {
          if(pos[idx] == op) {
           idx++;
           nexto=opos[++oidx];
          }
          else
          {
             // move op toward nexto;
             if(nexto!=op) {
               if(nexto<op) op--;
               else
                 op++;
             }
          }
          if(nextb != bp) {
             if(nextb<bp) bp--;
             else
               bp++;
          }
          answer +=1;
       } 
       else
       {
          if(pos[idx] == bp) {
           idx++;
           nextb=bpos[++bidx];
          }
          else
          {
             // move op toward nexto;
             if(nextb!=bp) {
               if(nextb<bp) bp--;
               else
                 bp++;
             }
          }
          if(nexto != op) {
             if(nexto<op) op--;
             else
               op++;
          }
          answer +=1;
       } 


       }
        
    cout<<"Case #"<<iter<<": "<<answer<<endl;

  }  

}
