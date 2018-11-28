#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

void decomp( int a, int no[], const int pow[])
{
     int i=19;
     while (a>0)
     {
           if (pow[i]>a) {i--;}
           else
           {
               a-=pow[i];
               no[i]++;
           }
     }
}

void reduce( int a, int no[], const int pow[])
{
     int i=19;
     while (a>0)
     {
           if (pow[i]>a) {i--;}
           else
           {
               a-=pow[i];
               no[i]--;
           }
     }
}

bool addable( int a, int no[], const int pow[])
{
     int i=19;
     bool add = true;
     while ((a>0) && add)
     {
           if (pow[i]>a) {i--;}
           else
           {
               if (no[i]==1) {add = false; return add;}
               a-=pow[i];
           }
     }
     if (add) {reduce(a,no,pow); return add;}          
}

int main() {
    ifstream fin;
    ofstream fout;
    
    int test_case;
    fin.open("C_l.in");
    
    fout.open("output_c.txt");
    
    fin>>test_case;
    int gen[20];
    gen[0]=1;
    
    for (int i=1; i<20; i++)
    {
        gen[i] = gen[i-1]*2;
    }
    
    int tccnt=0;
    while (test_case!=tccnt)
    {
          tccnt++;
          //read
          int n;
          fin>>n;
          vector<int> s;
          int no[20];
          memset(no,0,sizeof(no));
          bool poss = true;
          for (int i=0; i<n; i++)
          {
              int temp;
              fin>>temp;
              s.push_back(temp);
              decomp(temp, no, gen);
          }
          for (int i=0; (i<20)&&poss; i++)
              if (no[i]%2==1) {poss = false;}
          int val=0;    
          if (poss)
          {
              sort(s.begin(), s.end());      
              for (int i=n-1; i>=1; i--)
              {
                if (addable(s[i],no,gen))
                {val += s[i];}
              }          
          }
          
          //print the answer
          fout<<"Case #"<<tccnt<<": ";
          if (poss) {fout<<val;} else {fout<<"NO";}
          fout<<endl;
          /*cout<<"Case #"<<tccnt<<": ";
          if (poss) {cout<<val;} else {cout<<"NO";}
          cout<<endl;*/
    }

cout<<"Finished!\n";
fin.close();
fout.close();
system ("pause");
return 0;
}
